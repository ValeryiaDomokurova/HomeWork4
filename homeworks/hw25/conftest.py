# pylint: disable=import-error
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='class')
def browser_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.saucedemo.com/')
        yield page
        browser.close()
