# specs: ContestScraper.py 40 ./demoFolder
import sys
if len(sys.argv) == 3:
    contest_no = sys.argv[1]
    save_location = sys.argv[2]

else:
    print('Please adhere to the specs.')
    exit(3)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
options = webdriver.ChromeOptions()
options.headless = True

PATH = ".\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(PATH, options=options)

Path(save_location).mkdir(parents=True, exist_ok=True)

driver.get("https://codeforces.com/contests")

contest_links_element = driver.find_elements_by_xpath(
    "//*[contains(text(), 'Enter »')]")
a = 1
while(True):
    if(int(contest_no) > len(contest_links_element)):
        a = a+1
        driver.get("https://codeforces.com/contests/page/"+str(a))
        fetchMoreLinks = driver.find_elements_by_xpath(
            "//*[contains(text(), 'Enter »')]")
        contest_links_element.extend(fetchMoreLinks)
        continue
    else:

        Contest_links = []
        for anchor_index in range(0, int(contest_no)):
            Contest_links.append(
                contest_links_element[anchor_index].get_attribute("href"))
        print(Contest_links)
        contest_name_array = []
        for element in Contest_links:
            # Only for Python 3.9 or newer
            contest_name_array.append(element.removeprefix(
                'https://codeforces.com/contest/'))
        for contest_name in contest_name_array:
            driver.get("https://codeforces.com/problemset")
            search_init = driver.find_element_by_class_name("closed")
            search_init.click()
            search_problem = driver.find_element_by_css_selector(
                ".filter input")
            search_problem.send_keys(contest_name)
            Prob_anchors = driver.find_elements_by_partial_link_text(
                contest_name)
            Prob_links = []
            for anchor in Prob_anchors:
                Prob_links.append(anchor.get_attribute("href"))
            print(Prob_links)
            for link in Prob_links:
                driver.get(link)
                Path(save_location+"/"+contest_name+"/" +
                     driver.title).mkdir(parents=True, exist_ok=True)
                ex_input = driver.find_elements_by_css_selector(".input pre")
                i = 0
                for input in ex_input:
                    i = i+1
                    with open(save_location+"/"+contest_name+"/"+driver.title+"/input"+str(i)+'.txt', 'x') as file:
                        file.write(input.text)
                ex_output = driver.find_elements_by_css_selector(".output pre")
                i = 0
                for output in ex_output:
                    i = i+1
                    with open(save_location+"/"+contest_name+"/"+driver.title+"/output"+str(i)+'.txt', 'x') as file:
                        file.write(output.text)

                def S(X): return driver.execute_script(
                    'return document.body.parentNode.scroll'+X)
                driver.set_window_size(S('Width'), S('Height'))
                driver.find_element_by_tag_name('body').screenshot(
                    save_location+"/"+contest_name+"/"+driver.title + "/"+driver.title+'Question.png')
        break
driver.quit()
