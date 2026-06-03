def calculate_grade(*marks):
    avg = sum(marks) / len(marks)
    if(avg >= 90):
        return "A"
    elif(avg >= 80):
        return "B"
    elif(avg >= 70):
        return "c"
    else:
        return "F"

    return(marks)
print(calculate_grade(99,67,78,92))  
