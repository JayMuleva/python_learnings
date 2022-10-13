a="hello,world!"  #single line string
print(a)

##multiline string-->
b="""hello i am jay     
i live in village siwai
my father is farmer"""
print(b)

#slicing string(You can return a range of characters by using the slice syntax.)-->
a="hello,world!"
print(a[2:8])


##modify strings-->
#1)upper case(The upper() method returns the string in upper case:)-->
a="this is demo"
print(a.upper())

#2)lower case(The lower() method returns the string in lower case:)-->
a="this is DEMO"
print(a.lower())

#3)remove whitespac(The strip() method removes any whitespace from the beginning or the end:)-->
a="   hello ,  world !   "
print(a.strip())

#4)replace string(The replace() method replaces a string with another string:)-->
a="hwllo , world!"
print(a.replace("w","e"))

##concatenation of string(To concatenate, or combine, two strings you can use the + operator.)-->
a='hello,'
b="world"
c=a+b
print(c)





