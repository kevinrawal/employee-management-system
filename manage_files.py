from set_employee_details import confirmation


def open_file_employee_data(employee_list: dict, path: str):
    with open(path, "r") as file:
        for line in file:
            info_pieces = line.strip().split(', ')

            employee_id = int(info_pieces[0])
            salary = float(info_pieces[6])

            # Replace the original values with converted ones
            info_pieces[0] = employee_id
            info_pieces[6] = salary

            employee_list[employee_id] = info_pieces


def open_file_available_id(available_id: list, path: str):
    with open(path, "r") as file:
        for line in file:
            available_id.append(int(line))


def close_file_employee_data(employee_list: dict, path: str):
    with open(path, "w") as file:
        for details in employee_list.values():
            file.write(", ".join(map(str, details)) + "\n")
        print("Employee data saved.")


def close_file_available_id(available_id: list, path: str):
    with open(path, "w") as file:
        for ids in available_id:
            file.write(str(ids) + "\n")


def open_backup_files() -> bool:
    flag = False
    with open("employee_data_backup.txt", 'r') as file1:
        first_char = file1.read(1)
        if first_char:
            flag = True

    with open("available_id_backup.txt", 'r') as file2:
        first_char = file2.read(1)
        if first_char:
            flag = True

    if flag:
        if confirmation("some changes are not saved, do you want to backup[y/n]: "):
            return True
        else:
            return False
    else:
        return False


def clear_file(path):
    with open(path, 'w'):
        pass  # The pass statement is used because we don't need to perform any write operation


def append_in_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


if __name__ == "__main__":
    pass
