def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    total_duration = sum(listened)
    minutes = total_duration // 60
    seconds = total_duration % 60
    return (f'Вы прослушали {len(listened)} песен общей продолжительностью {minutes} минут {seconds} секунд.')

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))