
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'ANT'
desired_caps['appPackage'] = 'com.google.android.calculator'
desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(50)
driver.find_element_by_name('0').click()
driver.find_element_by_android_uiautomator('text(\"3")').click()
driver.implicitly_wait(30)

driver.quit()
