import pytest
from Page_Object.base_action import Action_Class
import selenium

from Utilities.ReadProperites import Read_Cofig
from Utilities.Usag_file import usag_file
class Test_Login_Page():
    surname_input=Read_Cofig.user_name()
    password_input=Read_Cofig.password()
    wait_to_locator="//button[contains(text(),'Log in')]"

    @pytest.mark.sanity
    def test_001_login(self,catch1):
        self.driver=catch1
        #self.driver.implicitly_wait(20)
        action=Action_Class(self.driver)
        log_file=usag_file()
        logs=log_file.get_logger()
        action.click_to_go_login()
        logs.info("*************test_001_login ********************")
        logs.info("*************Go to the log file ********************")
        self.driver.switch_to.window(self.driver.window_handles[1])
        logs.info("*************Switch new windows ********************")
        action.input_surname(self.surname_input)
        logs.info("*************Added the input -surname ********************")
        action.input_password(self.password_input)
        logs.info("*************Added the input -Password ********************")
        wait=usag_file()
        wait.explict_wait(self.driver,self.wait_to_locator)
        action.click_on_login_button()
        logs.info("*************Click the button to login ********************")
        title_login_page=self.driver.title
        if title_login_page=="Dashboard / nopCommerce administration":
            logs.info("*************Title of Page Pass ********************")
            assert True
        else:
            self.driver.get_screenshot_as_file("C:/Users/akshha/PycharmProjects/pythonProject/ecommer_project2/Screenshorts/login.png")
            logs.info("*************Title of Page Fail ********************")
            assert False
        logs.info("*************Taken the screenshot for login page ********************")
        action.click_on_logout_button()
        logs.info("*************Click the button to logout ********************")

        logs.info("*************Close the current windows ********************")
        self.driver.close()
        logs.info("*************Quit the session ********************")
        self.driver.quit()