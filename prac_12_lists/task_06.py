print("Программа проверяет является ли введенное слово палиндромом")

word = input("Введите слово: ")
lst_word = list(word)
reverse_lst_word = lst_word[::-1]

if lst_word == reverse_lst_word:
    print("Это палиндром")
else:
    print("Не палиндром")
