import re


class Employee:

    def __init__(self):
        self.__employee_id = None
        self.__first_name = None
        self.__last_name = None
        self.__department_name = None
        self.__salary = None
        self.__contact_number = None
        self.__email_id = None

    def __repr__(self):
        return (
            f"Employee ID: {self.__employee_id}, "
            f"Name: {self.get_full_name()}, "
            f"Department: {self.__department_name}, "
            f"Salary: {self.__salary}, "
            f"Contact Number: {self.__contact_number}, "
            f"Email ID: {self.__email_id}"
        )

    def set_name(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_department_name(self, department_name):
        self.__department_name = department_name

    def set_salary(self, salary):
        self.__salary = salary

    def set_email_id(self, email):
        self.__email_id = email

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def get_employee_id(self):
        return self.__employee_id

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def get_department_name(self):
        return self.__department_name

    def get_salary(self):
        return self.__salary

    def get_email_id(self):
        return self.__email_id

    def get_contact_number(self):
        return self.__contact_number

    def get_employee_details_list(self):
        return [self.__employee_id, self.__first_name, self.__last_name, self.__department_name, self.__email_id,
                self.__contact_number, self.__salary]
