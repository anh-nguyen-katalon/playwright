from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://testops.staging.katalon.com', wait_until='networkidle')
    page.locator('[name=username]').fill('hai.nguyen+4@katalon.com')
    page.locator('[name=password]').fill('-9gBFiixf8H2wXg')
    page.locator('.signin-button').click()
    time.sleep(1)
    context.storage_state(path='storage_state.json')
    context.close()
