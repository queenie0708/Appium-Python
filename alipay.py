from appium import webdriver
import threading
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'PDP'
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['appActivity'] = '.AlipayLogin'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

sleep(40)
print('time to wake up')
driver.find_element_by_android_uiautomator('text(\"Ant Forest")').click()
driver.implicitly_wait(5)
sleep(8)
def swipeDown(driver, n):
    '''向下滑动屏幕'''
    for i in range(n):
        driver.swipe(300, 1000, 300, 100)
swipeDown(driver,7)
sleep(5)
print('is more friend there?')
driver.find_element_by_android_uiautomator('text(\"View more friends")').click()
driver.implicitly_wait(5)

friends = driver.find_element_by_class('android.view.View')
for friend in friend:
    friend.click()
    sleep(5)

    driver.find_element_by_android_uiautomator('text(\"")').click()

    
driver.quit()
