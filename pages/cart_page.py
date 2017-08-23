# -*- coding: UTF-8 -*-
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_item_presence(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".shortcuts .shortcut:first-child")
            return True
        except NoSuchElementException:
            return False

    def get_summary_block_element(self):
        return self.driver.find_element_by_css_selector("#box-checkout-summary")

    def click_on_carousel(self):
        self.driver.find_element_by_css_selector(".shortcuts .shortcut:first-child").click()

    def remove_item_from_cart(self):
        self.driver.find_element_by_css_selector(".viewport .item:first-child button[name=remove_cart_item]").click()

    def get_current_cart(self):
        return self.driver.find_element_by_css_selector("#checkout-cart-wrapper .viewport")

    def wait_dom_to_change(self, current_cart_locator):
        self.wait.until(EC.staleness_of(current_cart_locator))

    def check_cart_not_empty(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "#checkout-cart-wrapper .viewport")
            return True
        except NoSuchElementException:
            return False

    def wait_table_to_update(self, summary_block_element):
        self.wait.until(EC.staleness_of(summary_block_element))
