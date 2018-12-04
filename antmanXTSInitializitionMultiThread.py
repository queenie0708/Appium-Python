from appium import webdriver
import threading
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
import os

# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '9'
# desired_caps['deviceName'] = 'ANT'
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = '.Settings'


def initialize(driver):
    driver.find_element_by_android_uiautomator('text(\"Display")').click()
    driver.implicitly_wait(5)
    driver.find_element_by_android_uiautomator('text(\"Advanced")').click()
    driver.implicitly_wait(5)
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

def multitask(n=2):
    i = 1
    while i <= n:
      desired_caps = []
      caps = {
       'platformName' : 'Android',
       'platformVersion' : '9',
       'deviceName' : 'ANT' + str(i),
       'appPackage' : 'com.android.settings',
       'appActivity' : '.Settings'
       }
      desired_caps.append(caps)
      def task(i):
        driver = webdriver.Remote('http://localhost:4723+int(i)*2/wd/hub', desired_caps[i-1])
        print(driver.contexts)
            ##休眠20s等待页面加载完成
        initialize(driver)
        driver.quit()

        threads = []
        task = threading.Thread(target=task(i))
        threads.append(task)


def start_appium(port=4723):
    a = os.popen('netstat -ano | findstr "%s" '% port)
    sleep(2)
    t1 = a.read()
    if "LISTENING" in t1:
        print("appium服务已经启动：%s" % t1)
        # s = t1.split(" ")
        # s1 = [i for i in s if i != '']
        # pip = s1[-1].replace("\n", "")
    else:
        # 启动appium服务
        # appium -a 127.0.0.1 -p 4740 -U emulator-5554 127.0.0.1:62001 --no-reset
        os.system("appium -p %s " % (port))
        print("appium服务已经启动：%s" % (port))

if __name__ == '__main__':
  devices = int(input('how many devices ? '))
  # i = 1
  # while i <= devices:
  #   start_appium(4723 + i*2)
  # sleep(60)
  print('time to wake up')
  multitask(devices)
  print('go to threads')
  for t in threads:
    t.start()
