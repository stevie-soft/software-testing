from typing import cast

from behave import given, step, then, when  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext


@given("the home page is opened")
def step_impl(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.home_page.visit()


@given("the cookie modal is closed")
def coookie(context: Context):
    context = cast(AutomationExerciseContext, context)
    if context.site.cookie_modal.is_accepted:
        return

    context.site.cookie_modal.accept()


@given("the login page is opened")
def step_impl_2(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.login_page.visit()


@given("the name entered is '{value}'")
def step_impl_3(context: Context, value: str):
    context = cast(AutomationExerciseContext, context)
    context.site.signup_form.enter_name(value)


@given("the email entered is '{value}'")
def step_impl_4(context: Context, value: str):
    context = cast(AutomationExerciseContext, context)
    context.site.signup_form.enter_email(value)


@when("the signup form is sent")
def step_impl_5(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.signup_form.send()


@then("the account form appears")
def step_impl_6(context: Context):
    context = cast(AutomationExerciseContext, context)
    assert context.site.account_form.is_visible is True
