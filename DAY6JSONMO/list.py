import json
students=[
    {"name" :"sara","age":22,"mark":34},
     {"name":"soya","age":11,"mark":69},
     {"name":"ranju","age":23,"mark":88},
     {"name":"izza","age":30,"mark":90},
     {"name":"zera","age":19,"mark":78}
     ]
with open("students.json","w") as f:
    json.dump(students,f,indent=2)
with open("students.json","r") as f:
    print(f.read()) 
# print("\n studens deatails:")
# for student in data:

