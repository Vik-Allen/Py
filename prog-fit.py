from appium import webdriver
import time

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '13',
    'deviceName': 'OnePlus 8 Pro',
    'appPackage': 'ru.handh.sportlife',
    'appActivity': 'p389ru.handh.sportlife.p450ui.splash.SplashActivity',
    'noReset': True
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

