#!/usr/bin/env python3
"""Build the 2,000-row recommendation catalogue from public real datasets.

The importer downloads four public Kaggle datasets through the unauthenticated
dataset API, maps their recorded fields into the application schema, and keeps
missing values as ``Not specified``. Prices are historical dataset snapshots;
EUR and INR values are converted with fixed, documented rates for comparison.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import shutil
import sqlite3
import ssl
import statistics
import urllib.request
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

REAL_ID_START = 10_000_001
EUR_TO_USD = 1.08
INR_PER_USD = 83.0
QUOTAS = {"Laptops": 800, "Smartphones": 833, "Smart Watches": 300, "Headphones": 61, "Tablets": 6}
DATASETS = {
    "laptops": {
        "slug": "ironwolf437/laptop-price-dataset",
        "file": "laptop_price - dataset.csv",
        "source": "Kaggle laptop-price-dataset (Apache-2.0)",
    },
    "smartphones": {
        "slug": "muzammilbaloch/smartphone-dataset",
        "file": "smartphones.csv",
        "source": "Kaggle smartphone-dataset (Apache-2.0)",
    },
    "watches": {
        "slug": "devsubhash/fitness-trackers-products-ecommerce",
        "file": "Fitness_trackers_updated.csv",
        "source": "Flipkart fitness trackers (CC BY-SA 4.0)",
    },
    "electronics": {
        "slug": "manishkc06/electronics-product-pricing-dataset",
        "file": "electronics_products_pricing.csv",
        "source": "Datafiniti electronics pricing (CC0)",
    },
}


def clean(value: Any, fallback: str = "Not specified") -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text if text else fallback


def number(value: Any) -> float | None:
    match = re.search(r"-?\d+(?:\.\d+)?", str(value or "").replace(",", ""))
    return float(match.group()) if match else None


def dataset_page(slug: str) -> str:
    return f"https://www.kaggle.com/datasets/{slug}"


def download_sources(cache: Path) -> dict[str, Path]:
    cache.mkdir(parents=True, exist_ok=True)
    context = ssl.create_default_context()
    result: dict[str, Path] = {}
    for key, metadata in DATASETS.items():
        target = cache / str(metadata["file"])
        if not target.exists():
            url = f"https://www.kaggle.com/api/v1/datasets/download/{metadata['slug']}"
            print(f"Downloading {metadata['slug']} ...")
            request = urllib.request.Request(url, headers={"User-Agent": "CP3407 catalogue importer/2.0"})
            with urllib.request.urlopen(request, timeout=120, context=context) as response:
                archive = zipfile.ZipFile(io.BytesIO(response.read()))
                member = next((name for name in archive.namelist() if Path(name).name == metadata["file"]), None)
                if member is None:
                    raise RuntimeError(f"Expected {metadata['file']} in {metadata['slug']}")
                target.write_bytes(archive.read(member))
        result[key] = target
    return result


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def base_record(category: str, brand: str, name: str, price: float, source_key: str) -> dict[str, Any]:
    metadata = DATASETS[source_key]
    return {
        "ProductCategory": category,
        "ProductBrand": clean(brand, "Unknown"),
        "ProductName": clean(name),
        "ProductPrice": round(price, 2),
        "CPU": "Not specified",
        "GPU": "Not specified",
        "RAM": "Not specified",
        "Storage": "Not specified",
        "ScreenSize": "Not specified",
        "BatteryLife": "Not specified",
        "Weight": "Not specified",
        "UseCase": "general",
        "PurchaseURL": dataset_page(str(metadata["slug"])),
        "DataSource": metadata["source"],
        "PurchaseFrequency": 0,
        "CustomerSatisfaction": 0,
        "PurchaseIntent": 0,
    }


def laptop_records(path: Path) -> list[dict[str, Any]]:
    records = []
    for row in read_csv(path):
        price = number(row.get("Price (Euro)"))
        if not price or price <= 0:
            continue
        record = base_record("Laptops", row.get("Company", ""), row.get("Product", ""), price * EUR_TO_USD, "laptops")
        record.update({
            "CPU": clean(f"{row.get('CPU_Company', '')} {row.get('CPU_Type', '')} {row.get('CPU_Frequency (GHz)', '')} GHz"),
            "GPU": clean(f"{row.get('GPU_Company', '')} {row.get('GPU_Type', '')}"),
            "RAM": clean(f"{row.get('RAM (GB)', '')}GB"),
            "Storage": clean(row.get("Memory")),
            "ScreenSize": clean(f"{row.get('Inches', '')} inch · {row.get('ScreenResolution', '')}"),
            "Weight": clean(f"{row.get('Weight (kg)', '')} kg"),
            "UseCase": clean(f"study office portable {row.get('TypeName', '')} {row.get('OpSys', '')}"),
        })
        records.append(record)
    return records


def smartphone_records(path: Path) -> list[dict[str, Any]]:
    records = []
    for row in read_csv(path):
        price = number(row.get("price"))
        if not price or price <= 0:
            continue
        rating = number(row.get("avg_rating")) or 0
        record = base_record("Smartphones", row.get("brand_name", "").title(), row.get("model", ""), price / INR_PER_USD, "smartphones")
        record.update({
            "CPU": clean(f"{row.get('processor_brand', '')} · {row.get('num_cores', '')} cores · {row.get('processor_speed', '')} GHz"),
            "RAM": clean(f"{row.get('ram_capacity', '')}GB"),
            "Storage": clean(f"{row.get('internal_memory', '')}GB"),
            "ScreenSize": clean(f"{row.get('screen_size', '')} inch · {row.get('resolution_width', '')}×{row.get('resolution_height', '')} · {row.get('refresh_rate', '')}Hz"),
            "BatteryLife": clean(f"{row.get('battery_capacity', '')} mAh capacity"),
            "UseCase": clean(f"camera communication portable {row.get('os', '')} {'5G' if row.get('5G_or_not') == '1' else '4G'}"),
            "CustomerSatisfaction": max(0, min(5, round(rating / 2))),
            "PurchaseIntent": int(rating >= 8),
        })
        records.append(record)
    return records


def watch_records(path: Path) -> list[dict[str, Any]]:
    records = []
    for row in read_csv(path):
        if clean(row.get("Device Type"), "").lower() != "smartwatch":
            continue
        price = number(row.get("Selling Price"))
        if not price or price <= 0:
            continue
        rating = number(row.get("Rating (Out of 5)")) or 0
        reviews = number(row.get("Reviews")) or 0
        name = clean(f"{row.get('Model Name', '')} · {row.get('Color', '')}")
        record = base_record("Smart Watches", row.get("Brand Name", ""), name, price / INR_PER_USD, "watches")
        record.update({
            "ScreenSize": clean(row.get("Display")),
            "BatteryLife": clean(f"{row.get('Average Battery Life (in days)', '')} days"),
            "UseCase": clean(f"fitness notifications wearable {row.get('Strap Material', '')}"),
            "CustomerSatisfaction": max(0, min(5, round(rating))),
            "PurchaseFrequency": max(0, min(10, round(reviews / 100))),
            "PurchaseIntent": int(rating >= 4),
        })
        records.append(record)
    return records


def electronics_records(path: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in read_csv(path):
        grouped.setdefault(clean(row.get("id")), []).append(row)
    headphones: list[dict[str, Any]] = []
    tablets: list[dict[str, Any]] = []
    excluded = re.compile(r"case|cover|cable|adapter|replacement|earpad|ear pad|stand|holder|mount|speaker|charger", re.I)
    tablet_excluded = re.compile(r"case|cover|dock|mouse|trackball|headset|headphone|stylus|pen|backpack|bumper|kit|accessory|protector|mount|laptop", re.I)
    for observations in grouped.values():
        row = max(observations, key=lambda item: sum(bool(value) for value in item.values()))
        title = clean(row.get("name"))
        lower_title = title.lower()
        recorded_prices = [value for value in (number(item.get("price")) for item in observations) if value and value > 0]
        price = statistics.median(recorded_prices) if recorded_prices else None
        if not price or price <= 0:
            continue
        if re.search(r"headphones?", lower_title) and not excluded.search(lower_title):
            record = base_record("Headphones", row.get("brand", ""), title, price, "electronics")
            record.update({"CPU": "Not applicable", "GPU": "Not applicable", "RAM": "Not applicable", "Storage": "Not applicable", "ScreenSize": "Not applicable", "Weight": clean(row.get("weight")), "UseCase": "music audio travel office"})
            record["PurchaseURL"] = clean(row.get("sourceURLs"), record["PurchaseURL"]).split(",")[0]
            headphones.append(record)
        categories = str(row.get("categories", "")).lower()
        if (re.search(r"\bipad\b|\btablet\b|galaxy tab", lower_title) and ("tablets" in categories or "ipad" in categories) and not tablet_excluded.search(lower_title)):
            record = base_record("Tablets", row.get("brand", ""), title, price, "electronics")
            record.update({"Weight": clean(row.get("weight")), "UseCase": "study creative portable media"})
            record["PurchaseURL"] = clean(row.get("sourceURLs"), record["PurchaseURL"]).split(",")[0]
            tablets.append(record)
    return headphones, tablets


def select_records(paths: dict[str, Path]) -> list[dict[str, Any]]:
    pools: dict[str, list[dict[str, Any]]] = {
        "Laptops": laptop_records(paths["laptops"]),
        "Smartphones": smartphone_records(paths["smartphones"]),
        "Smart Watches": watch_records(paths["watches"]),
    }
    pools["Headphones"], pools["Tablets"] = electronics_records(paths["electronics"])
    selected: list[dict[str, Any]] = []
    for category, quota in QUOTAS.items():
        pool = sorted(pools[category], key=lambda row: (row["ProductBrand"].lower(), row["ProductName"].lower(), row["ProductPrice"]))
        if len(pool) < quota:
            raise RuntimeError(f"Only {len(pool)} valid {category} rows; {quota} required")
        selected.extend(pool[:quota])
    return selected


def delete_private_rows(connection: sqlite3.Connection) -> None:
    for table in ("favorites", "search_results", "search_history", "feedback", "users"):
        if connection.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)).fetchone():
            connection.execute(f"DELETE FROM {table}")


def write_database(source: Path, output: Path, records: list[dict[str, Any]], csv_output: Path) -> None:
    if source.resolve() != output.resolve():
        shutil.copy2(source, output)
    connection = sqlite3.connect(output)
    now = datetime.now(timezone.utc).isoformat()
    csv_rows: list[dict[str, Any]] = []
    try:
        with connection:
            delete_private_rows(connection)
            connection.execute("DELETE FROM product_specs")
            connection.execute("DELETE FROM products WHERE ProductID >= ?", (REAL_ID_START,))
            for offset, record in enumerate(records):
                product_id = REAL_ID_START + offset
                connection.execute(
                    """INSERT INTO products
                       (ProductID, ProductCategory, ProductBrand, ProductPrice, CustomerAge,
                        CustomerGender, PurchaseFrequency, CustomerSatisfaction, PurchaseIntent)
                       VALUES (?, ?, ?, ?, NULL, NULL, ?, ?, ?)""",
                    (product_id, record["ProductCategory"], record["ProductBrand"], record["ProductPrice"], record["PurchaseFrequency"], record["CustomerSatisfaction"], record["PurchaseIntent"]),
                )
                spec = {"ProductID": product_id, **{key: record[key] for key in ("ProductName", "CPU", "GPU", "RAM", "Storage", "ScreenSize", "BatteryLife", "Weight", "UseCase", "PurchaseURL", "DataSource")}, "LastUpdated": now}
                connection.execute(
                    """INSERT INTO product_specs
                       (ProductID, ProductName, CPU, GPU, RAM, Storage, ScreenSize, BatteryLife,
                        Weight, UseCase, PurchaseURL, DataSource, LastUpdated)
                       VALUES (:ProductID, :ProductName, :CPU, :GPU, :RAM, :Storage, :ScreenSize,
                               :BatteryLife, :Weight, :UseCase, :PurchaseURL, :DataSource, :LastUpdated)""",
                    spec,
                )
                csv_rows.append({**spec, "ProductCategory": record["ProductCategory"], "ProductBrand": record["ProductBrand"], "ProductPriceUSD": record["ProductPrice"]})
        with csv_output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(csv_rows[0]))
            writer.writeheader()
            writer.writerows(csv_rows)
    finally:
        connection.close()


def verify_database(path: Path, expected: int) -> None:
    connection = sqlite3.connect(path)
    try:
        tables = {}
        for table in ("products", "product_specs", "users", "search_history", "favorites", "feedback"):
            tables[table] = connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        categories = dict(connection.execute("""SELECT p.ProductCategory, COUNT(*) FROM products p
            JOIN product_specs s ON p.ProductID=s.ProductID GROUP BY p.ProductCategory ORDER BY p.ProductCategory"""))
        sources = dict(connection.execute("SELECT DataSource, COUNT(*) FROM product_specs GROUP BY DataSource"))
    finally:
        connection.close()
    if tables["product_specs"] != expected or categories != QUOTAS:
        raise RuntimeError(f"Catalogue validation failed: {tables=} {categories=}")
    if any(tables[key] for key in ("users", "search_history", "favorites", "feedback")):
        raise RuntimeError(f"Private rows remain: {tables}")
    print(json.dumps({"tables": tables, "categories": categories, "sources": sources}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("digital_products.db"))
    parser.add_argument("--output", type=Path, default=Path("digital_products_real.db"))
    parser.add_argument("--csv-output", type=Path, default=Path("real_product_catalog.csv"))
    parser.add_argument("--cache", type=Path, default=Path(".catalog-source-cache"))
    args = parser.parse_args()
    paths = download_sources(args.cache)
    records = select_records(paths)
    write_database(args.source, args.output, records, args.csv_output)
    verify_database(args.output, sum(QUOTAS.values()))


if __name__ == "__main__":
    main()
