from typing import cast

from behave import given, step, then, when  # type: ignore | Incomplete typing | **kwargs: Unknown
from behave.runner import Context
from features.context import AutomationExerciseContext


@given("the random step is defined")
def random_step(context: Context):
    context = cast(AutomationExerciseContext, context)
    context.site.home_page.visit()
