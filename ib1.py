from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

chromedriver_path =r'C:\Users\Aditya Voleti\MISC\Downloads\chromedriver_win32\chromedriver.exe' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options = chrome_options)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('aditya_voleti')
password = webdriver.find_element_by_name('password')
password.send_keys('avddd1911sbs')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

