class InvalidMarkError(Exception):
    pass

def students(name,*mark):
    if len(mark) == 0:
        print("no marks")
    for m in mark:    
        if(m < 0 or m > 100):
            raise InvalidMarkError("mark must be 0 to 100")
    avg = sum(mark) / len(mark)
    if avg >= 90:
        grade= "A"
    elif avg >= 79:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"
    return name, avg, grade
# results = students("sara",90,56,32,87,99,78)
# print(results)   
def report(students_list):
    print("_" *40)
    print(f"{'name' :<10}{'average' :<10}{'grade' :<10}")
    print("_" *40)
    for student in students_list:
        try:
            name = student[0]
            mark = student[1:]
            result = students(name,*mark)
            print(f"{result[0]:<10} {result[1]:<10} {result[2]:<10}")
        except InvalidMarkError as e:
            print(f"{student[0]:<10 }error: {e}")
std_data =[
    ("sara",98,65,43,23,90,66),
    ("cherry",99,80,80,70,93,99),
    ("tom",67,2,78,45,88,66)
]
report(std_data)        





     
