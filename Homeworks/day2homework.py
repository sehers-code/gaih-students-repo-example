list1 = list(range(10))
list2 = list1[ : 5]
list3 = list1[5 : 10]

list3.extend(list2)
print(list3)

n = int(input('Enter a single digit number: '))
list4 = list(range(n))
for i in list4:
    if i % 2 == 0:
        print(i)
