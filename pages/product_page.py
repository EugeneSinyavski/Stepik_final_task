from .base_page import BasePage
from .locators import ProductPageLokators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLokators.BASKET)
        basket.click()

    def allert_guest_add_product_to_basket(self):
        alertinner_elements = self.browser.find_elements(*ProductPageLokators.ALERTINNER_ELEMENTS)
        name_book = self.browser.find_element(*ProductPageLokators.NAME_BOOK)
        price = self.browser.find_element(*ProductPageLokators.PRICE)
        assert name_book.text == alertinner_elements[0].text, "lohi pedal"
        assert price.text == alertinner_elements[2].text, "gggfgf"
