# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

myList = [1, 2, 3, 1, 2, 4, 5]
print(myList)
myNewList = []
for i in myList:
    if i not in myNewList:
        if myList.count(i) > 1:
            myNewList.append(int(i))
print(f"Cписок с дублирующимися элементами: {myNewList}")
