import time

from launchapp import Launch


class Login(Launch):

    def __init__(self, driver):

        self.driver = driver


    def navigation_continue_btn(self):
        time.sleep(3)
        self.driver.implicitly_wait(5)
        continue_button = self.driver.find_element_by_id('de.sevenmind.android:id/actionButton')
        continue_button.click()

        
    def navigation_login_btn(self):
        time.sleep(3)
        self.driver.implicitly_wait(5)
        login_button = self.driver.find_element_by_id('de.sevenmind.android:id/actionButton')
        login_button.click()


    def navigation_email_btn(self):
        time.sleep(3)
        self.driver.implicitly_wait(5)
        email_button = self.driver.find_element_by_id('de.sevenmind.android:id/actionButton')
        email_button.click()
        

    def do_login_email(self, email):
        time.sleep(3)
        self.driver.implicitly_wait(5)
        email_input = self.driver.find_element_by_id('de.sevenmind.android:id/cellDialogTextInputEditText')
        email_input.send_keys(email)
        self.driver.press_keycode(66)


    def do_login_password(self, password):
        time.sleep(3)
        self.driver.implicitly_wait(5)
        password_input = self.driver.find_element_by_id('de.sevenmind.android:id/cellDialogTextInputEditText')
        password_input.send_keys(password)
        self.driver.press_keycode(66)