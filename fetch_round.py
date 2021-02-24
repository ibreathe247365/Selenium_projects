import sys
if len(sys.argv) == 2:
    contest_no = sys.argv[1]
else:
    print('Please adhere to the specs.')
    exit(2)

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

Path("./"+contest_no).mkdir(parents=True, exist_ok=True)

driver.get("https://codeforces.com/problemset")
# search_init = driver.find_element_by_xpath(
#     "/html/body/div[6]/div[4]/div[2]/div[2]/div[5]/div/img")
# search_init.click()
# time.sleep(10)
# search_problem = driver.find_element_by_xpath(
#     "/html/body/div[6]/div[4]/div[2]/div[2]/div[5]/div/span[2]/input")
# search_problem.send_keys(contest_no)
search_init = driver.find_element_by_class_name("closed")
search_init.click()
search_problem = driver.find_element_by_css_selector(".filter input")
search_problem.send_keys(contest_no)
Prob_anchors = driver.find_elements_by_partial_link_text(contest_no)
Prob_links = []
for anchor in Prob_anchors:
    Prob_links.append(anchor.get_attribute("href"))
# driver.manage().window().maximize()
# driver.save_screenshot("image1.png")
print(Prob_links)
for link in Prob_links:
    driver.get(link)
    Path("./"+contest_no+"/"+driver.title).mkdir(parents=True, exist_ok=True)
    # time.sleep(5)
    # driver.save_screenshot('.\{contest_no}\{driver.title}.png')
    # driver.save_screenshot('.\\'+contest_no+'\\'+driver.title+'.png')
    # driver.save_screenshot('.//'+contest_no+'//'+driver.title+'.png')
    # driver.save_screenshot('./{contest_no}/{driver.title}.png')
    # driver.save_screenshot("image"+driver.title+'.png')
    ex_input = driver.find_elements_by_css_selector(".input pre")
    i = 0
    for input in ex_input:
        # print(input.text)
        i = i+1
        with open("./"+contest_no+"/"+driver.title+"/input"+str(i)+'.txt', 'x') as file:
            file.write(input.text)
    ex_output = driver.find_elements_by_css_selector(".output pre")
    i = 0
    for output in ex_output:
        # print(input.text)
        i = i+1
        with open("./"+contest_no+"/"+driver.title+"/output"+str(i)+'.txt', 'x') as file:
            file.write(output.text)
    # driver.save_screenshot("./"+contest_no+"/"+driver.title +
    #                        "/"+driver.title+'Question.png')

    def S(X): return driver.execute_script(
        'return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'), S('Height'))
    driver.find_element_by_tag_name('body').screenshot("./"+contest_no+"/"+driver.title +
                                                       "/"+driver.title+'Question.png')

driver.quit()
