__author__ = 'Singhhakam'


from selenium import webdriver
class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        # You need to change this path to your machine local path D:\\Automation Tools\\python\\
        directory = "D:\\Automation Tools\\python\\QA_task\\WebPage\\ScreenShots"
        self.driver.get_screenshot_as_file(directory+path)


