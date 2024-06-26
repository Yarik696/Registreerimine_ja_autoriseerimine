﻿import random
import string

def generate_password(length=12):    #Генерирует случайный пароль заданной длины,принимает аргумент length, который по умолчанию равен 12
    #Составляет пароль из символов, включая специальные символы, цифры и буквы
    symbols0 = ".,:;!_*-+()/#¤%&"
    symbols1 = '0123456789'
    symbols2 = 'qwertyuiopasdfgjklzxcvbnm'
    symbols3 = symbols2.upper()  
    all_symbols = symbols0 + symbols1 + symbols2 + symbols3  
    symbol_list = list(all_symbols)  
    random.shuffle(symbol_list)  
    password = ''.join([random.choice(symbol_list) for _ in range(length)])  
    return password

def register(username, password, usernames, passwords):    #Регистрирует нового пользователя,
    #принимает имя пользователя(username),пароль(password),список зарегистрированных имен пользователей(usernames) и словарь паролей(passwords)
    if username in usernames:  
        print("Пользователь с таким именем уже существует")
        return False
    if password == generate_password():  
        print("Пароль не может быть сгенерирован")
        return False
    usernames.append(username)  
    passwords[username] = password  
    print("Пользователь успешно зарегистрирован")
    return True

def login(username, password, passwords):    #Авторизует пользователя,принимает имя пользователя(username),пароль(password) и словарь паролей(passwords),
    #проверяет соответствие имени пользователя и пароля из словаря паролей
    if username not in passwords:  
        print("Пользователя с таким именем не найдено")
        return False
    if passwords[username] != password: 
        print("Неверный пароль")
        return False
    print("Авторизация прошла успешно")
    return True

def change_password(username, old_password, new_password, passwords):    #Изменяет пароль пользователя
    #Принимает имя пользователя(username),текущий пароль(old_password),новый пароль(new_password) и словарь паролей(passwords)
    if username not in passwords:  
        print("Пользователя с таким именем не найдено")
        return False
    if passwords[username] != old_password:  
        print("Неверный текущий пароль")
        return False
    if new_password == generate_password():  
        print("Новый пароль не может быть сгенерирован")
        return False
    passwords[username] = new_password  
    print("Пароль успешно изменен")
    return True

def recover_password(username, passwords):    #Восстанавливает пароль пользователя
    #Принимает имя пользователя(username) и словарь паролей(passwords),генерирует новый пароль и сохраняет его в словаре паролей,заменяя старый пароль.
    if username not in passwords:  
        print("Пользователя с таким именем не найдено")
        return False
    recovered_password = generate_password()  
    passwords[username] = recovered_password  
    print(f"Новый пароль для {username}: {recovered_password}")  
    return True

