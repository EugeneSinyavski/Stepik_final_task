from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()

    def allert_guest_add_product_to_basket(self):
        alertinner_elements = self.browser.find_elements(*ProductPageLocators.ALERTINNER_ELEMENTS)
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        assert name_book.text == alertinner_elements[0].text, \
            "the name of the book in the cart does not match the product page"
        assert price.text == alertinner_elements[2].text, \
            "the price of the product does not match the price of the product in the cart"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
