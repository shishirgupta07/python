
import cv2
import math
print("hello word")
print(8+5)


age=32
if(age<18):
    print("no")
else:
    print("yes")



# this is comment

''' multi 
    line
    comment
''' 


# pip install opencv-python
# used for image processing 

print("gcd of 3 and 6 is",math.gcd(3,6))

Harry=34
harry=12
print(harry)
print(Harry)
# Harry and harry both are different means case sensetive **



#type operator 
a=34
typeOfA=type(a)
print(typeOfA)






#type casting
a="34"
a=int(a)
print("string to int casting",a)

'''
b="34iaa"
b=int(b)  # string to int not possible
print(b)
'''


# string ka khel start krte he
name="harry"
print(name[3])
print(name[2:4]) # string slicing...



# strip in string
name="         shishir start and end  k space strip hote he"
print(name)
print(name.strip())
print(len(name))

var=name.lower()
print(var)
var2=name.upper()
print(var2)

var3 = name.replace('s','S')
print(var3)


names="shishir,himanshu,harsh,shiddarth"
print(names.replace(",",'\n'))




# placeHolder in python
name1="shishir"
name2="chintu"
namess="my name is {} and nick name is {}".format(name1,name2)
print(namess)


namess="my name is {1} and nick name is {0}".format(name1,name2)
print(namess)



#fstring same above concept in new version
namess=f"my name is {name1} and nick name is {name2}"
print(namess)



# operators 
a=13
b=4
print(a**b) #exponential or power operator 
print(a//b) #floor division operator 


'''
up
# alt + aero key is used for code updown
down

'''

#python collection
'''
1. list
2. tuple
3. set
4. dictionary 

'''
#list
lst=[1,2,3,4,5]
print(lst)
lst[2]=7
print(lst)


#slicing in list
var=lst[2]
print(var)
var=lst[1:3]
print(var)
print(len(lst))


# append used for add elements in the last
lst.append(344)
print(lst)


# insert is used to add in particular position 
lst.insert(3,33333)
print(lst)


# pop() function used for removing last elements from lst
# lst.remove(33333) used for remove particular input


# delete 
del lst[2]
print(lst)

# clear used for clear the lst or empty
lst.clear()
print("clear",lst)






#tuple 
a=("shishir","rajat","sanjay")
print(a)
print(type(a))
# a[0]="chintu" not allowed unchange hi rhegaaa error aayega  ese krna ho to list me change krna phle fir esa krna


#tuple to list conversion
a=list(a)
a[0]="chintu"
print(a)

#set 
s1={1,1,1,1,1,2,6,2,4,3,3,3}
print(s1)
s1.add(777) # used for single element will add 
s1.update([23,24,5,67,8,9]) # multiple elemts add kr sakte he list pass krdo
print(s1)

s1.remove(1) # remove krne k liye yadi he nhi to error


#pop(),clear(),del() bhi use hote he


#intersection, union in set



#dictionary
harrydic = {
    "name":"harry",
    "class":"4th",
    "marks":35
}
print(harrydic)
print(harrydic["marks"])


# name=input("enter your name")
# print(name + name)



# function 

def sum(a,b):
    return a+b
print(sum(2,3))

#class
class Employee:
    def __init__(self,name, salary):
        self.name=name
        self.salary=salary

harry = Employee ("harry",34)
print(harry.name)
print(harry.salary)    



