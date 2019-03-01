import random

mylist = ['A','B','C']
answer = ['1','2','3']
value = random.choice(mylist)
print (value)
input()
mylist.remove(value)
value = random.choice(mylist)
mylist.remove(value)
print (value)
input()
value = random.choice(mylist)
print(value)
mylist.remove(value)
