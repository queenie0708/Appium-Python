from time import sleep
import unittest
from appium import webdriver
class Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'ANT',
            'newCommandTimeout': 240,
            'appPackage': 'com.google.android.calculator',
            'appActivity': 'com.android.calculator2.Calculator'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test(self):
        Formula = '890+567-123*789/123'
        Result =  '668'
        sleep(5) #when launching the first time it have a advanced pad there
        print('test start')
        convertString = {
            '*' : '×',
            '-' : '−',
            '/' : '÷'
            }
        for F in Formula:
            if F in convertString: F = convertString[F]
            self.driver.find_element_by_android_uiautomator('text("'+str(F)+'")').click()
            print ( F + 'is clicked')
              
        self.driver.find_element_by_android_uiautomator('text(\"=")').click()
        print('now we should get result')
        sleep(5)
        whatWeGet = self.driver.find_element_by_id('com.google.android.calculator:id/result').text
        print ('result is ' + whatWeGet)
        self.assertEqual(whatWeGet,Result)
        sleep(5)
        
    def tearDown(self):
        self.driver.quit()
        print('Done ')


if __name__ == '__main__':
    unittest.main()
