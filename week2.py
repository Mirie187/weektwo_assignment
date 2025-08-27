my_list = []

for num in (10,20,30,40):
    my_list.append(num)
print(my_list)

my_list.insert(1,15)
print(my_list)

list_two = [50,60,70]
my_list.extend(list_two)
print(my_list)

my_list.pop()
print(my_list)

my_list.sort()
position = my_list.index(30)
print ("index of valu 30: ", position)
