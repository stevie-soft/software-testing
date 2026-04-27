from typing import cast

from behave import step  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext


@step("the text field '{element_key}' of '{scope_key}' is set to '{value}'")
def fill_field_value(
    context: Context,
    scope_key: str,
    element_key: str,
    value: str,
):
    context = cast(AutomationExerciseContext, context)
    context.site.scopes[scope_key].elements[element_key].fill(value)


@step("the select field '{element_key}' of '{scope_key}' is set to '{value}'")
def set_field_value(
    context: Context,
    scope_key: str,
    element_key: str,
    value: str,
):
    context = cast(AutomationExerciseContext, context)
    context.site.scopes[scope_key].elements[element_key].set(value)


@step("the radio button '{element_key}' of '{scope_key}' is selected")
@step("the button '{element_key}' of '{scope_key}' is clicked")
def click_button(
    context: Context,
    scope_key: str,
    element_key: str,
):
    context = cast(AutomationExerciseContext, context)
    context.site.scopes[scope_key].elements[element_key].click()


@step("the element '{element_key}' of '{scope_key}' says '{text}'")
def check_text(
    context: Context,
    scope_key: str,
    element_key: str,
    text: str,
):
    context = cast(AutomationExerciseContext, context)
    assert context.site.scopes[scope_key].elements[element_key].says(text)
