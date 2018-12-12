#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/hunter/Desktop/python/PythonAppium2/")

from util.driver import Driver
from util.server import Server
from util.element_finder import ElementFinder

class MainTest():

    def start_test(self):
        server = Server()
        port = server.start_server()

        driver = Driver()
        driver.start_driver(port)

        # finder = ElementFinder(driver)

        # finder.find_element().by_id('sdfsdf')
        


if __name__ == '__main__':

    test = MainTest()
    test.start_test()
