from launchapp import Launch
from testdata import Testdata
from login import Login

import pytest

class Test_login(Launch):
    
    def test_navigation_continue_btn(self):
        driver = Login(self.driver)

        driver.navigation_continue_btn()

    def test_navigation_login_btn(self):
        driver = Login(self.driver)

        driver.navigation_login_btn()

    def test_navigation_email_btn(self):
        driver = Login(self.driver)

        driver.navigation_email_btn()

    def test_do_login_email(self):
        driver = Login(self.driver)
    
        driver.do_login_email(Testdata.email)

    def test_do_login_password(self):
        driver = Login(self.driver)
        
        driver.do_login_password(Testdata.password)