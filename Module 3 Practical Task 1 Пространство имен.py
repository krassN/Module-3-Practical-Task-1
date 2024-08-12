calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result


print(string_info('Capybara'))


def is_contains(string, list_to_search):
    count_calls()
    string.lower()
    new_list_to_search = [x.lower() for x in list_to_search]
    
    if string.lower() in new_list_to_search:
        return True
    else:
        return False


print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
