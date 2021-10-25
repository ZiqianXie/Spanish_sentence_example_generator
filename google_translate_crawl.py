from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox(executable_path='geckodriver.exe')


def get_example(word):
    query = 'https://translate.google.com/?sl=es&tl=en&text={}&op=translate'
    browser.get(query.format(word))
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "VK4HE")))
    time.sleep(0.5)
    try:
        expand = browser.find_elements_by_class_name("VK4HE")[-1]
        expand.click()
    except:
        pass
    l = list(map(lambda x: x.text, browser.find_elements_by_class_name("AZPoqf")))
    r = []
    for oracion in l:
        browser.get(query.format(oracion))
        time.sleep(0.5)
        translation = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "J0lOec")))
        r.append((oracion, translation.text.strip()))
    return r
