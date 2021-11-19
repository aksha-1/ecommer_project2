import time

import selenium
from selenium.webdriver.common.by import By

from Utilities.ReadProperites import Read_Cofig, login_locator


class Action_Class:
    Start_URL="https://www.nopcommerce.com/en/demo"
    # Login page #
    admin_button_click_classname=login_locator.admin_click_button()
    login_surname_id =login_locator.surname_button()
    input_button_pass_enter_ID =login_locator.pas_button()
    click_login_button_xpath=login_locator.click_tologin_button()
    click_logout_button_xpath =login_locator.logout_button()
    def __init__(self,driver):
        self.driver=driver
    def click_to_go_login(self):
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,self.admin_button_click_classname).click()
    def input_surname(self,surname):
        self.driver.find_element(By.ID,self.login_surname_id).clear()
        time.sleep(2)

        self.driver.find_element(By.ID,self.login_surname_id).send_keys(surname)
    def input_password(self,password):
        self.driver.find_element(By.ID,self.input_button_pass_enter_ID).clear()
        time.sleep(2)
        self.driver.find_element(By.ID,self.input_button_pass_enter_ID).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.click_login_button_xpath).click()

    def click_on_logout_button(self):
        self.driver.find_element(By.XPATH,self.click_logout_button_xpath).click()



