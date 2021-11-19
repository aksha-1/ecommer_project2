import time
from selenium.webdriver.support.ui import Select

class Add_New_Customer:
    lik_customer_manu_x_path="//p[contains(text(),'Customers')]"
    #lik_customer_manu_x_path="//a[@href='#']//span[contains(text(),'Customers')]"
    #lik_customer_sub_menu_x_path="//span[@class='menu-item-title'] [contains(text(),'Customers')]"
    lik_customer_sub_menu_x_path="//p[contains(text(),' Customers')]"
    lin_button_add_new_x_path="//a[@class='btn btn-primary']"
    text_input_email_x_path="//input[@id='Email']"
    text_input_pass_x_path="//input[@id='Password']"
    text_input_name_x_path="//input[@id='FirstName']"
    text_input_lastname_xpath="//input[@id='LastName']"
    rb_select_male_xpath="//input[@id='Gender_Male']"
    rb_select_female_xpath="//input[@id='Gender_Female']"
    text_input_data_of_birth="//input[@id='DateOfBirth']"
    text_input_company_name_id="Company"
    text_cb_tax_examineted_id="IsTaxExempt"
    list_box_new_letter_x_path="//div[@class='k-multiselect-wrap k-floatwrap']"
    list_box_Your_store_name_x_path="//option[contains(text(),'Your store name')]"
    list_customer_roll_x_path="//div[@class='k-multiselect-wrap k-floatwrap']"
    list_customer_Administrators_x_path="//option[contains(text(),'Administrators')]"
    list_customer_Guests_x_path="//option[contains(text(),'Guests')]"
    list_del_customer_xpath="//span[@class='k-select']//span[2]"
    list_customer_Registered_x_path="//option[contains(text(),'Registered')]"
    list_customer_Vendors_x_path="//option[contains(text(),'Vendors')]"
    rd_manage_vendor_x_path="//select[@id='VendorId']"
    text_admin_comment_x_path="//textarea[@id='AdminComment']"
    button_save_customer_x_path="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def ClickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lik_customer_manu_x_path).click()

    def ClickOnCustomerSubMenu(self):
        self.driver.find_element_by_xpath(self.lik_customer_sub_menu_x_path).click()

    def ClickOnAddNew(self):
        self.driver.find_element_by_xpath(self.lin_button_add_new_x_path).click()

    def SetEmail(self,email_Id):
        self.driver.find_element_by_xpath(self.text_input_email_x_path).send_keys(email_Id)

    def SetPass(self,password):
        self.driver.find_element_by_xpath(self.text_input_pass_x_path).send_keys(password)
    def SetName(self,name):
        self.driver.find_element_by_xpath(self.text_input_name_x_path).send_keys(name)

    def SetLastName(self,lastname):
        self.driver.find_element_by_xpath(self.text_input_lastname_xpath).send_keys(lastname)

    def SetGendarSelection(self,gendar):

        if gendar=="Male":
            #self.driver.find_element_by_xpath(self.rb_select_male_xpath).send_keys(gendar)
            self.driver.find_element_by_xpath(self.rb_select_male_xpath).click()
        elif gendar=="Female":
            #self.driver.find_element_by_xpath(self.rb_select_female_xpath).send_keys(gendar)
            self.driver.find_element_by_xpath(self.rb_select_female_xpath).click()
        else:
           # self.driver.find_element_by_xpath(self.rb_select_female_xpath).send_keys(gendar)
            self.driver.find_element_by_xpath(self.rb_select_female_xpath).click()
    def SetDateOfSelection(self,date):
        self.driver.find_element_by_xpath(self.text_input_data_of_birth).send_keys(date)


    def SetCompanyName(self,companyname):
        self.driver.find_element_by_id(self.text_input_company_name_id).send_keys(companyname)
    def taxExaminated(self):
        self.driver.find_element_by_id(self.text_cb_tax_examineted_id).click()
    def SetNewsLatter(self,name):
        self.driver.find_element_by_xpath(self.list_box_new_letter_x_path).click()
        if name=="Test store 2":
            self.driver.find_element_by_xpath(self.list_box_Your_store_name_x_path).click()

    def SetSelectCustomerRoll(self,role):
        self.driver.find_element_by_xpath(self.list_customer_roll_x_path).click()
        time.sleep(5)
        if role=="Registered":
            self.role=self.driver.find_element_by_xpath(self.list_customer_Registered_x_path).click()

        elif role=="Administrators":
            self.role=self.driver.find_element_by_xpath(self.list_customer_Administrators_x_path).click()


        elif role=="Guests":
            self.driver.find_element_by_xpath(self.list_del_customer_xpath).click()
            time.sleep(5)

            self.role=self.driver.find_element_by_xpath(self.list_customer_Guests_x_path).click()

        elif role=="Vendors":
            self.role = self.driver.find_element_by_xpath(self.list_customer_Vendors_x_path).click()
        else:
            self.role = self.driver.find_element_by_xpath(self.list_customer_Guests_x_path).click()
            time.sleep(2)
        self.driver.execute_script("arguments[0].click();",self.role)
    def SetManageOfVendar(self):
        drop=Select(self.driver.find_element_by_xpath(self.rd_manage_vendor_x_path))
        drop.select_by_index(1)
    def SetAdminComment(self,content):
        self.driver.find_element_by_xpath(self.text_admin_comment_x_path).send_keys(content)

    def SaveCustomerPage(self):
        self.driver.find_element_by_xpath(self.button_save_customer_x_path).click()
        #"The new customer has been added successfully."























