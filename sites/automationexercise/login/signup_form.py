from core import HtmlElement


class SignupForm(HtmlElement):
    ELEMENTS = {
        # region: FORM FIELDS
        "Name": ("input", {"data-qa": "signup-name"}),
        "Email": ("input", {"data-qa": "signup-email"}),
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
        "Signup": ("button", {"data-qa": "signup-button"}),
        # endregion
        #
        # region: TEXTS
        "Error Message": ("p", {"style": "color: red;"}),
        # endregion
    }
