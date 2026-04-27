from behave.runner import Context

from sites.automationexercise.website import AutomationExerciseWebsite


class State:
    def __init__(self) -> None:
        self.logged_in: bool = False


class AutomationExerciseContext(Context):
    site: AutomationExerciseWebsite
    state: State
