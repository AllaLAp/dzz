#Внизу кода моё дз
'''def strcounter(string):
    for symbol in string:
        counter = 0
        for sub_symbol in string:
            if symbol == sub_symbol:
                counter += 1
        print(symbol, counter)

strcounter('abcdeaa')'''

'''#Верное решение
def strcounter(string):
    for symbol in set(string):
        counter = 0
        for sub_symbol in string:
            if symbol == sub_symbol:
                counter += 1
        print(symbol, counter)

strcounter('abcdeaa')

#set - неупорядоченное множество,
#там разбиваются символы в рандомном порядке'''

'''def strcounter(string):
    syms_counter ={}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
    print(syms_counter)
strcounter('abcdeaa')'''

#Моё решённое дз:
s = input('Введите строку: ')
check = len(s) // 2
if s[:check] == s[:len(s)-check-1:-1]:
    print('True')
else:
    print('False')
