class InvalidMarkError(Exception):
    pass


def students(name, *mark):

    if len(mark) == 0:
        print("No marks")

    for m in mark:
        if m < 0 or m > 100:
            raise InvalidMarkError("mark must be 0 to 100")

    avg = sum(mark) / len(mark)

    if avg >= 90:
        grade = "A"
    elif avg >= 79:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"

    return name, avg, grade


def report(student_list):

    print("-" * 35)
    print(f"{'Name':<10}{'Average':<10}{'Grade':<10}")
    print("-" * 35)

    for student in student_list:
        try:
            name = student[0]
            mark = student[1:]

            result = students(name, *mark)

            print(f"{result[0]:<10}{result[1]:<10.1f}{result[2]:<10}")

        except InvalidMarkError as e:
            print(f"{student[0]:<10}Error: {e}")


student_data = [
    ("sara", 98, 65, 43, 23, 90, 66),
    ("cherry", 99, 21, 42, 77, 93, 11),
    ("tom", 67, 2, 78, 45, 88, 66)
]

report(student_data)