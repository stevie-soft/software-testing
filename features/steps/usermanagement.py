from typing import cast

from behave import given, step, then, when  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext


@given("the home page is opened")
def step_impl_10(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.home_page.visit()


@given("the cookie modal is closed")
def coookie_check(context: Context):
    context = cast(AutomationExerciseContext, context)
    if context.site.cookie_modal.is_accepted:
        return

    context.site.cookie_modal.accept()


@given("the login page is opened")
def step_impl_20(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.login_page.visit()


@given("the field '{field_name}' is filled with '{field_value}'")
def fill_field_value(context: Context, field_name: str, field_value: str):
    context = cast(AutomationExerciseContext, context)
    context.site.account_form.fill(field_name, field_value)


@given("the field '{field_name}' is set to '{field_value}'")
def set_field_value(context: Context, field_name: str, field_value: str):
    context = cast(AutomationExerciseContext, context)
    context.site.account_form.set(field_name, field_value)


@given("the option '{field_name}' is selected")
def select_option(context: Context, field_name: str):
    context = cast(AutomationExerciseContext, context)
    context.site.account_form.click(field_name)


@given("the name '{value}' is entered")
def step_impl_30(context: Context, value: str):
    context = cast(AutomationExerciseContext, context)
    context.site.signup_form.enter_name(value)


@given("the email '{value}' is entered")
def step_impl_40(context: Context, value: str):
    context = cast(AutomationExerciseContext, context)
    context.site.signup_form.enter_email(value)


@when("the signup form is sent")
def step_impl_50(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.signup_form.send()


@then("the account form appears")
def step_impl_60(context: Context):
    context = cast(AutomationExerciseContext, context)
    assert context.site.account_form.is_visible is True


@when("the account form is sent")
def step_impl_80(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.account_form.send()


@then("the '{message}' message appears")
def step_impl_90(context: Context, message: str):
    context = cast(AutomationExerciseContext, context)
    context.site.says(message)
