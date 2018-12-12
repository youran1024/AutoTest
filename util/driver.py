#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from appium import webdriver

server_base = "http://127.0.0.1:"
server_end = "/wd/hub"

capabilities = {
    "platformName": "iOS",
    "automationName": "XCUITest",
    "platformVersion": "11.0",
    "app": "/Users/hunter/Desktop/python/PythonAppium2/app/iOSFinancial.app",
    "deviceName": "iPhone 8",
    "noReset":"true"    
}

capabilities_real = {
    "udid": "5d00e43272746fd85c456ddcbe52593b64d7f132",
    "app": "/Users/hunter/Desktop/iOSFinancial-r.app",
    "platformName": "iOS",
    "deviceName": "iPhone",
    "automationName": "XCUITest",
    "platformVersion": "11.4"
}

class Driver():

    def start_driver(self, port):

        server = server_base + str(port) + server_end
        try:
            print(server, capabilities_real)
            driver = webdriver.Remote(server, capabilities_real)
            return driver
        except Exception as e:
            print('driver start error:', e)

        return None

if __name__ == '__main__':
    
    driver = Driver()
    driver.start_driver(4723)


