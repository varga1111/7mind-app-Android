from appium import webdriver
import pytest
#from applitools.selenium import Eyes
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class Launch():

    '''eyes = Eyes()
    eyes.api_key = 'YOUR_API_KEY' 
    '''

    desired_cap = {
    "deviceName": "R58R90GEM4R",
    "platformName": "Android",
    "app": "/Users/openmindschooling/MyStuff/Mobile_App_Testing/Android/Apps/7Mind Meditation reinvented_v2.50.0_apkpure.com.apk",
    "platformVersion": "11"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)



''' try:

        # Start the test.
        eyes.open(driver= driver, app_name='7Mind Meditation reinvented_v2.50.0_apkpure.com', test_name='Selenium Eyes Test')

        # Visual UI testing.
        eyes.check_window('Library')

        # End the test.
        eyes.close()

    finally:

        # Close the app.
        driver.quit()

        # If the test was aborted before eyes.close was called, ends the test as aborted.
        eyes.abort_if_not_closed()'''