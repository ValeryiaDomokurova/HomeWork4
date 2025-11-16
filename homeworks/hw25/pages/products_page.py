from playwright.sync_api import Page
from homeworks.hw25.pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_button = page.locator('[class=shopping_cart_link]')
        self.product = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')

    def add_product_to_cart(self):
        self.product.click()

    def go_to_cart(self):
        self.cart_button.click()
