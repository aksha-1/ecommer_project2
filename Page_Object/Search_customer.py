class Test_customer_search:
    txt_search_email_id="SearchEmail"
    text_search_first_name_id="SearchFirstName"
    tex_search_last_name_id="SearchLastName"
    button_click_search_id="search-customers"
    hole_table_x_path="//table[@id='customers-grid']"
    search_row_table_xpath="//table[@id='customers-grid']//tbody/tr"
    search_column_table_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def SetInput(self,email):
        self.driver.find_element_by_id(self.txt_search_email_id).clear()
        self.driver.find_element_by_id(self.txt_search_email_id).send_keys(email)

    def SetFirstName(self,firstname):
        self.driver.find_element_by_id(self.text_search_first_name_id).clear()
        self.driver.find_element_by_id(self.text_search_first_name_id).send_keys(firstname)

    def SetLastName(self,lastname):
        self.driver.find_element_by_id(self.tex_search_last_name_id).clear()
        self.driver.find_element_by_id(self.tex_search_last_name_id).send_keys(lastname)
    def ClickOnButton(self):
        self.driver.find_element_by_id(self.button_click_search_id).click()

    def NoRowOfTable(self):
        return len(self.driver.find_element_by_xpath(self.search_row_table_xpath))


    def NoColumnOfTable(self):
        column=len(self.driver.find_element_by_xpath(self.search_column_table_xpath))
        return column
    def SerchCustomerByEmail(self,useremail):
        flag=False
        for r in range(1,2):
            row=self.driver.find_element_by_xpath(self.hole_table_x_path)
            email_on_page=row.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email_on_page==useremail:
                flag=True
                break
        return flag
    def SerchCustomerByName(self,username):
        flag=False
        for r in range(1,self.NoColumnOfTable()+1):
            row=self.driver.find_element_by_xpath(self.hole_table_x_path)
            search_name=row.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if search_name==username:
                flag=True
                break
        return flag



