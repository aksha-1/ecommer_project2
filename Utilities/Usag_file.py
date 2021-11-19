import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class usag_file:

    def get_logger(self):
        logs = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('C:/Users/SSERIES/PycharmProjects/ecommer_project2/Logfiles/sanity.log')
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(lineno)d :%(name)s :%(message)s")
        logs.setLevel(logging.DEBUG)
        fileHandler.setFormatter(format)
        logs.addHandler(fileHandler)
        return logs

    def explict_wait(self,driver1,value):
        self.driver1=driver1
        wait = WebDriverWait(self.driver1,60)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,value)))

    #-8600008341