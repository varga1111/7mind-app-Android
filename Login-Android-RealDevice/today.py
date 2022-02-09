from appium.webdriver.common.appiumby import AppiumBy as By

from basemethods import Base_methods
import time

class Today(Base_methods):
    ''' By Locators'''

   


    def __init__(self, driver):
        
        super().__init__(driver)

    
    def my_journey_visible(self):
        self.driver.implicitly_wait(3)

        my_journey_btn = self.driver.find_element_by_accessibility_id('Back to My Journey')
        text = my_journey_btn.text
        assert text == 'My Journey'
        return bool(my_journey_btn)

        