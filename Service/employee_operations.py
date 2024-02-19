from Service import manage_file
from filelock import FileLock


class EmployeeOperations:
    def __init__(self):
        pass

    def view_employees(self):
        try:
            employee_list = manage_file.read_data("all_employee")
        except FileNotFoundError as e:
            return e
        else:
            data = []
            for employee_id in employee_list["employee"]:
                data.append(self.view_employee(employee_id))
            return data

    def view_employee(self, employee_id: str):
        try:
            data = manage_file.read_data(employee_id)
        except FileNotFoundError as e:
            return e
        else:
            return data

    def update_details(self, employee_id, update_filed, updated_value):
        filepath = f"{manage_file.base_path}{employee_id}.json"
        try:
            manage_file.validate_file(filepath)
            lock = FileLock(f"{filepath}.lock", timeout=5)

            while lock.acquire(True):
                print("Waiting...")

            with lock:
                data = manage_file.read_data(employee_id)
                data[update_filed] = updated_value
                manage_file.write_data(employee_id, data)

        except FileNotFoundError as e:
            return e

    def update_name(self, employee_id: str, new_name: str):
        self.update_details(employee_id, "name", new_name)

    def update_email(self, employee_id: str, new_email: str):
        self.update_details(employee_id, "email_id", new_email)

    def update_contact_number(self, employee_id: str, new_contact_number: str):
        self.update_details(employee_id, "contact_number", new_contact_number)

