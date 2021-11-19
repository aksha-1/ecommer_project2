import string

import pytest
from Page_Object.base_action  import Action_Class
from Page_Object.add_customer import Add_New_Customer
import random
import selenium

from Utilities.ReadProperites import Read_Cofig
from Utilities.Usag_file import usag_file
from Page_Object.Search_customer import Test_customer_search

class Test_AddCustomer_005:
    surname_input=Read_Cofig.user_name()
    password_input=Read_Cofig.password()

    @pytest.mark.regression
    def test_searchcustomer_005_TestCase(self,catch1):
        self.driver=catch1
        action=Action_Class(self.driver)
        log_file=usag_file()
        logs=log_file.get_logger()
        action.click_to_go_login()
        logs.info("*************test_searchcustomer_005_TestCase ********************")
        logs.info("*************open new windows with login page ********************")
        self.driver.switch_to.window(self.driver.window_handles[1])
        action.input_surname(self.surname_input)
        action.input_password(self.password_input)
        action.click_on_login_button()
        self.driver.maximize_window()
        logs.info("*************Login is successfully ********************")
        self.customer = Add_New_Customer(self.driver)
        self.customer.ClickOnCustomerMenu()
        self.customer.ClickOnCustomerSubMenu()
        logs.info("*************Customer Sub-menu Option done ********************")
        self.search=Test_customer_search(self.driver)
        self.search.SetFirstName("AKS")
        logs.info("************* Search my name options ********************")
        self.search.ClickOnButton()
        logs.info("************* search button pass ********************")
        #email_search=self.search.SerchCustomerByEmail("victoria_victoria@nopCommerce.com")
        #assert True==email_search
        #logs.info("*************Customer search by mail is successfully ********************")
       # else:
          #  logs.info("*************Customer search by mail is unsuccessfully ********************")
        self.driver.close()
        self.driver.quit()





