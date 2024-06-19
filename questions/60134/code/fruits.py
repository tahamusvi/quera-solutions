def fruits(fruit_list):
    good_mass_range = range(300, 601)
    good_volume_range = range(100, 501)

    def is_good_fruit(fruit):
        return fruit['shape'] == 'sphere' and fruit['mass'] in good_mass_range and fruit['volume'] in good_volume_range

    good_fruits = {}
    for fruit in fruit_list:
        if is_good_fruit(fruit):
            fruit_name = fruit['name']
            good_fruits[fruit_name] = good_fruits.get(fruit_name, 0) + 1

    return good_fruits
