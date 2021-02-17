from behave import given,when,then
from selenium import webdriver
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from Common import Locators
@given(u'the url e.ggtimer.com is open')
def open_browser(context):
    context.driver = webdriver.Chrome(executable_path="Drivers\\chromedriver.exe")
    context.driver.get("https://e.ggtimer.com/")
@when(u'I set the timer to 25 and click on start button')
def set_time_and_start(context):
    context.driver.find_element_by_id(Locators.Egg_timer_text_id).send_keys(25)
    context.driver.find_element_by_xpath(Locators.Egg_timer_start_xpath).click()


@then(u'Count down starts by decrementing by 1 second')
def verify_countdown(context):
    try:
        waitfor = WebDriverWait(context.driver, 8)
        waitfor.until(expected_conditions.presence_of_element_located((By.XPATH, Locators.Timer_xpath)))
        logging.info("Page loaded")
    except TimeoutException():
        logging.info("Timeout")
    count = 24
    while True:

        timer_ele = context.driver.find_element_by_xpath(Locators.Timer_xpath)
        val = timer_ele.get_attribute("innerText")
        lst = val.split(" ")
        try:
            assert count == int(lst[0]), "The value is not as expected.Expected: {}, Actual: {}".format(count, lst[0])
        except AssertionError as e:
            logging.error(e)
        time.sleep(1)
        if val == "0 second":
            break
        count = count - 1


@then(u'After the countdown ends a alert is displayed')
def verify_alert(context):
    try:
        a = WebDriverWait(context.driver, 2)
        a.until(expected_conditions.alert_is_present())
        context.driver.switch_to.alert.accept()
        logging.info("alert appeared")
    except TimeoutException():
        logging.error("alert did not appear")

    context.driver.close()

