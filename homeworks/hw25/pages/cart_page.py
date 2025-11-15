# pylint: disable=import-error
from playwright.sync_api import Page
from homeworks.hw25.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_button = page.locator('[id="checkout"]')

    def click_checkout(self):
        self.checkout_button.click()
