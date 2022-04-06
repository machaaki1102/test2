from selenium import webdriver
import time 
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

borwer = webdriver.Chrome(executable_path='chromedriver.exe')
#tools
def click_by_position(driver, x, y) -> None:
    actions = ActionChains(driver)

    # MOVE TO TOP_LEFT (`move_to_element` will guide you to the CENTER of the element)
    whole_page = driver.find_element_by_tag_name("html")
    #actions.move_to_element_with_offset(whole_page, 0, 0)

    actions.move_to_element(whole_page)
    # MOVE TO DESIRED POSITION THEN CLICK
    actions.move_by_offset(x, y)
    actions.click()

    actions.perform()

#body
lat = 34.999418
lon= 134.990197
url =f'https://soil-inventory.rad.naro.go.jp/figure.html?lat={lat}&lng={lon}&zoom=15'
#url2 = 'https://soil-inventory.rad.naro.go.jp/figure.html?lat=34.999418&lng=134.990197&zoom=15'
borwer.get(url)
time.sleep(3)

x = 100
y = 100
#click_by_position(borwer, x, y)

click_by_position(borwer, x, y)
#a = browzer.find_element_by_id("map").click()
#time.sleep(3)

#pyautogui.click(200,600)
#print(a.is_enabled())
#browzer.quit()




#actions = ActionChains(borwer)

    # MOVE TO TOP_LEFT (`move_to_element` will guide you to the CENTER of the element)
whole_page = driver.find_element_by_id("buttonLeftBox")
#whole_page = driver.find_element(by=By.ID, value='map')
#whole_page = driver.find_element(map")
#actions.move_to_element_with_offset(whole_page, 0, 0)
actions.move_to_element(whole_page)
actions.perform()