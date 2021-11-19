import string

import pytest
from Page_Object.base_action  import Action_Class
from Page_Object.add_customer import Add_New_Customer
import random
import selenium

from Utilities.ReadProperites import Read_Cofig
from Utilities.Usag_file import usag_file

class Test_AddCustomer:
    surname_input=Read_Cofig.user_name()
    password_input=Read_Cofig.password()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_customer_003_TestCase(self,catch1):
        self.driver=catch1
        action=Action_Class(self.driver)
        log_file=usag_file()
        logs=log_file.get_logger()
        action.click_to_go_login()
        self.driver.switch_to.window(self.driver.window_handles[1])
        action.input_surname(self.surname_input)
        action.input_password(self.password_input)
        action.click_on_login_button()
        self.driver.maximize_window()
        #self.driver
        logs.info("*************Login is successfully ********************")
        self.customer=Add_New_Customer(self.driver)
        self.customer.ClickOnCustomerMenu()
        self.customer.ClickOnCustomerSubMenu()
        self.customer.ClickOnAddNew()
        logs.info("*************Test_003_Add_Customer Test Cases ********************")
        self.email=random_generation()+'@gmail.com'
        self.customer.SetEmail(self.email)
        self.customer.SetPass("test123")
        self.customer.SetName("Akshay")
        self.customer.SetLastName("Hachade")
        self.customer.SetGendarSelection("Male")
        self.customer.SetDateOfSelection("06/11/1996")  # Day/month/Year
        self.customer.SetCompanyName("Altair")
        self.customer.taxExaminated()
       # self.customer.SetNewsLatter("Test store 2")
        #self.customer.SetSelectCustomerRoll("Guests")
       # self.customer.SetManageOfVendar("Vendor 2")
        self.customer.SetManageOfVendar()
        self.customer.SetAdminComment("This is akshay ______________")
        self.customer.SaveCustomerPage()
        logs.info("*************Saving Customer information********************")
        self.msg=self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True==True
            logs.info("*************Add customer successfully alert validated and pass ********************")
        else:

            logs.info("*************Add customer successfully alert validated and failed ********************")
            self.driver.get_screenshot_as_file("C:/Users/akshha/PycharmProjects/pythonProject/ecommer_project2/Screenshorts/add_customer.png")
            assert False
            self.driver.close()
        logs.info("*************Test_003_Add_Customer Test Cases ********************")
        self.driver.close()
        self.driver.quit()


def random_generation(size=8,chars=string.ascii_lowercase+string.digits):
    return''.join(random.choice(chars) for x in range(size))
