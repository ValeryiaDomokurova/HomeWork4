import pytest
from playwright.sync_api import sync_playwright, expect


playwright = sync_playwright().start()


class TestSauceDemo:

    @pytest.fixture
    def browser_page(self):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://saucedemo.com/")
        yield page
        browser.close()
        playwright.stop()

    def test_login(self, browser_page):
        browser_page.locator('[name="user-name"]').fill("standard_user")
        browser_page.locator('[name="password"]').fill("")