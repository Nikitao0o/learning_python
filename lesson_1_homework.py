def chekpol(string):
    if string == string[::-1]:
        print(string, end=' - ')
        return True
    else:
        print(string, end=' - ')
        return False

print(chekpol(str(input('Проверка на палиндром: '))))

