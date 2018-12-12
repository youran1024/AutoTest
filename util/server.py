#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from appium import webdriver
import os
import datetime

# appium -p 4100

base_cmd = 'appium -p '
other_set = ' --no-reset --session-override'
log_cmd = ' --log ./log/'
server_port = 4100

class Server():
    
    def start_server(self):
        
        time_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        log_name = time_now + '.log'
        log_set = log_cmd + log_name
        server_cmd = base_cmd + str(server_port) + other_set + log_set
        try:
            os.system(server_cmd)
        except Exception as e:
            print('server start error:', e)

        return server_port


if __name__ == '__main__':
    server = Server()
    server.start_server()
