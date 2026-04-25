from behave.runner import Context

from sites.automationexercise.website import AutomationExerciseWebsite
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
# options.add_argument("--headless=new")
# options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options)


def before_all(context: Context):
    context.site = AutomationExerciseWebsite(driver)


def after_all(_: Context):
    driver.quit()
