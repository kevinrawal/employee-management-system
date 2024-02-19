from fastapi import FastAPI
from Models.Employee import Employee
from Service.employee_operations import EmployeeOperations
from Service.admin_operations import AdminOperation
import uvicorn

app = FastAPI()


@app.post("/add_employee")
def add_employee(employee: Employee):
    admin = AdminOperation()
    admin.add_employee(employee)
    return admin.view_employee(employee.id)

@app.get("/employee/{employee_id}")
def view_employee(employee_id: str):
    employee = EmployeeOperations()
    data = employee.view_employee(employee_id)
    return data


if __name__ == "__main__":
    uvicorn.run(app)

