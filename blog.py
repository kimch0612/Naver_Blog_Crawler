from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, urllib.request

mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("c:/chromedriver.exe", options=chrome_options)
url = input("긁어올 카테고리의 첫번째 글 링크를 입력하세요: ")
driver.implicitly_wait(7)
driver.get(url)
i = 5
ii = 0
title_before = ""
fin = 0
name = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[4]/div[1]/div/div[1]/div/div/div[2]').text

def crawling():
    global i, ii, title_before, fin, name
    title = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[4]/div[1]/div/div[1]/div/div/div[2]')
    post = driver.find_element_by_xpath('//*[@id="viewTypeSelector"]/div/div[2]')
    if title_before != title.text:
        with open(name + ".txt", "a", encoding="utf8") as f:
            f.write("///" + title.text + "///" + "\n\n" + post.text + '\n\n\n')
        i -= 1
        title_before = title.text
    else:
        if ii != 3:
            ii += 1
            pass
        else:
            try:
                driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[4]/div[6]/div/div[1]/div/div/div/div[1]').click()
            except:
                driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[4]/div[6]/div/div[1]/div/div[2]/div/div[1]').click()
            time.sleep(2)
            title = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[4]/div[1]/div/div[1]/div/div/div[2]')
            post = driver.find_element_by_xpath('//*[@id="viewTypeSelector"]/div/div[2]')
            with open(name + ".txt", "a", encoding="utf8") as f:
                f.write("///" + title.text + "///" + "\n\n" + post.text + '\n\n\n')
            fin = 1

def nextpost():
    global i
    if i > 2:
        driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[4]/div[6]/div/div[1]/div/div/div/div[%s]'%i).click()
    else:
        try:
            driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[4]/div[6]/div/div[1]/div/div/div/div[2]').click()
        except:
            driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[4]/div[6]/div/div[1]/div/div[2]/div/div[2]').click()

while True:
    if fin != 1:
        time.sleep(2)
        crawling()
        nextpost()
    else:
        driver.quit()
        break

print("완료")