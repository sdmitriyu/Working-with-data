import csv


def write_holiday_cities(first_letter):
    visited_cities = set()
    wanted_cities = set()

    with open('travel_notes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, visited, wanted = row[0].split(',')
            if name.startswith(first_letter):
                visited_cities.update(visited.split(';'))
                wanted_cities.update(wanted.split(';'))

    all_cities = sorted(visited_cities.union(wanted_cities))
    visited_cities = ', '.join(sorted(visited_cities))
    wanted_cities = ', '.join(sorted(wanted_cities))
    not_visited_cities = ', '.join(sorted(c for c in wanted_cities if c not in visited_cities))
    next_city = sorted(not_visited_cities)[0] if not_visited_cities else None

    with open('holiday.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Посетили:', visited_cities])
        writer.writerow(['Хотят посетить:', wanted_cities])
        writer.writerow(['Никогда не были в:', not_visited_cities])
        writer.writerow(['Следующим городом будет:', next_city])


# Пример использования
# write_holiday_cities('L')