list= ['SHARON', 1251, "REA", 3.14, 3+2j]
tinylist=[1251, "Pamda"]
print(list)
print(tinylist)
print(list[0])
print(list[2:4])
print(list + tinylist)
print(tinylist * 4)

my_list = [1, 2, 3]
print(id(my_list))  # Output: 140257702953728
my_list.append(4)
print(my_list)      # Output: [1, 2, 3, 4]
print(id(my_list))  # Output: 140257702953728 (Same ID)
