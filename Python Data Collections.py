#list
mylist=[1,'s',3.1,9]
#methods
print(type(mylist))
print(len(mylist))
mylist.append(1)
insert(1,10)
list2=[0,]
mylist.extend(list2)
mylist.remove(3.1)
mylist.pop(1)
mylist.clear()
list3=mylist.copy()
mylist.reverse()
mylist.sort()
#slicing
print(mylist[0:2])
print(mylist[1:])
print(mylist[:3])
#membership operator in list
if 3.1 in mylist:
  print("yes")
else:
  print("no")
#tuple
# in tuple you cannot change the value nor remove any member
mytuple=(2,'one',4.56)

print(mytuple*2)
#set
myset={2,"python"}
myset.add("sukkur")
set2={0,}
myset.update(set2)
print(myset.union(set2))
print(myset.intersection(set2))
print(myset.issubset(set2))
print(myset.issuperset(set2))
#dictionary
mydictionary={1:'amara',2:5.00}
print(mydictionary)
print(mydictionary[2])
for i in mydictionary:
  print(i)
  print(mydictionary[i])
  print(i, mydictionary[i])



