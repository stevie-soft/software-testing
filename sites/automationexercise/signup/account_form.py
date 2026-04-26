from typing import Literal

from core import DomElement, HtmlElement


class AccountForm(HtmlElement):
    GENDER_MALE_RBUTTON = DomElement(
        "input",
        {
            "id": "id_gender1",
        },
    )
    GENDER_FEMALE_OPTION = DomElement(
        "input",
        {
            "id": "id_gender2",
        },
    )
    PASSWORD_FIELD = DomElement(
        "input",
        {
            "data-qa": "password",
        },
    )

    CREATE_ACCOUNT_BUTTON = DomElement(
        "button",
        {
            "data-qa": "create-account",
        },
    )

    def choose_gender(self, gender: Literal["male", "female"]) -> None:
        if gender == "male":
            target = self.GENDER_MALE_RBUTTON
        else:
            target = self.GENDER_FEMALE_OPTION

        self.html.click_on(target)

    def enter_password(self, password: str) -> None:
        self.html.fill(self.PASSWORD_FIELD, password)

    @property
    def is_visible(self) -> bool:
        return self.html.is_clickable(self.CREATE_ACCOUNT_BUTTON)
