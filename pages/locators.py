from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "#register_form button.btn.btn-lg.btn-primary")


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    ALERTINNER_ELEMENTS = (By.CSS_SELECTOR, "div.alertinner strong")
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    PRODUCT = (By.CSS_SELECTOR, "div.row h2.col-sm-6.h3")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")
