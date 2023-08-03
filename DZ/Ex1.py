# ✔	Три друга взяли вещи в поход. Сформируйте словарь,
# где ключ — имя друга, а значение —кортеж вещей.
# Ответьте на вопросы:
# ✔	Какие вещи взяли все три друга
# ✔	Какие вещи уникальны, есть только у одного друга
# ✔	Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔	Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

def addFriend(group):
    name = str(input('Имя друга - '))
    scarb = tuple((str(input('Что взял в поход - '))).split(' '))
    group[name] = scarb
    return group


group = {'Максим': ('нож', 'ложка', 'тарелка', 'палатка'),
         'Саша': ('нож', 'ложка', 'тарелка', 'котелок'),
         'Сева': ('нож', 'тарелка', 'топор', 'гитара')}
print(group)

persons = group.keys()
habar = group.values()

myList = []
for key in group:
    myList.extend(list(group[key]))

notUniqueItem = set()
notHaveOne = set()
for key, value in group.items():
    for i in range(len(value)):
        if myList.count(value[i]) == 1:
            print(f'{value[i]} - уникальная вещь {key}, взял её')
        if myList.count(value[i]) == len(group):
            notUniqueItem.add(value[i])
        if myList.count(value[i]) == len(group) - 1:
            notHaveOne.add(value[i])
for key, value in group.items():
    for i in notHaveOne:
        if i not in group[key]:
            print(f'{key} не взял с собой {i}')
print(f'Есть у всех {notUniqueItem}')
