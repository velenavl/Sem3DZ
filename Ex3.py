# ✔	Создайте вручную кортеж содержащий элементы разных типов.
# ✔	Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

values = ('ama', 1.002, 12, True, [1, 2, 'hh'], 11, 9.001)
# result = {
#     'type list': [[1, 2, 'hh']],
#     'type float': [1.002, 9.001],
# }
result = {}

for value in values:
    result[type(value)] = result.get(type(value), [])
    result[type(value)].append(value)
print(result)
