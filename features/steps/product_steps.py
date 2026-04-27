from typing import cast

from behave import step  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext


@step("'{count_str}' products appear")
def count_products(context: Context, count_str: str):
    context = cast(AutomationExerciseContext, context)
    expected_count = int(count_str)
    assert expected_count == context.site.count(".single-products")
