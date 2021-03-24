# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


# запускаем приложение
driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
       "app": r"C:/Users/Aleksandr/Google Диск/MTT/Distrib/MicroSIP-3.20.3/microsip.exe"
    })

driver.find_element_by_id('1078').click()
# driver.find_element_by_id('1078').send_keys(Keys.CONTROL, 'a')
# driver.find_element_by_id('1078').send_keys(Keys.BACKSPACE)
driver.find_element_by_id('1078').send_keys('+79153414301')
driver.find_element_by_id('1022').click()


# "C:/windows/system32/calc.exe"
# "C:/Users/Aleksandr/Google Диск/MTT/Distrib/MicroSIP-3.20.3/microsip.exe"
# "C:/Program Files (x86)/PhonerLite/PhonerLite.exe"

time.sleep(10)

driver.close()

"""
# coding: utf-8
from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'false',
        "app": r"C:/windows/system32/calc.exe"
    })

window = driver.find_element_by_class_name('CalcFrame')
view_menu_item = window.find_element_by_id('MenuBar').find_element_by_name('View')

view_menu_item.click()
view_menu_item.find_element_by_name('History').click()
window.find_element_by_id('121').click()

driver.close()
"""