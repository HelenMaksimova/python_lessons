# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_str = input('Введите несколько слов, разделённых пробелами:')

print(f'Вы ввели: "{user_str}"')

user_list = enumerate(user_str.split(' '), 1)

for idx, elem in user_list:
    print(idx, elem[:10])
