# class InvalidMarkEror(Exception):
#     pass
def calculate_grade( name : str,grade :chr,mark :list[int])->str:
    avg = sum(mark) / len(mark)
    if avg >= 89:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 75:
        return "C"
    elif avg >= 65:
        return "D"
    else:
        return "F"
# name : str = input("enter name :")
# mark : int = int(input("enter marks :"))    
# mark : list[int]=[98,65,90]
# grade : str = calculate_grade(name,mark)
# print("name :",name) 
# print("grade :",grade)    
# 
name = input("enter name :")
marks =[90,67,34] 
grade = calculate_grade(mark)
print("name :",name)
print("grade :",grade)         