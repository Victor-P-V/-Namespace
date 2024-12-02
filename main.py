calls = 0 # 1)Создать переменную calls = 0 вне функций.
def count_calls (): # 2) Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
    global calls
    calls+=1
def string_info (string): # 3) Создать функцию string_info с параметром string и реализовать логику работы по описанию.
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search): # 4) Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
# Вывод результата
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)
