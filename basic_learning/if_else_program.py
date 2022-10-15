marks=int(input("enter marks:"))
if marks>80:
    print("secured A grade")
elif marks>60 and marks<=80:
    print("B")
elif marks>40 and marks<=60:
    print("C")
elif marks>25 and marks<=40:
    print("B")
else:
    print("F")