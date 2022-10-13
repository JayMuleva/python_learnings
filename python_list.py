#list(Lists are used to store multiple items in a single variable.)-->
#Lists are created using square brackets

thislist=["apple","banana","cherry"]
print(thislist)

#list_items(List items are ordered, changeable, and allow duplicate values.)-->

#access list items-->
#1)by indxing-->
thislist=["apple","banana","cherry"]
print(thislist[1])

#check if item exist-->
thislist=["apple","banana","cherry"]
if "banana" in thislist:
    print("yes banana is present in thislist")

#-------------------------------------------------------------------------------------------------------------

#change list items-->
thislist=["apple","banana","cherry"]
thislist[1]="watermelon"
print(thislist)

thislist=["apple","banana","cherry","pineapple"]
thislist[1:3]="watermelon","abs"
print(thislist)

thislist=["apple","banana","cherry"]
thislist.insert(1,"pineapple")
print(thislist)

#---------------------------------------------------------------------------------------------------------------

#adding list items-->
thislist=["apple","banana","cherry"]
thislist.append("hgs")
print(thislist)

thislist=["apple","banana","cherry"]
thislist.insert(1,"pineapple")
print(thislist)

thislist=["apple","banana","cherry"]  #The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
mylist=["abc","def","ghi","jkl"]
thislist.extend(mylist)
print(thislist)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#removing list items-->
thislist=["apple","banana","cherry"]
thislist.remove("apple")
print(thislist)

thislist=["apple","banana","cherry"]
thislist.pop(2)
print(thislist)

thislist=["apple","banana","cherry"]
del thislist[1]
print(thislist)

thislist=["apple","banana","cherry"]
thislist.clear()
print(thislist)

#-------------------------------------------------------------------------------------------------------------------------
#loop through a list-->

thislist=["apple","banana","cherry","pineapple"]  #using for loop
for x in range(0,4):
    print(thislist[x])

thislist=["apple","banana","cherry","pineapple"]  #using while loop
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1








