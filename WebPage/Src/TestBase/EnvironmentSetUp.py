__author__ = 'Singhhakam'

import unittest
import datetime
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):

#setUP contains the browser setup attributes
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(
            executable_path=r"geckodriver.exe")
        print ("Run Started at :"+str(datetime.datetime.now()))
        print("Environment Set Up")
        print("------------------------------------------------------------------")
        self.driver.implicitly_wait(20)
#        self.driver.maximize_window()

#tearDown method just to close all the browser instances and then quit
    @classmethod
    def tearDown(self):
     if (self.driver!=None):
        print("------------------------------------------------------------------")
        print("Test Environment Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))
        self.driver.close()
        self.driver.quit()