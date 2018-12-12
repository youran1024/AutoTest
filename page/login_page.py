#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/hunter/Desktop/python/PythonAppium2/")

from util.element_finder import ElementFinder
from util.ini_handle import IniHandle

class LoginPage():

    def __init__(self, driver):
        self.element_finder = ElementFinder(driver)

    def name_field(self):
        return self.element_finder.find_element('sdf','name')

