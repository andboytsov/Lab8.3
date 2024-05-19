DATABASE = {
    'Коля': 'Москва',
    'Маша': 'Санкт-Петербург',
    'Петя': 'Екатеринбург'
}

def process_friend(name, query):
    if name in DATABASE:
        if query == 'ты где?':
            return f'{name} в городе {DATABASE[name]}'
        else:
            return 'Неизвестный запрос'
    else:
        return f'У тебя нет друга по имени {name}'

print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))