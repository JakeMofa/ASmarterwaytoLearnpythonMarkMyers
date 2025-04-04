tasks = ["email Frank", "call Sarah", "meet with", "Zach"]


#we can use pop to take an item from one of the elements
#and then save the string to a diffrent list
Shortened_Task = tasks.pop(1)
print(tasks)


print(Shortened_Task)
#we can  make a diffrent empty list from the one we took and append it to ti
task_accomplished = []

task_accomplished.append(Shortened_Task)

#you can use insert to insert into a list from a particualr task
task_accomplished.insert(1, tasks.pop(2))

print(task_accomplished)

## You can pop the first element of list y and append it to the end of list x

#Rather than this

x = []
y = y.pop(0)
x.append(y)

## we can reformat as thus
x.append(y.pop(0))

#Pop the fourth element of list y and insert it as the third element of list x.
x.insert(2, y.pop(3))


