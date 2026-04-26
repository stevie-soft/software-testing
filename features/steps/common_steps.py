from time import sleep
from typing import cast

from behave import step  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext


@step("the '{page_key}' page is opened")
def visit_page(context: Context, page_key: str):
    context = cast(AutomationExerciseContext, context)
    context.site.pages[page_key].visit()


@step("the message '{message}' appears")
def check_message(context: Context, message: str):
    context = cast(AutomationExerciseContext, context)
    context.site.says(message)


@step("the cookie modal is closed")
def check_cookie(context: Context):
    context = cast(AutomationExerciseContext, context)
    if context.site.has_cookie("__gads"):
        return

    context.site.cookie_modal.accept()


@step("we wait '{seconds}' seconds")
def wait(_: Context, seconds: str):
    sleep(int(seconds))
