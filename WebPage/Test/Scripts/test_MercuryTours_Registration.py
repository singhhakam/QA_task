__author__ = 'Singhhakam'

import unittest
from time import sleep
from WebPage.Test.TestUtility.ScreenShot import SS
from WebPage.Src.PageObject.Pages.ConfirmationPage import Confirmation
from WebPage.Src.PageObject.Pages.HomePage import Home
from WebPage.Src.TestBase.EnvironmentSetUp import EnvironmentSetup

from WebPage.Src.PageObject.Pages.RegistrationPage import Register


class MercuryTours_Registration(EnvironmentSetup):

    def test_RegistrationFlow(self):

# Screenshots relative paths
        ss_path = "\\Test_MercuryTours_Registration\\"
        #ss_path = '/Test_MercuryTours_Registration/'

        driver = self.driver
        self.driver.get("http://newtours.demoaut.com")
        self.driver.set_page_load_timeout(20)

# Creating object of SS screenshots utility
        ss = SS(driver)
#calling home page object to click on Register Link
        home = Home(driver)
        if home.getRegister().is_displayed():
            print("Register Link displaying")
            home.getRegister().click()
            sleep(4)

#calling registration page object to proceed with registration flow
        reg = Register(driver)
        if reg.getRegis_txt().is_displayed():
            print(reg.regis_txt.text)
            ss.ScreenShot(ss_path+'Registration.png')
        else:
            print("Registration page not loaded")
        try:
            reg.setFirstName("First name")
            reg.setLastName("S")
            reg.setPhone("0001498896")
            reg.setEmail("abc@gmail.com")
            reg.setCountry("INDIA")
            reg.setUserName("abc@gmail.com")
            reg.setPassword(123456789)
            reg.setConfirmPassword(123456789)
            sleep(5)

            ss.ScreenShot(ss_path+'RegistrationData.png')
            reg.submitRegistration()

            sleep(4)
            ss.ScreenShot(ss_path+'PostRegistration.png')
        except Exception as e:
            print("Exception occurred "+e)

#calling Post Registration check
        post = Confirmation(driver)

        print(post.thankYou.text)
        if (post.UserID.text).find("abc@gmail.com"):
            print("Registration Process Successful")
        else:
            print("User Failed to register properly")



if __name__ == '__main__':
    unittest.main()
