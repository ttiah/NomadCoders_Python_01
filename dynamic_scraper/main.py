from playwright.sync_api import sync_playwright

p = sync_playwright().start()
b = p.chromium.launch(headless=False)
page = b.new_page()
page.goto('https://daum.net')
page.screenshot(path='daum.png')
