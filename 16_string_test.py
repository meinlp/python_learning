print('Списки')
first = [1, 2, 3, 4, 5]
second = first
third = second.copy()
first.append(6)
print(second)
print(third)

print('Индексы')
saying = "Don't panic!"
letters = list(saying)
print(letters)
print(letters[0])   # то есть элемент списка с индексом 0 - первый элемент
print(letters[8])   # положительный индекс считается с начала
print(letters[-8])  # а отрицательный с конца

print('Диапазоны')
print(letters[0:-1:1])  # [start:stop:step]
print(letters[0:10:3])  # каждая третья до 10 не включительно
print(letters[3:])      # все, кроме первых трех
print(letters[:10])     # все, до 10 не включительно
print(letters[::2])     # каждая вторая

print('Начало и конец в диапазонах')
book = "The Hitchiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)
print(booklist[0:3])
print(''.join(booklist[0:3]))   # мы выбрали первые три символа и преобразовали их в строку
print(''.join(booklist[-6:]))   # а тут последние 6 символов