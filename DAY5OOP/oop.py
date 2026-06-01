class students:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def display(self):
        print(f"name:{self.name}")
        print(f"mark:{self.mark}")
    def __str__(self):
        return self.name
s1=students("sanjayi",45)
print(s1)
s1.display()
        
    