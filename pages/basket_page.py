from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
            "Product is presented, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "Message is not presented, but should be"
