# -*- coding: UTF-8 -*-
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/")
        self.wait.until(EC.title_is("Online Store | Test Selenium Store"))
        return self

    def get_first_product(self):
        return self.driver.find_element_by_css_selector(".content a.link")
