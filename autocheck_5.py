def format_phone_number(func):
    def international_number(number):
        phone = func(number)
        if len(phone) == 12:
            return '+' + phone
        else:
            return '+38' + phone
    return international_number
    

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

format_phone_number(sanitize_phone_number('+38(097)2056043'))