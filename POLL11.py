from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

for x in range (0,20):
    # SET UP
    PATH = "C:\webdrivers\chromedriver.exe"
    s = Service('\webdrivers\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    linkadres = "https://pollev.com/lula"
    driver.get(linkadres)

    time.sleep(1)

    # DISMISS: ACCEPTING THE POLICY OF POLLEV
    driver.find_element(by=By.XPATH, value="/html/body/aside/div[2]/div[2]/pe-button[1]/button/span").click()
    time.sleep(1)

    #driver.find_element(by=By.XPATH, value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/advisory-message/div/div/button[2]").click()
    #time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/advisory-message/div/div/button[2]").click()
    time.sleep(1)

    # SKIP BUTTON
    driver.find_element(by=By.XPATH,value="//html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-screen-name/div[2]/div[2]/pe-button[2]/button/span").click()

    time.sleep(1)

    # START QUIZ AND CHOOSING RESPONSE 1
    # driver.find_element(by=By.XPATH,value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-activity/div/div/div/button").click()
    driver.find_element(by=By.XPATH,value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-activity/div/div/div[2]/div[2]/div/div[1]/button[1]/div[2]").click()
    #time.sleep(1)

    # # FINISHING THE QUIZ
    # driver.find_element(by=By.XPATH,value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-activity/div/div/div/div[2]/nav/button[2]").click()
    # time.sleep(1)
    # driver.find_element(by=By.XPATH,value="/html/body/pe-application/notification-manager/pe-notification/aside/div[2]/div[2]/pe-button/button/span").click()
    # time.sleep(1)
    # driver.find_element(by=By.XPATH,value="/html/body/pe-application/div/div/pec-response-live/layout-plain/section/div/main/div/pec-response-activity/div/div/div/div[2]/nav/button[2]").click()


    # FORMAT FOR FINDING ELEMENT
    # driver.find_element(by=By.XPATH,value="").click()

    print(driver.title,'ANS', x,"POLL6")
    time.sleep(0.1)
    driver.quit()
