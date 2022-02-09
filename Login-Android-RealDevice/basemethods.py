from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from launchapp import Launch


from testdata import Testdata

'''This class is the parent of all pages.'''
'''It contains all the generic methods and utilities for all pages.'''
class Base_methods(Launch):

    def __init__(self, driver):
        self.driver = driver
        

    def do_click(self, by_locator):
         wait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)).click()


    def do_send_keys(self, by_locator, text):
        wait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).send_keys(text)


    def is_visible(self, by_locator):
        element = wait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    
    def get_title(self, title):
        wait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    
    def hover(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()