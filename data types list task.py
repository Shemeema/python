#LIST

#1.creatingand accessing list

fruits = ["apple","banana","cherry"]
print(fruits[1])

#2.appending and removing elements

fruits.append("orange")
fruits.remove("banana")
print(fruits)

#slicing a list

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[:5])

#list comprehension

squares=[x**2 for x in [1,2,3,4,5,6,7,8,9,10]]
print(squares)







#TUPLE

#creating and accessing a tuple

colors=("red","green","blue")
print(colors[0])

#unpacking a tuple
(color1 ,color2, color3) =colors
print(color1)
print(color2)
print(color3)

#tuple method

tuple1=(3,6,3,7,4,5,7,0,9,8,4,5,0,3,2,3,5,7)
print(tuple1.count(3))



#SET

#creating and accessing a set

unique_numbers={1,2,3,4}
unique_numbers.add(5)
print(unique_numbers)

#union and intersection

a={1,2,3}
b={3,4,5}
d=a.union(b)
print(d)

e=a.intersection(b)
print(e)

#set comprehension

sqrs={x**2 for x in (1,2,3,4,5)}
print(sqrs)




#DICTIONARY 

#creating accessing a dictionary

students = {'name':'john','age':20,'grade':'A'}
a=students.get('grade')
print(a)

#update and remove

students.update({'grade':'A+'})
print(students)

# students.pop('age')
# print(students)

#iterating over

for i in students.keys():                            
    print(i)

#dictionary comprehension

numbers ={x:x**2 for x in (1,2,3,4,5)}
print(numbers)