from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox(executable_path='geckodriver.exe')


def get_example(word):
    query = 'https://translate.google.com/?sl=es&tl=en&text={}&op=translate'
    browser.get(query.format(word))
    try:
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "AZPoqf")))
    except:
        return []
    time.sleep(0.1)
    try:
        for element in browser.find_elements_by_class_name("Dwvecf"):
            if element.text.startswith('Examples'):
                expand = element.find_element(By.XPATH, "following-sibling::*")
                time.sleep(0.4)
                expand.find_element_by_class_name('VK4HE').click()
                break
    except:
        pass
    m = list(map(lambda x: x.text, browser.find_elements_by_class_name("AZPoqf")))
    r = []
    for oracion in m:
        browser.get(query.format(oracion))
        time.sleep(0.5)
        translation = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "J0lOec")))
        r.append((oracion, translation.text.strip()))
    return r
