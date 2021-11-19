import configparser
config=configparser.ConfigParser()
config.read("C:/Users/SSERIES/PycharmProjects/ecommer_project2/ConfigureFiles/Config.ini")

class Read_Cofig:
    @staticmethod
    def user_name():
        user_name=config.get("common info","user_name")
        return user_name

    @staticmethod
    def password():
        password=config.get("common info","password")
        return password

class login_locator:
    @staticmethod
    def admin_click_button():
        admin_button=config.get("login locator","admin_button")
        return admin_button
    @staticmethod
    def surname_button():
        login_surname_id_=config.get("login locator","login_surname_id_")
        return login_surname_id_
    @staticmethod
    def pas_button():
        input_button_pass_enter_ID_=config.get("login locator","input_button_pass_enter_ID_")
        return input_button_pass_enter_ID_
    @staticmethod
    def click_tologin_button():
        click_login_button_xpath_=config.get("login locator","click_login_button_xpath_")
        return click_login_button_xpath_
    @staticmethod
    def logout_button():
        click_logout_button_xpath_=config.get("login locator","click_logout_button_xpath_")
        return click_logout_button_xpath_

class Driver_Comman:

    @staticmethod
    def URL():
        Parent_URL=config.get("base to run","Parent_URL")
        return Parent_URL


