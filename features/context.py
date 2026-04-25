from behave.runner import Context

from sites.automationexercise.website import AutomationExerciseWebsite


class AutomationExerciseContext(Context):
    site: AutomationExerciseWebsite
