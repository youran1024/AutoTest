#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from appium import webdriver
from ini_handle import IniHandle

ini_path = './config/element_config.ini'

class ElementFinder():

    def __init__(self, _driver):
        if _driver:
            self.driver = _driver
            self.ini_hanle = IniHandle(ini_path)
        else:
            raise ValueError
            

    def find_element(self, module, name):
        value = self.ini_hanle.get_value(module, name)

        values = value.split('?')
        find_type = values[0]
        find_value = values[1]

        method = None
        if find_type == 'id':
            method = self.driver.find_element_by_id
        elif find_type == 'name':
            method = self.driver.find_element_by_name
        elif find_type == 'type':
            method = self.driver.find_element_by_type
        else:
            method = self.driver.find_element_by_xpath
        
        element = method(find_value)

        return element


from driver import Driver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    base_driver =  Driver().start_driver(4723)

    finder = ElementFinder(base_driver)
    time.sleep(5)
    login_button = finder.find_element('index_module', 'login_button')
    login_button.click()
    time.sleep(5)

    element = finder.find_element('login_module', 'name_field')
    element.clear()
    element.send_keys('15652376134')

    pass_field = finder.find_element('login_module', 'pass_field')
    pass_field.clear()
    pass_field.send_keys('De')

    login_button = finder.find_element('login_module', 'login_button')
    login_button.click()

    

    # time.sleep(2)
    # tost_element = ("xpath","//*[contains(@text,"+"密码需要在6~16位之间"+")]")
    # element = WebDriverWait(base_driver,10,0.1).until(EC.presence_of_element_located(tost_element))
    # print('elemnet:', element)



