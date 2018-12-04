from appium import webdriver
import threading
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'ANT'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_android_uiautomator('text(\"Display")').click()
driver.implicitly_wait(5)
#driver.find_element_by_android_uiautomator('text(\"Advanced")').click()
#driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"Sleep")').click()
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"30 minutes")').click()
driver.implicitly_wait(5)
driver.find_element_by_class_name('android.widget.ImageButton').click() #back
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"Security & location")').click()
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"Screen lock")').click()
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"None")').click()
driver.implicitly_wait(5)
driver.find_element_by_class_name('android.widget.ImageButton').click() #back
driver.implicitly_wait(5)
# need scroll down but don't know how so use search instead,enter from search there is no advanced
driver.find_element_by_class_name('android.widget.ImageButton').click()
driver.find_element_by_class_name('android.widget.EditText').send_keys('sys') #back
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"System")').click()
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"Date & time")').click()
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"Use 24-hour format")').click()
driver.implicitly_wait(5)
driver.find_element_by_class_name('android.widget.ImageButton').click() #back
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"Backup")').click()
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"Back up to Google Drive")').click()
driver.implicitly_wait(5)
driver.find_element_by_class_name('android.widget.ImageButton').click() #back
driver.implicitly_wait(5)
#driver.find_element_by_android_uiautomator('text(\"Advanced")').click()
#driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"Developer options")').click()
driver.implicitly_wait(5)
driver.find_element_by_android_uiautomator('text(\"Stay awake")').click()
driver.implicitly_wait(5)
#oh we need to scroll and this time there is no work around
def swipeDown(driver, n):
    '''向下滑动屏幕'''
    for i in range(n):
        driver.swipe(300, 800, 300, 100)
swipeDown(driver,2)

driver.find_element_by_android_uiautomator('text(\"Verify apps over USB")').click()
driver.implicitly_wait(5)
driver.find_element_by_class_name('android.widget.ImageButton').click() #back
driver.implicitly_wait(5)

driver.quit()
