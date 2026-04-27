from time import sleep
from typing import cast

from behave import step  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext
from features.environment import MAIN_USER
from features.steps.scoped_steps import click_button, fill_field_value


@step("the '{page_key}' page is opened")
def visit_page(context: Context, page_key: str):
    context = cast(AutomationExerciseContext, context)
    context.site.pages[page_key].visit()


@step("the message '{message}' appears")
def check_message(context: Context, message: str) -> None:
    context = cast(AutomationExerciseContext, context)
    context.site.says(message)


@step("the user is logged in")
def login(context: Context):
    context = cast(AutomationExerciseContext, context)
    if context.state.logged_in:
        return

    logout(context)
    visit_page(context, "Login")
    check_cookie(context)
    fill_field_value(context, "Login Form", "Email Address", MAIN_USER.email)
    fill_field_value(context, "Login Form", "Password", MAIN_USER.password)
    click_button(context, "Login Form", "Login")
    check_message(context, "Logged in as")
    context.state.logged_in = True


@step("the user is logged out")
def logout(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.driver.delete_all_cookies()


@step("the cookie modal is closed")
def check_cookie(context: Context):
    context = cast(AutomationExerciseContext, context)
    if context.site.has_cookie("__gads"):
        return

    context.site.cookie_modal.accept()


@step("we wait '{seconds}' seconds")
def wait(_: Context, seconds: str):
    sleep(int(seconds))
