import logging


import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilities.ReadProperites import Driver_Comman


@pytest.fixture
def catch1(browser):
    if browser=="chrome":
        driver=webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
        driver.get(Driver_Comman.URL())
        return driver




    #elif browser=="firefox":
        #driver = webdriver.Firefox(executable_path="D:/Akshay/num_file/driver/geckodriver.exe")



# This will get the value from CLI - command line input
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return the the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

####################### PYtest HTML Report ###################

# IT is hook for adding Environment info to HTML Report #
'''def pytest_configure(config):
    config._metadata['Project_Name'] = 'nop Commerce'
    config._metadata['Module_Name'] = "Customers"
    config._metadata ['Tester'] = 'Akshay'
'''
#It is hook for Delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)








