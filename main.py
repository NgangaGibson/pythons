import phonenubers
from phonenumbers import geocoder
def_check_phone_region(target):
    phone=phonenumbers.parse(target.none)
    if not phonenumbers.is_valid_number(phone)
    print("invalid phoneNumber")
    return
    region=geocoder.description_for_number(phone,"en")
    print("phone number",target)
    print("numbering region",region or"unknown")
    except phonenumbers.Numbersparseexception:
        print("please enter a valid number format")
        check_phone_region("")