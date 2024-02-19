from pydantic import BaseModel


class Employee(BaseModel):
    id: str
    email_id: str
    contact_number: str
    name: str
    department: str
    salary: float
    grade: int
