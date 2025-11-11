# pylint: disable=import-error
# pylint: disable=line-too-long
import pytest
from playwright.sync_api import sync_playwright, expect


class TestSauceDemo:

    @pytest.fixture(scope='class')
    def browser_page(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto('https://www.saucedemo.com/')
            yield page
            browser.close()

    def test_login(self, browser_page):
        browser_page.locator('[name="user-name"]').fill("standard_user")
        browser_page.locator('[name="password"]').fill("secret_sauce")
        expect(browser_page.locator('[name="user-name"]')).to_have_value("standard_user")
        expect(browser_page.locator('[name="password"]')).to_have_value("secret_sauce")
        browser_page.locator('[class="submit-button btn_action"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/inventory.html')
        expect(browser_page.locator('[class="title"]')).to_have_text("Products")

    def test_add_card_button(self, browser_page):
        browser_page.locator('[id=add-to-cart-sauce-labs-backpack]').click()
        expect(browser_page.locator('[class=shopping_cart_link]')).to_have_text("1")
        expect(browser_page.locator('[id="remove-sauce-labs-backpack"]')).to_be_visible()
        expect(browser_page.locator('[class="title"]')).to_have_text("Products")

    def test_go_to_card_page(self, browser_page):
        browser_page.locator('[class=shopping_cart_link]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/cart.html')
        expect(browser_page.locator('[class="title"]')).to_have_text("Your Cart")
        browser_page.locator('[id="checkout"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/checkout-step-one.html')
        expect(browser_page.locator('[class="title"]')).to_have_text("Checkout: Your Information")

    def test_enter_your_information(self, browser_page):
        browser_page.locator('[id="first-name"]').fill("James")
        browser_page.locator('[id="last-name"]').fill("Bond")
        browser_page.locator('[id="postal-code"]').fill("123456")
        browser_page.locator('[id="continue"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/checkout-step-two.html')
        expect(browser_page.locator('[class="title"][class="title"]')).to_have_text("Checkout: Overview")

    def test_finish_button(self, browser_page):
        browser_page.locator('[id="finish"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/checkout-complete.html')
        expect(browser_page.locator('[class="title"]')).to_have_text("Checkout: Complete!")
