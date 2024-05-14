import random


def choose_pizza(available_pizzas, favorite_pizzas):
    weighted_pizzas = list(available_pizzas.values())
    weights = [16 if pizza in favorite_pizzas else 1 for pizza in weighted_pizzas]
    chosen_pizza = random.choices(weighted_pizzas, weights=weights, k=1)[0]
    number = next((key for key, val in available_pizzas.items() if val == chosen_pizza), None)
    return number, chosen_pizza


def get_pizza_count():
    return int(input('How many pizzas would you like? '))


def main():
    available_pizzas = {1: 'Cassa', 2: 'Syrová bomba', 3: 'Pekelníček', 4: 'Tropical',
                        5: 'Pizza Taxi', 6: 'Vegetariánska', 7: 'Western', 8: 'Labužnícka',
                        9: 'Margherita', 10: 'Svieži dych', 11: 'Študentská', 12: 'Eufória',
                        13: 'Bačov sen', 14: 'Vidiecka', 15: 'Fitness pizza', 16: 'Tuniaková',
                        17: 'Slivopizza', 18: 'Špenátová', 19: 'Kebab pizza', 20: 'Pivárska',
                        21: 'Stagioni', 22: 'Šunková', 23: 'Dubáková', 24: 'Pizza štangle'}
    favorite_pizzas = ['Slivopizza', 'Špenátová', 'Pivárska']

    print('Your favorite pizzas:')
    print('\n'.join(favorite_pizzas))

    user_input = input('Press "E" for edit the list or press "ENTER" to continue: ')

    if len(favorite_pizzas) == 0 or user_input.lower() == 'e':
        print("Select your favorite pizzas from the list below (enter the corresponding numbers separated by commas): ")
        print('\n'.join([f"{key}: {pizza}" for key, pizza in available_pizzas.items()]))
        selected_pizza_numbers = [int(num.strip()) for num in
                                  input("Enter the numbers of your favorite pizzas separated by commas: ").split(",")]
        favorite_pizzas.extend([available_pizzas[num] for num in selected_pizza_numbers if num in available_pizzas])

    pizza_count = get_pizza_count()

    if pizza_count > 1:
        print("Today's pizza choices are:")
        for _ in range(pizza_count):
            chosen_pizza = choose_pizza(available_pizzas, favorite_pizzas)
            print(f"{chosen_pizza[0]}. {chosen_pizza[1]}")
    else:
        chosen_pizza = choose_pizza(available_pizzas, favorite_pizzas)
        print(f"Today's pizza choice is:\n{chosen_pizza[0]}. {chosen_pizza[1]}")


if __name__ == "__main__":
    main()
