from selenium import webdriver
import time 
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='chromedriver.exe')
#tools
def click_by_position(driver, x, y) -> None:
    actions = ActionChains(driver)

    # MOVE TO TOP_LEFT (`move_to_element` will guide you to the CENTER of the element)
    whole_page = driver.find_element_by_id("map")
    actions.move_to_element_with_offset(whole_page, 0, 0)

    # MOVE TO DESIRED POSITION THEN CLICK
    actions.move_by_offset(x, y)
    actions.click()

    actions.perform()
    print(whole_page.location)

#body
lat = 34.999418
lon= 134.990197
url =f'https://soil-inventory.rad.naro.go.jp/figure.html?lat={lat}&lng={lon}&zoom=15'

driver.get(url)
time.sleep(2)

driver.execute_script("window.scrollTo(0, 200)")

x = 5
y = 85
click_by_position(driver, x, y)
#driver.execute_script("window.scrollTo(0, (document.getElementById('map').scrolltop))")

time.sleep(2)
popname = driver.find_element_by_id('popName')
popExplain = driver.find_element_by_id('popExplain')
print(popname.text)
print(popExplain.text)

#driver.execute_script('windows.scrollTO(0,200);')
# ある要素までスクロールする
#element = driver.find_element_by_id("map")
#element = driver.find_element_by_id("map")
#actions = ActionChains(driver)
#actions.move_to_element(element)
#actions.perform()

#print(whole_page.location)
#print(driver.get_window_size())
#print(element.is_enabled())

#actions.move_to_element(element)
#actions.perform()


#click_by_position(borwer, x, y)


#a = browzer.find_element_by_id("map").click()
#time.sleep(3)

#pyautogui.click(200,600)
#browzer.quit()




#actions = ActionChains(borwer)

    # MOVE TO TOP_LEFT (`move_to_element` will guide you to the CENTER of the element)
#whole_page = driver.find_element_by_id("buttonLeftBox")
#whole_page = driver.find_element(by=By.ID, value='map')
#whole_page = driver.find_element(map")
#actions.move_to_element_with_offset(whole_page, 0, 0)
#actions.move_to_element(whole_page)
#actions.perform()