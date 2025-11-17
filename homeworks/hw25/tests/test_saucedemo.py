from playwright.sync_api import expect
from homeworks.hw25.pages.login_page import LoginPage
from homeworks.hw25.pages.products_page import ProductsPage
from homeworks.hw25.pages.cart_page import CartPage
from homeworks.hw25.pages.checkout_step_one_page import CheckoutStepOnePage
from homeworks.hw25.pages.checkout_step_two_page import CheckoutStepTwoPage


class TestSauceDemo:
    def test_login(self, browser_page):
        page = browser_page
        login_page = LoginPage(page)
        login_page.navigate('https://www.saucedemo.com/')

        login_page.fill_username("standard_user")
        login_page.fill_password("secret_sauce")
        login_page.click_login_button()

        assert login_page.is_url_contains('/inventory.html')
        expect(page.locator('[class="title"]')).to_have_text("Products")

    def test_add_to_cart(self, browser_page):
        page = browser_page

        products_page = ProductsPage(page)
        products_page.add_product_to_cart()

        assert products_page.is_url_contains('/inventory.html')
        expect(page.locator('[class="title"]')).to_have_text("Products")

    def test_go_to_cart_page(self, browser_page):
        page = browser_page

        products_page = ProductsPage(page)
        products_page.go_to_cart()

        assert products_page.is_url_contains('/cart.html')
        expect(page.locator('[class="title"]')).to_have_text("Your Cart")

    def test_enter_your_information(self, browser_page):
        page = browser_page

        cart_page = CartPage(page)
        cart_page.click_checkout()

        assert cart_page.is_url_contains('/checkout-step-one.html')
        expect(page.locator('[class="title"]')).to_have_text("Checkout: Your Information")

        checkout_step_one_page = CheckoutStepOnePage(page)
        checkout_step_one_page.fill_your_information("James", "Bond", "123456")
        checkout_step_one_page.click_continue_button()

        assert checkout_step_one_page.is_url_contains('/checkout-step-two.html')
        expect(page.locator('[class="title"]')).to_have_text("Checkout: Overview")

    def test_finish_button(self, browser_page):
        page = browser_page

        checkout_step_two_page = CheckoutStepTwoPage(page)
        checkout_step_two_page.click_finish_button()

        assert checkout_step_two_page.is_url_contains('/checkout-complete.html')
        expect(page.locator('[class="title"]')).to_have_text("Checkout: Complete!")
