from selenium import webdriver
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 5)
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_few_items_to_cart(self, count):

        i = 1

        while i < count + 1:
            self.main_page.open()
            self.main_page.get_first_product().click()

            self.product_page.add_item_to_cart()
            self.product_page.wait_cart_count_increase(i)

            i += 1

    def delete_items_from_cart(self):
        self.product_page.get_cart_link().click()
        while True:
            # remember current table locator
            summary_block_element = self.cart_page.get_summary_block_element()

            # stop the carousel if we have one
            if self.cart_page.check_item_presence():
                self.cart_page.click_on_carousel()

            # remember current DOM locator
            current_cart_locator = self.cart_page.get_current_cart()

            # remove the item
            self.cart_page.remove_item_from_cart()

            # waiting for DOM to change
            self.cart_page.wait_dom_to_change(current_cart_locator)

            # check table
            self.cart_page.wait_table_to_update(summary_block_element)

            # stop cycle if cart is empty
            if not self.cart_page.check_cart_not_empty():
                break


