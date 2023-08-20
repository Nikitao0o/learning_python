from pprint import pprint as pp

def strcounter(string):
    for symbol in string:
        counter = 0
        for subsymbol in string:
            if symbol == subsymbol:
                counter += 1
        print(symbol, counter)


def strcounter(string):
    for symbol in set(string):
        counter = 0
        for subsymbol in string:
            if symbol == subsymbol:
                counter += 1
        print(symbol, counter)


def strcounter(string):
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0) +1

    for i in syms_counter:
        print(i, syms_counter[i])


strcounter('abdsadasauhucihuhc')
