import time

import pytest
from Page_Object.base_action  import Action_Class
import selenium

from Utilities.ReadProperites import Read_Cofig
from Utilities.Usag_file import usag_file
from Utilities import ExcelUtils
class Test_Login_002_DDT_Page():
    path="C:/Users/akshha/PycharmProjects/pythonProject/ecommer_project2/TestData/Login_data.xlsx"
    #surname_input=Read_Cofig.user_name()
   # password_input=Read_Cofig.password()
    wait_to_locator="//button[contains(text(),'Log in')]"

    @pytest.mark.regression
    def test_DDT_login(self,catch1):

        self.driver=catch1
        self.driver.implicitly_wait(20)
        action=Action_Class(self.driver)
        log_file=usag_file()
        logs=log_file.get_logger()

        action.click_to_go_login()
        logs.info("*************Go to the log file ********************")
        self.driver.switch_to.window(self.driver.window_handles[1])
        logs.info("*************test_002_DDT_login""********************")
        logs.info("*************Verifying login test ********************")
        list_var=[]
        logs.info("*************Switch new windows ********************")
        self.row=ExcelUtils.getRowCount(self.path,"Sheet1")
        for r in range(2,self.row+1):
            self.user=ExcelUtils.readData(self.path,"Sheet1",r,1)
            self.password=ExcelUtils.readData(self.path,"Sheet1",r,2)
            self.exp= ExcelUtils.readData(self.path, "Sheet1", r,3)
            action.input_surname(self.user)
            action.input_password(self.password)
            #wait = usag_file()
           # wait.explict_wait(self.driver, self.wait_to_locator)
            time.sleep(3)
            action.click_on_login_button()
            logs.info("*************click_on_login_button ********************")
            Actual_Title=self.driver.title
            expect_title="Dashboard / nopCommerce administration"
            if Actual_Title==expect_title:
                logs.info("*************expect_title pass ********************")
                if self.exp=="Pass":
                    action.click_on_logout_button()
                    logs.info("************* Passed ********************")
                    list_var.append("Pass")
                elif self.exp=="Fail":
                    logs.info("************* Failed ********************")
                    action.click_on_logout_button()
                    list_var.append("Fail")

            elif Actual_Title!=expect_title:
                logs.info("*************expect_title Failed ********************")
                if self.exp=="Pass":
                    logs.info("************* Failed ********************")
                    list_var.append("Fail")
                elif self.exp=="Fail":
                    logs.info("************* Pass ********************")
                    list_var.append("Pass")
        if "Fail" not in list_var:
            logs.info("************* Login DDT test Passed............ ********************")
            assert True
            self.driver.close()
        else:
            logs.info("************* Login DDT test Failed............ ********************")
            assert False

        logs.info("************ End Of the Login DDT Test Process **************")
        self.driver.close()
        self.driver.quit()









