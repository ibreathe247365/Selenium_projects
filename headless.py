import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

options = webdriver.ChromeOptions()
options.headless = True
PATH = ".\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)

driver.get("https://codeforces.com/problemset")


def S(X): return driver.execute_script(
    'return document.body.parentNode.scroll'+X)


driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('demo.png')
