# main.py
from employee import Employee
from command_info import print_main_help, print_update_help
from manage_files import open_file_employee_data, open_file_available_id, close_file_available_id, \
    close_file_employee_data, open_backup_files, clear_file, append_in_file
from set_employee_details import (set_name, set_department_name, set_salary, set_email_id, set_contact_number,
                                  generate_employee_id, confirmation)


def display_employee(employee: list):
    print(
        f"Employee ID: {employee[0]}, "
        f"Name: {employee[1]} {employee[2]}, "
        f"Email ID: {employee[4]}, "
        f"Contact Number: {employee[5]}, "
        f"Department: {employee[3]}, "
        f"Salary: {employee[6]}\n"
    )


def display_all_employee(employee_list: dict):
    employee_list = sorted(employee_list.items(), key=lambda x: x[0])

    for _, employee in employee_list:
        display_employee(employee)


def add_employee(employee_list, available_id):
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
    # append_in_file("employee_data_backup.txt", ", ".join(map(str, employee_list[employee_id])) + "\n")
    print("New employee added 🥳")


def delete_employee(employee_list: dict, available_id: list):

    employee_ids = list(map(int, input("Enter Employee IDs to delete: ").split()))
    if confirmation("Are you sure you wanted to delete[y/n]"):
        for employee_id in employee_ids:
            deleted_employee = employee_list.pop(employee_id, None)
            if deleted_employee:
                print(f"Employee {deleted_employee} deleted")
                available_id.append(employee_id)
                # append_in_file("available_id_backup.txt", employee_id)
            else:
                print("Employee not found.")


def update_employee_details(employee_list):
    employee_id = int(input("Enter Employee ID to update: "))

    if employee_id not in employee_list:
        print("Employee not found.")

    duplicate_employee = employee_list[employee_id].copy()  # shallow copy, used for recovery changes
    prev_employee = employee_list[employee_id]  # deep copy
    display_employee(prev_employee)
    # print_update_help()
    while True:

        admin_command = input("$admin-update: ")
        if admin_command == "exit-u":
            # append_in_file("employee_data_backup.txt", ", ".join(map(str, employee_list[employee_id])) + "\n")
            print("changes saved, Going back to the main menu.")
            break

        elif admin_command == "exit":
            if confirmation("changes will not saved if you exit directly, are you sure[y/n]"):
                employee_list[employee_id] = duplicate_employee
                print("changes not saved !!")
                break

        elif admin_command == "u-name":
            first_name, last_name = set_name()
            prev_employee[1] = first_name
            prev_employee[2] = last_name
            print("Name updated successfully.")

        elif admin_command == "u-email":
            prev_employee[4] = set_email_id()
            print("Email ID updated successfully.")

        elif admin_command == "u-contact":
            prev_employee[5] = set_contact_number()
            print("Contact Number updated successfully.")

        elif admin_command == "u-department":
            prev_employee[3] = set_department_name()
            print("Department updated successfully.")

        elif admin_command == "u-salary":
            prev_employee[6] = set_salary()
            print("Salary updated successfully.")

        elif admin_command == "help":
            print_main_help()

        elif admin_command == "help-update":
            print_update_help()

        else:
            print('invalid command, use "help-update" for list down all commands')


def main():
    employee_list = {}
    available_id = []

    # open employee details file and store it in dictionary
    open_file_employee_data(employee_list, "employee_data.txt")

    # open available ids list and store it in list
    open_file_available_id(available_id, "available_id.txt")

    # backup
    # if open_backup_files():
    #     open_file_employee_data(employee_list, "employee_data_backup.txt")
    #     open_file_available_id(available_id, "available_id_backup.txt")

    # clear_file("employee_data_backup.txt")
    # clear_file("available_id_backup.txt")

    while True:
        user_input = input("$admin: ")
        match user_input:
            # add new employee
            case "add-employee":
                add_employee(employee_list, available_id)

            # delete employee
            case "delete-employee":
                delete_employee(employee_list, available_id)

            # update information about employee
            case "update-employee":
                update_employee_details(employee_list)

            case "read-employee":
                display_all_employee(employee_list)

            case "help":
                print_main_help()

            # save and exit
            case "exit":
                # save employee data
                close_file_employee_data(employee_list, "employee_data.txt")

                # save ids data
                close_file_available_id(available_id, "available_id.txt")

                # clear_file("available_id_backup.txt")
                # clear_file("employee_data_backup.txt")

                print('::Logged out::')
                break
            case _:
                print('Invalid command, use "help" to list down all commands')


if __name__ == "__main__":
    main()
