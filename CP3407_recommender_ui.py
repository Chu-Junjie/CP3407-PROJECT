import os
import sqlite3
import pandas as pd
import streamlit as st
import requests


# ==============================================================================
# DATABASE INFRASTRUCTURE: CSV DATABASE SYNC (Fulfills US-02)
# ==============================================================================
def setup_database_infrastructure():
    csv_filename = "US-02 Database Setup & Import.csv"
    db_filename = "digital_products.db"
    table_name = "products"

    if not os.path.exists(csv_filename):
        return False

    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()

    try:
        cursor.execute(f"SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='{table_name}';")
        if cursor.fetchone()[0] > 0:
            connection.close()
            return True

        dataframe = pd.read_csv(csv_filename)
        dataframe.to_sql(table_name, connection, if_exists="replace", index=False)
        connection.commit()
        connection.close()
        return True
    except Exception:
        connection.close()
        return False


setup_database_infrastructure()


# ==============================================================================
# FRONTEND ENGINE: BUDGET INTERACTION & API INTEGRATION (Fulfills US-03 Expansion)
# ==============================================================================
def render_frontend_application():
    st.set_page_config(page_title="AI Device Recommender", page_icon="💻", layout="centered")

    st.title("💡 Smart Digital Product Recommender")
    st.markdown("### User Story 03: Customized Leaderboard with Price Ceiling Constraints")
    st.write(
        "Welcome! Specify your tech preferences along with your budget constraints to render custom matching rows.")
    st.write("---")

    # Step 1: Real User Preference Input Form (With New Pricing Capability)
    st.subheader("🔍 Step 1: Specify Your System & Budget Preferences")
    col1, col2 = st.columns(2)
    with col1:
        category_selection = st.selectbox(
            "Target Device Category",
            ["Smartphones", "Tablets", "Laptops", "Smart Watches", "Headphones"]
        )
    with col2:
        brand_selection = st.selectbox(
            "Target Brand Ecosystem",
            ["Samsung", "Apple", "Sony", "HP", "Other Brands"]
        )

    # NEW FEATURE: Interactive price constraint slider/number box input component
    price_ceiling = st.number_input(
        "Maximum Budget Constraint (USD $)",
        min_value=10.0,
        max_value=10000.0,
        value=1500.0,
        step=50.0,
        help="Products with database prices higher than this value will be automatically filtered out."
    )

    # Step 2: Trigger True Cross-Platform Request Pipeline
    st.subheader("🏆 Step 2: Live Algorithmic Output")

    if st.button("Generate Budget-Friendly Recommendations", type="primary"):
        # Package user configuration parameters including the new max_price constraint
        request_payload = {
            "category": category_selection,
            "brand": brand_selection,
            "max_price": price_ceiling
        }

        backend_url = "http://127.0.0.1:5000/api/recommend"

        with st.spinner(f"Transmitting metrics to backend server with budget capped at ${price_ceiling}..."):
            try:
                response = requests.post(backend_url, json=request_payload, timeout=5)

                if response.status_code == 200:
                    api_result = response.json()
                    products = api_result.get("data", [])

                    if products:
                        st.success(
                            f"🎉 [SUCCESS] Found real system items tracking under your ${price_ceiling:.2f} budget boundary!")
                        st.write("Top cost-effective database items ranking results:")
                        st.write("---")

                        for index, item in enumerate(products):
                            st.markdown(f"""
                            <div style="
                                background-color: #f8f9fa; 
                                padding: 15px; 
                                border-radius: 8px; 
                                border-left: 5px solid #28a745; 
                                margin-bottom: 12px;
                                box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
                            ">
                                <span style="font-weight: bold; color: #28a745; font-size: 1.1em;">RANK {index + 1}</span>
                                <h4 style="margin: 5px 0; color: #333;">{item['brand']} {item['category']}</h4>
                                <p style="margin: 0; font-size: 0.95em; color: #555;">
                                    <b>Product ID:</b> #{item['product_id']} | 
                                    <b>Live Query Price:</b> <span style="color: #28a745; font-weight: bold;">${item['price']:.2f}</span> | 
                                    <b>Algorithmic Match:</b> <span style="color: #dc3545; font-weight: bold;">{item['match_score']}%</span>
                                </p>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.warning(f"No products found that match the criteria and stay below ${price_ceiling:.2f}.")
                else:
                    st.error(f"Backend Server responded with error status code: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("❌ [CRITICAL CONNECTION ERROR] Cannot communicate with the real backend.")
                st.info("Ensure that `server.py` is currently actively running in another terminal window!")


if __name__ == "__main__":
    render_frontend_application()
