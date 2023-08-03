# Пользователь вводит данные.
# Сделайте проверку данных и преобразуйте
# если возможно в один из вариантов ниже:
# ✔	Целое положительное число
# ✔	Вещественное положительное или отрицательное число
# ✔	Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔	Строку в нижнем регистре в остальных случаях

values = ['1', 'stre', '1.02', 'Afnfgap', '-9.2']
for value in values:
    if value.isdecimal():
        print(int(value))
    elif '.' in value:
        fraction_parts = value.split('.')
        if '-' in fraction_parts[0]:
            fraction_parts[0] = fraction_parts[0].replace('-', '')
        if (len(fraction_parts) == 2
                and fraction_parts[0].isdecimal()
                and fraction_parts[1].isdecimal()):
            print(float(value))
    elif value != value.lower():
        print(value.lower())
    else:
        print(value.upper())
