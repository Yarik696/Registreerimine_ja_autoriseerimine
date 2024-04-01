import MyModule

usernames = []
passwords = {}

while True:
    print("1. Регистрация")
    print("2. Авторизация")
    print("3. Изменение пароля")
    print("4. Восстановление пароля")
    print("5. Выход")

    choice = input("Выберите опцию: ")

    if choice == "1":  
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        if MyModule.register(username, password, usernames, passwords):
            continue

    elif choice == "2":   
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        if MyModule.login(username, password, passwords):
            continue

    elif choice == "3":   
        username = input("Введите имя пользователя: ")
        old_password = input("Введите текущий пароль: ")
        new_password = input("Введите новый пароль: ")
        MyModule.change_password(username, old_password, new_password, passwords)

    elif choice == "4":   
        username = input("Введите имя пользователя: ")
        MyModule.recover_password(username, passwords)

    elif choice == "5":  
        break

    else:
        print("Неверный выбор")


