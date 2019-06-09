values = input("Input comma seprated numbers : ")
list1 = values.split(",")
list = []
for i in list1:
	list.append(int(i))
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
