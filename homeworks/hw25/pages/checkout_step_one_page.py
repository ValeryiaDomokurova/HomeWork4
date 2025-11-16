from playwright.sync_api import Page
from homeworks.hw25.pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name = page.locator('[id="first-name"]')
        self.last_name = page.locator('[id="last-name"]')
        self.postal_code = page.locator('[id="postal-code"]')
        self.continue_button = page.locator('[id="continue"]')

    def fill_first_name(self, first_name):
        self.first_name.fill(first_name)

    def fill_last_name(self, last_name):
        self.last_name.fill(last_name)

    def fill_postal_code(self, postal_code):
        self.postal_code.fill(postal_code)

    def click_continue_button(self):
        self.continue_button.click()

    def fill_your_information(self, first_name, last_name, postal_code):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)
