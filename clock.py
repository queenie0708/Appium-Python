import os,time
import unittest
from appium import webdriver

class Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'ANT',
            'newCommandTimeout': 240,
            'appPackage': 'com.google.android.deskclock',
            'appActivity': 'com.android.deskclock.DeskClock'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test(self):
        def deleteAlarm(driver):
            arrows = self.driver.find_elements_by_accessibility_id('Expand alarm')
            amount = len(arrows)
            print(amount)
            i = 0
            while i < amount:
              driver.find_element_by_accessibility_id('Expand alarm').click()
              time.sleep(2)
              driver.find_element_by_android_uiautomator('text(\"Delete")').click()
              driver.implicitly_wait(5)
              print( str(i) +' deleted')
              i = i +1
              time.sleep(5)
        print('test start')
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('text(\"ALARM")').click()
        self.driver.implicitly_wait(5)
        print('switch to ALAM')
        deleteAlarm(self.driver)
        print('now wake up')
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        systemTime = self.driver.device_time
        print(systemTime)
        time.sleep(5)
        print('add alarm')
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        self.driver.implicitly_wait(5)
        print('switch to text input mode')
        minute = self.driver.find_element_by_id('android:id/input_minute')
        print (minute.text)
        print (int(minute.text)+2)
        setMinute = int(minute.text)+2
        print (setMinute)
        minute.clear()
        minute.send_keys(str(setMinute))
        time.sleep(5)
        print ('now minute' + str(setMinute))
        self.driver.find_element_by_android_uiautomator('text(\"OK")').click()
        print ('alarm added')
        time.sleep(40)
        self.driver.lock()
        print('screen locked')
        self.driver.find_element_by_id("com.google.android.deskclock:id/dismiss").click()
        driver.implicitly_wait(5000)
        # while tryTime < maxTry:
        #   if dismiss == true:
        #      dissmiss.click()
        #      print ('dismissed')
        #      break
        #   else:
        #      print( tryTime + 'waiting for alarm ring')



    def tearDown(self):
        self.driver.quit()
        print('Done ')


if __name__ == '__main__':
    unittest.main()
