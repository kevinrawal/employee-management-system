from Service.employee_operations import EmployeeOperations
from Models import Employee
from Service import manage_file


class AdminOperation(EmployeeOperations):
    def __init__(self):
        super().__init__()
        pass

    def add_employee(self, new_employee: Employee):
        employee_id = new_employee.id
        filepath = f"{manage_file.base_path}{employee_id}.json"
        print("1")
        manage_file.create_file(filepath)
        print("2")
        try:
            manage_file.write_data(new_employee.id, new_employee.model_dump())
        except FileNotFoundError as e:
            print(e)

    def update_department(self, employee_id: str, new_department: str):
        self.update_details(employee_id, "department", new_department)

    def update_salary(self, employee_id: str, new_salary: float):
        self.update_details(employee_id, "salary", new_salary)

    def update_grade(self, employee_id: str, new_grade: int):
        self.update_details(employee_id, "grade", new_grade)

    def delete_employee(self, employee_id: str):
        try:
            manage_file.delete_file(employee_id)
        except FileNotFoundError as e:
            return e
