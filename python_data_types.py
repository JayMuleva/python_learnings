"""Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""

#text_type -->
a="hello,world"
print(a)
print(type(a))

#numric_type(Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.) -->
#1)int-->
a=35
print(a)
print(type(a))

#2)float(Float, or "floating point number" is a number, positive or negative, containing one or more decimals.)-->
a=34.5
print(a)
print(type(a))

#3)complex (Complex numbers are written with a "j" as the imaginary part:)-->
a=56.2j
print(a)
print(type(a))


#type_convention-->

a=1
b="im jay"
c=8.3
d=45.9j

e=str(a) #convert from int to string
f=int(c) #convert from float to int
g=float(a) #convert from int to float
h=complex(c) #convert from float to complex

print(e)
print(f)
print(g)
print(h)

print(type(e))
print(type(f))
print(type(g))
print(type(h))


#random number-->

import random
print(random.randrange(1,10))






