mark=[23,76,34,87,23,56,88,11,22,45]
average=(sum(mark)/len(mark))
print(average)
largest=max(mark)
lowest=min(mark)
unique=list(set(mark))
print(unique)
above=[]
for i in mark:
    if(i>average):
        above.append(i)
print(above)
print(mark)
print("\n____student marks____")  
print("average",average)
print("unique",unique)
print("highest",largest)
print("lowest",lowest)
print("above ",above)     