# -*- coding: UTF-8 -*-
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[name=add_cart_product]")))
        if self.driver.find_element(By.CSS_SELECTOR, "h1.title").get_attribute("innerText") == "Yellow Duck":
            self.driver.find_element_by_css_selector("select[name='options[Size]']").click()
            self.driver.find_element_by_css_selector("select[name='options[Size]'] option:nth-child(2)").click()

        self.driver.find_element_by_css_selector("button[name=add_cart_product]").click()
        return self

    def wait_cart_count_increase(self, i):
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart .quantity"), str(i)))

    def get_cart_link(self):
        return self.driver.find_element_by_css_selector("#cart-wrapper .link")