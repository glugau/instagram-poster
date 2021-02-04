from selenium import webdriver
import time
from instagram import login
from selenium.webdriver.common.keys import Keys


def post(driver, caption, paths, postDay="now", postHour = "now", postMinute = "0"):
    driver.get("https://business.facebook.com/creatorstudio/")
    time.sleep(3)  # click the top left dropdown menu
    driver.find_element_by_class_name("g1fckbup").click()
    time.sleep(0.5)  # select new post
    driver.find_element_by_xpath("//div[contains(@class, 'g1fckbup') and contains(@class, 'ct5fwkgv') and contains(@class, 'mr4k7n6j') and contains(@class, 'sdgvddc7') and contains(@role, 'menuitem')]").click()
    time.sleep(3)  # input the caption in the field
    driver.find_element_by_xpath(
        "//div[contains(@class, 'notranslate') and contains(@class, '_5rpu') and contains(@role, 'combobox')]").send_keys(caption)
    time.sleep(1)
    first = True
    for path in paths:
        if first:
            first = False
            # click the blue button to add an image
            driver.find_element_by_xpath("//div[starts-with(@id, 'js_') and starts-with(@aria-controls, 'js_') and contains(@aria-haspopup, 'true')]").click()
            time.sleep(0.1)
            # give the image to the field
            driver.find_element_by_xpath("//input[contains(@accept, 'video/*, image/*')]").send_keys(path)
        else:
            # click the blue button which has moved positions to add an image
            driver.find_element_by_xpath("//div[starts-with(@id, 'js_') and starts-with(@aria-controls, 'js_') and contains(@aria-haspopup, 'true')]").click()
            driver.find_element_by_xpath("//input[contains(@accept, 'video/*, image/*')]").send_keys(path)
    time.sleep(2)
    if postDay == "now" and postHour == "now":
        # posts
        driver.find_element_by_xpath(
            "//button[contains(@class, '_271k') and contains(@class, '_271m') and contains(@class, '_1qjd')]").click()
    else:
        # click the blue arrow
        driver.find_element_by_id("js_48").click()
        time.sleep(0.1)
        # click the button to post at a specified time
        driver.find_element_by_xpath(
            "//div[contains(@class, '_811a') and contains(@class, '_811b') and contains(@class, '_811c') and contains(@class, '_3qn7') and contains(@class, '_61-0') and contains(@class, '_2fyh') and contains(@class, '_3qnf')]").click()
        time.sleep(0.1)
        if postDay != "now":
            #  input the postDay var
            date_field = driver.find_element_by_xpath("//input[contains(@class, '_58al') and contains(@type, 'text') and contains(@dir, 'ltr')]")
            date_field.send_keys(Keys.CONTROL, "a")
            time.sleep(0.1)
            date_field.send_keys(postDay)
            time.sleep(0.1)
            date_field.send_keys(Keys.ENTER)
        if postHour != "now":
            driver.find_elements_by_xpath("//input[contains(@role, 'spinbutton')]")[1].send_keys(postMinute)
            driver.find_elements_by_xpath("//input[contains(@role, 'spinbutton')]")[0].send_keys(postHour)
        time.sleep(0.2)
        # posts
        driver.find_element_by_xpath("//button[contains(@class, '_271k') and contains(@class, '_271m') and contains(@class, '_1qjd')]").click()
    time.sleep(5)

