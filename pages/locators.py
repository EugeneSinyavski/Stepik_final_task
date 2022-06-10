from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLokators:
    BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    ALERTINNER_ELEMENTS = (By.CSS_SELECTOR, "div.alertinner strong")
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
