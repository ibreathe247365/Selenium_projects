# specs: RangeScraper.py min_range max_range pages

import sys
if len(sys.argv) == 4:
    min_range = sys.argv[1]
    max_range = sys.argv[2]
    pages = sys.argv[3]

else:
    print('Please adhere to the specs.')
    exit(4)

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
Prob_links = []
for index in range(1, int(pages)+1):
    driver.get("https://codeforces.com/problemset/page/" +
               str(index)+"?tags="+min_range+"-"+max_range)
    # Prob_anchors = driver.find_elements_by_partial_link_text(
    # "/problemset/problem/")
    PartialLinkHref = "/problemset/problem/"
    Prob_anchors = driver.find_elements_by_xpath(
        "//a[contains(@href,'" + PartialLinkHref + "')]")
    # print(Prob_anchors)
    Prob_anchors = set(Prob_anchors)  # Removing Duplicates
    for anchor in Prob_anchors:
        Prob_links.append(anchor.get_attribute("href"))
print(Prob_links)

Path("./"+min_range+"-"+max_range).mkdir(parents=True, exist_ok=True)

for link in Prob_links:
    driver.get(link)
    Path("./"+min_range+"-"+max_range+"/" +
         driver.title).mkdir(parents=True, exist_ok=True)
    ex_input = driver.find_elements_by_css_selector(".input pre")
    i = 0
    for input in ex_input:
        # print(input.text)
        i = i+1
        try:
            with open("./"+min_range+"-"+max_range+"/"+driver.title+"/input"+str(i)+'.txt', 'x') as file:
                file.write(input.text)
        except:
            continue
    ex_output = driver.find_elements_by_css_selector(".output pre")
    i = 0
    for output in ex_output:
        # print(input.text)
        i = i+1
        try:
            with open("./"+min_range+"-"+max_range+"/"+driver.title+"/output"+str(i)+'.txt', 'x') as file:
                file.write(output.text)
        except:
            continue
    # driver.save_screenshot("./"+contest_no+"/"+driver.title +
    #                        "/"+driver.title+'Question.png')

    def S(X): return driver.execute_script(
        'return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'), S('Height'))
    driver.find_element_by_tag_name('body').screenshot("./"+min_range+"-"+max_range+"/"+driver.title +
                                                       "/"+driver.title+'Question.png')

# driver.quit()
