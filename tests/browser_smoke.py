"""Browser regression checks against the real Flask API and a temporary database.

Install requirements.txt and playwright, then run:
    python tests/browser_smoke.py
Uses installed Edge; set UI_BROWSER_CHANNEL=chromium for Playwright Chromium.
Optional UI_SCREENSHOT_DIR writes review screenshots outside the repository.
"""
import os
from pathlib import Path
import sys
import tempfile

from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main():
    with tempfile.TemporaryDirectory() as temp:
        os.environ['DATABASE_URL'] = 'sqlite:///' + str(Path(temp) / 'ui.db')
        import server
        server.setup_database()
        client = server.app.test_client()
        try:
            with sync_playwright() as playwright:
                channel = os.environ.get('UI_BROWSER_CHANNEL', 'msedge')
                browser = playwright.chromium.launch(channel=channel, headless=True)
                context = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.route('http://127.0.0.1:8000/', lambda route: route.fulfill(content_type='text/html', body=(ROOT / 'index.html').read_text(encoding='utf-8')))

                def api(route):
                    request = route.request
                    path = request.url.split(':5000', 1)[1]
                    response = client.open(path, method=request.method, data=request.post_data, headers={key: value for key, value in request.headers.items() if key.lower() in ('content-type', 'authorization')})
                    route.fulfill(status=response.status_code, content_type='application/json', body=response.get_data(as_text=True))

                page.route('http://127.0.0.1:5000/api/**', api)
                page.goto('http://127.0.0.1:8000/')
                expect(page.locator('html')).to_have_attribute('lang', 'zh-CN')
                expect(page.locator('#submitBtn')).to_have_text('查找推荐产品')

                def fits():
                    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), page.evaluate('({width: innerWidth, scroll: document.documentElement.scrollWidth})')

                def screenshots(name):
                    if os.environ.get('UI_SCREENSHOT_DIR'):
                        target = Path(os.environ['UI_SCREENSHOT_DIR'])
                        target.mkdir(parents=True, exist_ok=True)
                        page.screenshot(path=str(target / (name + '.png')), full_page=True)

                for width in (320, 375, 390, 430, 768, 1280):
                    page.set_viewport_size({'width': width, 'height': 844})
                    for lang in ('en', 'zh-CN'):
                        page.locator('#languageSelect').select_option(lang)
                        fits()
                page.set_viewport_size({'width': 390, 'height': 844})
                screenshots('mobile-preferences')
                page.locator('#categorySelect').select_option('Smartphones')
                page.locator('#languageSelect').select_option('en')
                expect(page.locator('#categorySelect')).to_have_value('Smartphones')
                page.reload()
                expect(page.locator('html')).to_have_attribute('lang', 'en')
                page.locator('#languageSelect').select_option('zh-CN')
                page.reload()
                expect(page.locator('html')).to_have_attribute('lang', 'zh-CN')
                page.locator('#authUsername').fill('mobile-user-with-a-long-name')
                page.locator('#authEmail').fill('mobile@example.com')
                page.locator('#authPassword').fill('Password123!')
                page.locator('#registerBtn').click()
                expect(page.locator('#userMenuBtn')).to_be_visible()
                page.locator('#submitBtn').click()
                expect(page.locator('.product-card').first).to_be_visible()
                expect(page.locator('#pageStatus')).to_contain_text('匹配结果')
                original_name = page.locator('.product-name').first.inner_text()
                for index in (0, 1):
                    page.locator('.compare-checkbox').nth(index).check()
                    page.locator('.favorite-btn').nth(index).click()
                    expect(page.locator('.favorite-btn').nth(index)).to_have_text('♥ 已收藏')
                page.locator('#languageSelect').select_option('en')
                expect(page.locator('.compare-checkbox').first).to_be_checked()
                expect(page.locator('.product-name').first).to_have_text(original_name)
                expect(page.locator('.favorite-btn').first).to_have_text('♥ Saved')
                page.locator('#languageSelect').select_option('zh-CN')
                for width in (320, 390, 768, 1280):
                    page.set_viewport_size({'width': width, 'height': 844})
                    fits()
                page.set_viewport_size({'width': 390, 'height': 844})
                screenshots('mobile-results')
                page.locator('#compareBtn').click()
                expect(page.locator('#compareTableContainer th').first).to_have_text('规格')
                fits()
                assert page.locator('#compareTableContainer').evaluate('(el) => el.scrollWidth > el.clientWidth')
                page.locator('#compareTableContainer').evaluate('(el) => el.scrollLeft = 200')
                assert page.locator('#compareTableContainer').evaluate('(el) => el.scrollLeft > 0')
                screenshots('mobile-comparison')
                page.locator('#languageSelect').select_option('en')
                expect(page.locator('#compareTableContainer th').first).to_have_text('Feature')
                page.locator('#languageSelect').select_option('zh-CN')
                page.locator('#backToLeaderboardBtn').click()
                page.locator('#helpfulBtn').click()
                expect(page.locator('#feedbackStatus')).to_contain_text('感谢反馈')
                page.locator('#userMenuBtn').click()
                expect(page.locator('.favorite-item')).to_have_count(2)
                expect(page.locator('.history-item').first).to_be_visible()
                page.set_viewport_size({'width': 320, 'height': 844})
                fits()
                for index in (0, 1):
                    page.locator('.favorite-item input').nth(index).check()
                page.locator('#languageSelect').select_option('en')
                expect(page.locator('.favorite-item input').first).to_be_checked()
                page.locator('#compareFavoritesBtn').click()
                expect(page.locator('#compareSection')).to_be_visible()
                fits()
                page.locator('#languageSelect').select_option('zh-CN')
                page.locator('#backToLeaderboardBtn').click()
                page.locator('#accountLogoutBtn').click()
                expect(page.locator('#authMessage')).to_have_text('你已退出登录。')
                page.locator('#preferredBrandSelect').select_option('Apple')
                page.locator('#excludedBrandSelect').select_option('Apple')
                page.locator('#submitBtn').click()
                expect(page.locator('#errorBox')).to_have_text('偏好品牌与排除品牌不能相同。')
                assert not errors, errors
                browser.close()
                print('PASS: bilingual layouts at 320–1280px; language persistence; state preservation; registration; recommendations; favorites; comparison; history; feedback; validation; no JS errors.')
        finally:
            server.engine.dispose()


if __name__ == '__main__':
    main()
