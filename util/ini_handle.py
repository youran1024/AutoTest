#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser

class IniHandle():

    def __init__(self, file_path):
        self.file_path = file_path
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(self.file_path)

    def get_value(self, module, name):
        return self.config_parser.get(module, name)

    
if __name__ == '__main__':

    handle = IniHandle('./config/element_config.ini')
    value = handle.get_value('login_module', 'name_field')
    print(value)
    
