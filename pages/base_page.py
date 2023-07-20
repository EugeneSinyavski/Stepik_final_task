import logging
import math
import os
import re

import allure
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators, BasketPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.logger = self.__logger_init()

    def __logger_init(self):
        logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        clean_logname = self.clean_test_name_for_logging(self.browser.test_name)
        file = logging.FileHandler(f"logs/{clean_logname}.log")
        file.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s"))
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(file)
        logger.setLevel(self.browser.log_level)
        return logger

    def open(self):
        with allure.step(f"Open URL: {self.url}"):
            self.logger.info(f"Opening URL: {self.url}")
            self.browser.get(self.url)

    def is_element_present(self, how, what):
        with allure.step(f"Checking if element '{how}:{what}' is not present on the page"):
            self.logger.info(f"Waiting for element '{how}:{what}' is present on the page")
            try:
                self.browser.find_element(how, what)
            except NoSuchElementException:
                self.logger.error(f"Element '{how}:{what}' is not present on the page")
                return False
            return True

    def is_not_element_present(self, how, what, timeout=4):
        with allure.step(f"Checking if element '{how}:{what}' is not present on the page"):
            self.logger.info(f"Waiting for element '{how}:{what}' is not present on the page")
            try:
                WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            except TimeoutException:
                return True
            self.logger.error(f"Element '{how}:{what}' is present on the page")
            return False

    def is_disappeared(self, how, what, timeout=4):
        with allure.step(f"Checking if element '{how}:{what}' is disappeared on the page"):
            self.logger.info(f"Waiting for element '{how}:{what}' is disappeared on the page")
            try:
                WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until_not(EC.presence_of_element_located((how, what)))
            except TimeoutException:
                self.logger.error(f"Element '{how}:{what}' is not disappeared on the page")
                return False
            return True

    @allure.step("Going to the basket page")
    def go_to_basket_page(self):
        view_basket = self.browser.find_element(*BasketPageLocators.VIEW_BASKET)
        view_basket.click()

    @allure.step("Going to the login page")
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    @allure.step("Checking if user is authorized")
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    @allure.step("Checking if login link is present")
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    @staticmethod
    def clean_test_name_for_logging(test_name):
        pattern = r'[^\w\-]'
        clean_name = re.sub(pattern, '_', test_name)
        return clean_name

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
