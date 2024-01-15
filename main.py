# main.py
from employee import Employee
from set_employee_details import (set_name, set_department_name, set_salary, set_email_id, set_contact_number,
                                  generate_employee_id)


def display_employee_details(employee_details):
    print("\nEmployee Details:")
    print("Employee ID:", employee_details[0])
    print("Name:", employee_details[1], employee_details[2])
    print("Email ID:", employee_details[4])
    print("Contact Number:", employee_details[5])
    print("Department:", employee_details[3])
    print("Salary:", employee_details[6])


def update_employee_details(employee_list, employee_id):
    if employee_id not in employee_list:
        print("Employee not found.")
        return

    pre_employee = employee_list[employee_id]
    while True:
        display_employee_details(pre_employee)
        print("\nOptions to Update:")
        print("1. Update Name")
        print("2. Update Email ID")
        print("3. Update Contact Number")
        print("4. Update Department")
        print("5. Update Salary")
        print("6. Go back")

        update_option = int(input("Choose an option: "))
        if update_option == 6:
            print("Going back to the main menu.")
            break

        elif 1 <= update_option <= 5:
            if update_option == 1:
                first_name, last_name = set_name()
                pre_employee[1] = first_name
                pre_employee[2] = last_name
                print("Name updated successfully.")

            elif update_option == 2:
                pre_employee[4] = set_email_id()
                print("Email ID updated successfully.")

            elif update_option == 3:
                pre_employee[5] = set_contact_number()
                print("Contact Number updated successfully.")

            elif update_option == 4:
                pre_employee[3] = set_department_name()
                print("Department updated successfully.")

            elif update_option == 5:
                pre_employee[6] = set_salary()
                print("Salary updated successfully.")

        else:
            print("Invalid option. Please try again.")


def main():
    employee_list = {}
    available_id = []

    # open employee details file and store it in dictionary
    with open("employee_data.txt", "r") as file:
        for line in file:
            info_pieces = line.strip().split(', ')

            employee_id = int(info_pieces[0])
            salary = float(info_pieces[6])

            # Replace the original values with converted ones
            info_pieces[0] = employee_id
            info_pieces[6] = salary

            employee_list[employee_id] = info_pieces

    # open available ids list and store it in list
    with open("available_id.txt", "r") as file:
        for line in file:
            available_id.append(int(line))

    print("\nMain Menu:")
    print("1. Add New Employee")
    print("2. Delete Employee")
    print("3. Update Employee Information")
    print("4. show employee details")
    print("5. save and exit")

    while True:
        user_input = int(input("$admin: "))  # I will change it in the future to string
        match user_input:
            # add new employee
            case 1:
                new_employee = Employee()
                employee_id = generate_employee_id(employee_list, available_id)

                new_employee.set_employee_id(employee_id)
                first_name, second_name = set_name()
                new_employee.set_name(first_name, second_name)
                new_employee.set_email_id(set_email_id())
                new_employee.set_contact_number(set_contact_number())
                new_employee.set_department_name(set_department_name())
                new_employee.set_salary(set_salary())

                employee_list[employee_id] = new_employee.get_employee_details_list()

                print("New employee added 🥳")

            # delete employee
            case 2:
                employee_id = int(input("Enter Employee ID to delete: "))
                deleted_employee = employee_list.pop(employee_id, None)
                if deleted_employee:
                    print(f"Employee {deleted_employee} deleted")
                    available_id.append(employee_id)
                else:
                    print("Employee not found.")

            # update information about employee
            case 3:
                employee_id = int(input("Enter Employee ID to update: "))
                update_employee_details(employee_list,employee_id)

            case 4:
                #TODO
                pass

            # save and exit
            case 5:
                with open("employee_data.txt", "w") as file:
                    for details in employee_list.values():
                        file.write(", ".join(map(str, details)) + "\n")
                    print("Employee data saved.")

                with open("available_id.txt", "w") as file:
                    for ids in available_id:
                        file.write(str(ids) + "\n")

                print("Exiting the program.")
                break

            case _:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
