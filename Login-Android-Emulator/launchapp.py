from appium import webdriver
import pytest

class Launch:

    desired_cap = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "app": "/Users/openmindschooling/MyStuff/Mobile_App_Testing/Android/Apps/7Mind Meditation reinvented_v2.50.0_apkpure.com.apk",
    "platformVersion": "11"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
