from typing import cast

from behave import given, step  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext


@step("the home page is opened")
def step_impl(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.home_page.open()


@given("the cookie modal is closed")
def coookie(context: Context):
    context = cast(AutomationExerciseContext, context)
    # todo: impl


@step("the login page is opened")
def step_impl_2(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.login_page.open()


@given("the name field is filled with '{value}'")
def step_impl_3(context: Context, value: str):
    context = cast(AutomationExerciseContext, context)
    context.site.login_page.signup_form.name_field.fill(value)


@given("the 'email' field is filled with '{value}'")
def step_impl_4(context: Context, value: str):
    context = cast(AutomationExerciseContext, context)
    context.site.login_page.signup_form.email_field.fill(value)


@step("the browser quits")
def step_impl_5(context: Context, value: str):
    context = cast(AutomationExerciseContext, context)
