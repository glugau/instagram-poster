from time import sleep
from selenium import webdriver

def login(user_username, user_pwd, driver):
    driver.get("https://business.facebook.com/creatorstudio/")
    sleep(5)
    driver.find_elements_by_xpath("//button[@data-cookiebanner='accept_button']")[1].click()
    sleep(1)
    driver.find_elements_by_xpath("//button[@data-cookiebanner='accept_button']")[0].click()
    sleep(1)
    driver.find_element_by_id("media_manager_chrome_bar_instagram_icon").click()
    sleep(1)
    window_before = driver.window_handles[0]
    driver.find_element_by_class_name("g1fckbup").click()
    sleep(3)
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    driver.find_element_by_class_name("bIiDR").click()
    sleep(1)
    driver.find_element_by_name("username").send_keys(user_username)
    sleep(0.1)
    driver.find_element_by_name("password").send_keys(user_pwd)
    sleep(0.1)
    driver.find_element_by_class_name("L3NKy").click()
    sleep(3)
    driver.find_element_by_class_name("yWX7d").click()
    sleep(3)
    driver.close()
    driver.switch_to_window(window_before)
    sleep(1)