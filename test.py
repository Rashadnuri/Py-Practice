thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


 
 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if x != "a":
    newlist.append(x)

print(newlist)


newlist = []
for x in range(10):
   newlist.append(x)
   print(newlist)
   
   
newlist = [x for x in range(10)]

print(newlist)


newlist = [x for x in range(10) if x < 5]

print(newlist)

#list1 = range(10)
#for i in list1 : 
#  print(i+10)

#list1 = [2,5,6,10,11,13,16]
#list2 = []
#for i in list1: 
# if i%2 == 0:
#    list2.append(i)
#print(list2)

#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = []

#or x in fruits:
#  if 'a' not in x:
#    newlist.append(x)
#print(newlist)