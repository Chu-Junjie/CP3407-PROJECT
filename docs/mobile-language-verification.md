# Mobile layout and Chinese language support

The website defaults to English. The header language selector switches
between Chinese and English immediately and stores the preference in
`cp3407_language`. Switching languages preserves form values, recommendation
results, checked products, authentication and the current screen.

Localization is limited to presentation. API filter values, product IDs, USD
prices and persisted queries retain their existing format. Product names and user
identifiers are preserved. Known API messages and recommendation explanations are
translated; unfamiliar external text falls back to its original wording.

On screens up to 760 px, forms use a single column, product details occupy the full
card width, and account/favorite controls wrap. Buttons have a minimum 44 px
height. The comparison table scrolls independently, supports keyboard focus and
keeps its specification column visible. Safe-area padding and reduced-motion
preferences are supported.

## Verification

Install the existing backend requirements and the optional browser test package:

```sh
python -m pip install -r requirements.txt playwright
python tests/browser_smoke.py
python -m pytest -q test_server.py
```

The browser script uses installed Microsoft Edge by default. To use bundled
Chromium, run `python -m playwright install chromium` and set
`UI_BROWSER_CHANNEL=chromium` before running the script. Set `UI_SCREENSHOT_DIR`
for optional screenshots.

The browser script uses a temporary SQLite database and routes browser API
requests through the actual Flask test client. It never contacts production or
writes to the bundled database. Checks cover:

- English default, Chinese switch, persistence across reloads, and retained state.
- Both languages at 320, 375, 390, 430, 768 and 1280 px without page overflow.
- Registration, recommendations, favorites, comparison, history and feedback.
- Independent comparison-table scrolling and translated validation messages.
- Preserved product names and no uncaught JavaScript errors.

Validation on 2026-09-23: browser checks passed in headless Edge; all 12 canonical
backend tests passed. Mobile preference, result and comparison screenshots were
also reviewed. Real-device Safari behavior has not been tested.
