from typing import cast

from behave import step  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext


@step("the text field '{field_name}' in form '{form_name}' is set to '{field_value}'")
def fill_field_value(context: Context, field_name: str, field_value: str):
    context = cast(AutomationExerciseContext, context)
    context.site.account_form.fill(field_name, field_value)
