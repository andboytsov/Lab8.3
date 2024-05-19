def process_query(query):
    name, question = query.split(', ', 1)
    
    if name == 'Анфиса':
        return process_anfisa(question)
    else:
        return None

def process_anfisa(question):
    if question == 'сколько у меня друзей?':
        return 3
    elif question == 'кто все мои друзья?':
        return (f'Коля, Маша, Петя')
    elif question == 'где все мои друзья?':
        return (f'Коля: Красноярск, Маша: Москва, Петя: Санкт-Петербург')
    elif question == 'кто виноват?':
        return 'Все виноваты!'
    else:
        return None

print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
