from datetime import datetime
from typing import Any, cast

from behave.runner import Context

from api import UserApi, User
from features.context import AutomationExerciseContext, State
from sites.automationexercise.website import AutomationExerciseWebsite
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


user_api = UserApi()
MAIN_USER = User(
    firstname="John",
    lastname="Doe",
    title="Mr",
    email="johndoe@unitesting.com",
    password="VerySecret1",
    birthdate=datetime(day=11, month=6, year=1991),
    country="Canada",
    state="Ontario",
    city="Toronto",
    address="123 Queen Street West",
    zipcode="M5V 3L9",
    mobile_number="+1 (416) 555-0123",
)
TEMPORARY_USER = User(
    firstname="Test",
    lastname="User",
    title="Mr",
    email="testing100@unitesting.com",
    password="Super$ecret1",
    birthdate=datetime(day=3, month=2, year=1986),
    country="United States",
    state="California",
    city="San Fransisco",
    address="Lincoln Way 77.",
    zipcode="CA 94122",
    mobile_number="415 416 4178",
)


def before_step(context: Context, _: Any):
    context = cast(AutomationExerciseContext, context)
    context.site.close_ads()


def before_all(context: Context):
    context = cast(AutomationExerciseContext, context)
    options = Options()
    # options.add_argument("--headless=new")
    # options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options)
    context.site = AutomationExerciseWebsite(driver)
    context.state = State()
    context.state.logged_in = False

    user_api.create_one(MAIN_USER)


def after_all(context: Context):
    context = cast(AutomationExerciseContext, context)
    user_api.delete_many(
        [
            MAIN_USER,
            TEMPORARY_USER,
        ]
    )
    context.site.driver.quit()
