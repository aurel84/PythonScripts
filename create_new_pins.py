import csv
import random

csv_file = "/path/to/directory/file.csv"


def make_pin(pass_length: int):
    int_list = []
    for i in range(pass_length):
        i = random.randint(0, 9)
        int_list.append(i)

    int_list = int("".join(str(x) for x in int_list))

    return int_list


with open(csv_file, "r") as read_file:
    reader = csv.reader(read_file)
    header = next(reader, None)

    print("email", "platform", "status", "passcode")

    for row in reader:
        email = row[0]
        platform = row[3].strip(" ")
        status = row[6].strip(" ")

        if platform == "MacOS" and status == "pending":
            print(email, platform, status, make_pin(6))
