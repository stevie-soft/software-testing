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
    TITLE_MR_RBUTTON = DomElement(
        "input",
        {
            "id": "id_gender1",
        },
    )
    TITLE_MRS_RBUTTON = DomElement(
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
    BIRTH_DATE_DAY_SELECT = DomElement(
        "select",
        {
            "data-qa": "days",
        },
    )
    BIRTH_DATE_MONTH_SELECT = DomElement(
        "select",
        {
            "data-qa": "months",
        },
    )
    BIRTH_DATE_YEAR_SELECT = DomElement(
        "select",
        {
            "data-qa": "years",
        },
    )
    FIRST_NAME_FIELD = DomElement(
        "input",
        {
            "data-qa": "first_name",
        },
    )
    LAST_NAME_FIELD = DomElement(
        "input",
        {
            "data-qa": "last_name",
        },
    )
    ADDRESS_FIELD = DomElement(
        "input",
        {
            "data-qa": "address",
        },
    )
    COUNTRY_SELECT = DomElement(
        "select",
        {
            "data-qa": "country",
        },
    )
    STATE_FIELD = DomElement(
        "input",
        {
            "data-qa": "state",
        },
    )
    CITY_FIELD = DomElement(
        "input",
        {
            "data-qa": "city",
        },
    )
    ZIPCODE_FIELD = DomElement(
        "input",
        {
            "data-qa": "zipcode",
        },
    )
    MOBILE_NUMBER_FIELD = DomElement(
        "input",
        {
            "data-qa": "mobile_number",
        },
    )
    CREATE_ACCOUNT_BUTTON = DomElement(
        "button",
        {
            "data-qa": "create-account",
        },
    )
    SUCCESSFUL_SIGNUP_MESSAGE = DomElement(
        "h2",
        {
            "data-qa": "account-created",
        },
    )

    ELEM_MAP: dict[str, DomElement] = {
        "title Mr": TITLE_MR_RBUTTON,
        "title Mrs": TITLE_MRS_RBUTTON,
        "Password": PASSWORD_FIELD,
        "Day of Birth": BIRTH_DATE_DAY_SELECT,
        "Month of Birth": BIRTH_DATE_MONTH_SELECT,
        "Year of Birth": BIRTH_DATE_YEAR_SELECT,
        "First name": FIRST_NAME_FIELD,
        "Last name": LAST_NAME_FIELD,
        "Address": ADDRESS_FIELD,
        "Country": COUNTRY_SELECT,
        "State": STATE_FIELD,
        "City": CITY_FIELD,
        "Zipcode": ZIPCODE_FIELD,
        "Mobile Number": MOBILE_NUMBER_FIELD,
        "Signup Message": SUCCESSFUL_SIGNUP_MESSAGE,
    }

    def choose_title(self, title: Literal["Mr", "Mrs"]) -> None:
        if title == "Mr":
            target = self.GENDER_MALE_RBUTTON
        else:
            target = self.GENDER_FEMALE_OPTION

        self.html.click_on(target)

    def fill(self, field_name: str, value: str) -> None:
        field = self.ELEM_MAP[field_name]
        self.html.fill(field, value)

    def click(self, element_name: str) -> None:
        dom_element = self.ELEM_MAP[element_name]
        self.html.click_on(dom_element)

    def set(self, field_name: str, value: str) -> None:
        field = self.ELEM_MAP[field_name]
        self.html.set_option_by_text(field, value)

    def says(self, element_name: str, value: str) -> bool:
        dom_element = self.ELEM_MAP[element_name]
        web_element = self.html.find_visible(dom_element)
        return web_element.text.lower() == value

    def enter_password(self, password: str) -> None:
        self.html.fill(self.PASSWORD_FIELD, password)

    def set_birthdate_day(self, day: int) -> None:
        self.html.set_option_by_value(self.BIRTH_DATE_DAY_SELECT, str(day))

    def set_birthdate_month(self, month: str) -> None:
        self.html.set_option_by_text(self.BIRTH_DATE_MONTH_SELECT, month)

    def set_birthdate_year(self, year: int) -> None:
        self.html.set_option_by_value(self.BIRTH_DATE_YEAR_SELECT, str(year))

    def enter_first_name(self, first_name: str) -> None:
        self.html.fill(self.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.html.fill(self.FIRST_NAME_FIELD, last_name)

    def enter_state(self, state: str) -> None:
        self.html.fill(self.STATE_FIELD, state)

    def enter_city(self, city: str) -> None:
        self.html.fill(self.CITY_FIELD, city)

    def enter_zipcode(self, zipcode: str) -> None:
        self.html.fill(self.ZIPCODE_FIELD, zipcode)

    def enter_address(self, address: str) -> None:
        self.html.fill(self.ADDRESS_FIELD, address)

    def enter_mobile_number(self, mobile_number: str) -> None:
        self.html.fill(self.MOBILE_NUMBER_FIELD, mobile_number)

    def send(self):
        self.html.click_on(self.CREATE_ACCOUNT_BUTTON)

    def is_successful_signup_message_visible(self) -> bool:
        web_element = self.html.find_visible(self.SUCCESSFUL_SIGNUP_MESSAGE)
        return web_element.text.lower() == "account created!"

    @property
    def is_visible(self) -> bool:
        return self.html.is_clickable(self.CREATE_ACCOUNT_BUTTON)
