from appium.webdriver.common.appiumby import AppiumBy as By

from basemethods import Base_methods

from today import Today


class Login(Base_methods):

    ''' By Locators'''
    continue_button = (By.ID, 'de.sevenmind.android:id/actionButton')
    login_button = (By.ID, 'de.sevenmind.android:id/actionButton')
    email_button = (By.ID, 'de.sevenmind.android:id/actionButton')
    email_input = (By.ID, 'de.sevenmind.android:id/cellDialogTextInputEditText')
    password_input = (By.ID, 'de.sevenmind.android:id/cellDialogTextInputEditText')


    def __init__(self, driver):
    
        super().__init__(driver)


    def navigation_continue_btn(self):
       self.do_click(self.continue_button)


    def navigation_login_btn(self):
        self.do_click(self.continue_button)


    def navigation_email_btn(self):
        self.do_click(self.continue_button)


    def do_login_email(self, email):
        self.do_send_keys(self.email_input, email)
        self.driver.press_keycode(66)


    def do_login_password(self, password):
        self.do_send_keys(self.password_input, password)
        self.driver.press_keycode(66)
        self.driver.implicitly_wait(3)
        
        return Today(self.driver)