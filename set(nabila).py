# data structures:
# 1. list - [array]
# 2. tuple - (tuple)
# 3. dictionary1 - {object}
# 4. set - {set}

# characteristics of Set:
#1. Indexing Impossible
#2. changing data inside of set is not possible.
#3. set cannot allow duplication of data.

#-----------------------------------------------------------------------------------------------------------------------
# How to convert list into set?

list_file= ['roti', 'nabila', 'samila', 'lamisa']
set_file= set(list_file)
print(set_file)
# again set file convert into list file like:
a = list(set(set_file))
print(a)
#_--------------------------------------------------------------------
# How to convert tuple into set
tuple = ('rose', 'camelia', 'goldmerry', 'jesmin')
set_file2= set(tuple)
print(set_file2)

# again set file convert into tuple file:
#b = tuple(set(set_file2))
#--------------------------------------------------------------------
# how to search data in set:
# if we want to fine data in set then we have to only print the data name in the set and answer will be true or false only.
set_1= {'maliha', 'sabiha', 'lamia', 'trishna'}
print('trishna' in set_1)
print('roti' in set_1)

# set cannot allow duplicat data in one set file: For example
set_2 ={ 'farhan', 'boby', 'imon', 'roti', 'farhan', 'bipa', 'roti', 'nabila'} # here farhan data is used twice but set show
print(set_2)                                                         # only one time bcz it is not allowed duplicate data in one set.

# how to add data in set?

addition_data = {'fariha', 'risha', 'shishir', 'ayash'}
addition_data.add('lamia')
print(addition_data)

# how to remove data in a set?
subtraction_data = {'jashore', 'khulna', 'dhaka', 'rajshahi', 'syhlet', 'rongpur', 'mymensingh'}
subtraction_data.remove('dhaka')
print(subtraction_data)

# concut system:
# this is a marge system of two different sets.
set_2 = {'rose', 'camelia', 'goldmerry', 'jesmin'}
set_3= {'maliha', 'sabiha', 'lamia', 'trishna'}
set_3.update(set_2)
print(set_3)

# how to remove multiple same data.
# 1st convert the list into set form cz in set multiple same data is not allowed. like

name =['nabila', 'sunny', 'aysha', 'warrisha', 'samila', 'sunny']
remove_data= list(set(name))
print(remove_data)

# print with loop through:

set_3= {'maliha', 'sabiha', 'lamia', 'trishna'}
for i in set_3:
    print(i)

# how to clear data?
set_2 = {'rose', 'camelia', 'goldmerry', 'jesmin'}
set_2.clear()
print(set_2)

set_3= {'maliha', 'sabiha', 'lamia', 'trishna'}
del set_3
print(set_3)