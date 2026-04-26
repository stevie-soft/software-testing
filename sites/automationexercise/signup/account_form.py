from core import HtmlElement


class AccountForm(HtmlElement):
    ELEMENTS = {
        # region: FORM FIELDS
        "Mr.": ("input", {"id": "id_gender1"}),
        "Mrs.": ("input", {"id": "id_gender2"}),
        "Password": ("input", {"data-qa": "password"}),
        "Day of Birth": ("select", {"data-qa": "days"}),
        "Month of Birth": ("select", {"data-qa": "months"}),
        "Year of Birth": ("select", {"data-qa": "years"}),
        "First name": ("input", {"data-qa": "first_name"}),
        "Last name": ("input", {"data-qa": "last_name"}),
        "Address": ("input", {"data-qa": "address"}),
        "Country": ("select", {"data-qa": "country"}),
        "State": ("input", {"data-qa": "state"}),
        "City": ("input", {"data-qa": "city"}),
        "Zipcode": ("input", {"data-qa": "zipcode"}),
        "Mobile Number": ("input", {"data-qa": "mobile_number"}),
        # endregion
        #
        # region: BUTTONS
        "Create Account": ("button", {"data-qa": "create-account"}),
        "Continue": ("a", {"data-qa": "continue-button"}),
        # endregion
    }

    @property
    def is_visible(self) -> bool:
        return self.elements["Create Account"].is_clickable()
