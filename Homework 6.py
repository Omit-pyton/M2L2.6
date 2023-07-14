# Створіть функцію, яка приймає рядок від користувача та записує його у файл.

def save():
    file = open("Homework 6.txt", 'w', encoding='utf-8')
    file.write(input("Enter your text: "))
    file.close()


save()
