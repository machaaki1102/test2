from selenium import webdriver
import time 
import os
from selenium.webdriver.common.by import By

browzer = webdriver.Chrome(executable_path='chromedriver.exe')


def click_by_position(driver, x, y) -> None:
    from selenium.webdriver.common.action_chains import ActionChains
    actions = ActionChains(driver)

    # MOVE TO TOP_LEFT (`move_to_element` will guide you to the CENTER of the element)
    whole_page = driver.find_element_by_tag_name("html")
    actions.move_to_element_with_offset(whole_page, 0, 0)

    # MOVE TO DESIRED POSITION THEN CLICK
    actions.move_by_offset(x, y)
    actions.click()

    actions.perform()


lat = 34.999418
lon= 134.990197
url =f'https://soil-inventory.rad.naro.go.jp/figure.html?lat={lat}&lng={lon}&zoom=12'
#url2 = 'https://soil-inventory.rad.naro.go.jp/figure.html?lat=34.999418&lng=134.990197&zoom=15'
browzer.get(url)
time.sleep(3)

x = 100
y = 100
click_by_position(browzer, x, y)

#a = browzer.find_element_by_id("map").click()
#time.sleep(3)

#pyautogui.click(200,600)
#print(a.is_enabled())
#browzer.quit()

