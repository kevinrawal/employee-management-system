import re


class InvalidEmailError(Exception):
    def __init__(self, message="Invalid email format"):
        self.message = message
        super().__init__(self.message)


class InvalidContactNumberError(Exception):
    def __init__(self, message="Invalid contact number"):
        self.message = message
        super().__init__(self.message)


def confirmation() -> bool:
    flag = input("confirm to change [y/n]: ")
    return flag == "yes" or flag == "y"


def set_name():
    while True:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        if confirmation():
            return first_name, last_name


def generate_employee_id(employee_list: dict, available_id: list) -> int:
    if len(available_id) == 0:
        return len(employee_list) + 1
    else:
        employee_id = available_id[len(available_id) - 1]
        available_id.pop()
        return employee_id


def set_department_name():
    while True:
        department_name = input("Department Name: ")
        if confirmation():
            return department_name


def set_salary() -> float:
    while True:
        try:
            salary = float(input("Salary: "))
        except ValueError:
            print("Salary must be numeric value ")
        else:
            if confirmation():
                return salary


def set_email_id() -> str:
    while True:
        try:
            email = input("Enter email address: ")
            email_pattern = r"\b[A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if not re.fullmatch(email_pattern, email):
                raise InvalidEmailError
        except InvalidEmailError as e:
            print(e)
        else:
            if confirmation():
                return email


def set_contact_number():
    while True:
        try:
            contact_number = input("Enter contact number, ie +91 123XXXX: ")
            contact_number_pattern = r"\+[1-9]\d{0,2}\s?\d{5,15}"  # to update
            if not re.fullmatch(contact_number_pattern, contact_number):
                raise InvalidContactNumberError
        except InvalidContactNumberError as e:
            print(e)
        else:
            if confirmation():
                return contact_number
