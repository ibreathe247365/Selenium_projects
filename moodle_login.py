from platform import machine
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
# captcha:first,second,add,subtract


def getCaptcha(sentence):
    words_array = sentence.split()
    num1, num2 = [int(s) for s in words_array if s.isdigit()]
    for word in words_array:
        if (word == 'first'):
            return num1
        elif (word == 'second'):
            return num2
        elif (word == 'add'):
            return num1+num2
        elif (word == 'subtract'):
            return num1-num2


if (__name__ == "__main__"):

    kerberos_id = input("Enter Kerberos ID:")
    password = input("Enter Password:")

    PATH = ".\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://moodle.iitd.ac.in/login/index.php")
    print(driver.title)

    username_field = driver.find_element_by_id("username")
    username_field.send_keys(kerberos_id)
    password_field = driver.find_element_by_id("password")
    password_field.send_keys(password)

    captcha_text = driver . find_element_by_id("login").text
    captcha_answer = getCaptcha(captcha_text)
    captcha_input_field = driver.find_element_by_id("valuepkg3")
    captcha_input_field.clear()
    captcha_input_field.send_keys(captcha_answer)

    login_button = driver.find_element_by_id("loginbtn")
    login_button.click()
