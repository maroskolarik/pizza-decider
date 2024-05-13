import random


def choose_pizza(available_pizzas, favorite_pizzas):
    # Concatenate favorite pizzas to the available ones
    weighted_pizzas = list(available_pizzas.values())  

    # Assign weights to pizzas based on their presence in the favorite list
    weights = [2 if pizza in favorite_pizzas else 1 for pizza in weighted_pizzas]

    # Randomly choose a pizza with the weights applied
    chosen_pizza = random.choices(weighted_pizzas, weights=weights, k=1)[0]
    number = get_number_from_name(available_pizzas, chosen_pizza)

    return number, chosen_pizza


def get_number_from_name(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def main():
    # List of available pizzas
    available_pizzas = {1: 'Cassa', 2: 'Syrová bomba', 3: 'Pekelníček', 4: 'Tropical',
                        5: 'Pizza Taxi', 6: 'Vegetariánska', 7: 'Western', 8: 'Labužnícka',
                        9: 'Margherita', 10: 'Svieži dych', 11: 'Študentská', 12: 'Eufória',
                        13: 'Bačov sen', 14: 'Vidiecka', 15: 'Fitness pizza', 16: 'Tuniaková',
                        17: 'Slivopizza', 18: 'Špenátová', 19: 'Kebab pizza', 20: 'Pivárska',
                        21: 'Stagioni', 22: 'Šunková', 23: 'Dubáková', 24: 'Pizza štangle'}
    # List of favorite pizzas
    favorite_pizzas = ['Stagioni']

    chosen_pizza = choose_pizza(available_pizzas, favorite_pizzas)
    print(f"Today's pizza choice is: {chosen_pizza[0]}. {chosen_pizza[1]}")


if __name__ == "__main__":
    main()
