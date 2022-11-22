# Set (Listas)
#     Similar a listas, mas não aceita valores duplicadoos e não tem índice.

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 60, 80]

num1 = set(list1)
print(num1)

num2 = set(list2)
print(num2)


print(num1 | num2) # | = união
print(num1 - num2) # diferença
print(num1 & num2) # & = interseção
print(num1 ^ num2) # ^ = diferença simétrica
print(len(num1))

s1 = {1, 2, 3, 4, 5}
print(type(s1))

s1.add(7)
s1.update([8, 9])
s1.remove(3) #gera umerro se não encontrar o valor
s1.discard(4)

print(s1)

set1 = {"a", "b", "c", "d", "e"}
set2 = {"a", "d", "e", "f", "g"}
set3 = {"a", "i", "j", "b", "l"}

set4 = set1.union(set2)
print(set4)

set4 = set1.intersection(set2)
print(set4)

set4 = set1.difference(set2)
print(set4)

set4 = set1.symmetric_difference(set2)
print(set4)
