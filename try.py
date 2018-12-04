import os,time
import unittest
from appium import webdriver
from selenium import webdriver
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'ANT',
            'newCommandTimeout': 240,
            "appPackage": "com.google.android.calculator",
            "appActivity": 'com.android.calculator2.Calculator'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test(self):
        print('test')
        time.sleep(5)

        driver.find_element_by_id("com.google.android.calculator:id/digit1").click()

    def tearDown(self):
        self.driver.quit()


