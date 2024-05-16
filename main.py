import random
from data.pizzas import available_pizzas, favorite_pizzas


def choose_pizza(available, favorite):
    weights = [16 if pizza in favorite else 1 for pizza in list(available.values())]
    chosen_pizza = random.choices(list(available.values()), weights=weights, k=1)[0]

    pizza_number = 0

    for number, pizza in available.items():
        if pizza == chosen_pizza:
            pizza_number = number

    return pizza_number, chosen_pizza


def get_pizza_count():
    while True:
        try:
            user_input = int(input('How many pizzas would you like? '))
            if user_input > 0:
                return user_input
            else:
                print('Please enter a positive number.')
        except ValueError:
            print('Please enter a valid integer.')


def print_chosen_pizza():
    pizza_count = get_pizza_count()

    if pizza_count > 1:
        chosen_pizzas = []
        print('Today\'s pizza choices are:')

        for i in range(pizza_count):
            chosen_pizza = choose_pizza(available_pizzas, favorite_pizzas)
            chosen_pizzas.append(chosen_pizza)

        chosen_pizzas = sorted(chosen_pizzas)

        for i in range(len(chosen_pizzas)):
            print(f'{chosen_pizzas[i][0]}. {chosen_pizzas[i][1]}')
    else:
        chosen_pizza = choose_pizza(available_pizzas, favorite_pizzas)
        print(f'Today\'s pizza choice is:\n{chosen_pizza[0]}. {chosen_pizza[1]}')


def edit_favorite_pizzas():
    global favorite_pizzas

    user_input = input('Press "E" for edit the list or press "ENTER" to continue: ')

    if len(favorite_pizzas) == 0 or user_input.lower() == 'e':
        print('Select your favorite pizzas from the list below (enter the corresponding numbers separated by commas): ')
        print('\n'.join([f'{key}: {pizza}' for key, pizza in available_pizzas.items()]))
        selected_pizza_numbers = [int(num.strip()) for num in
                                  input('Enter the numbers of your favorite pizzas separated by commas: ').split(',')]
        favorite_pizzas = [available_pizzas[num] for num in selected_pizza_numbers if num in available_pizzas]

        print('Your new favorite pizzas:')
        print('\n'.join(favorite_pizzas))


def main():
    print('Welcome to Pizza Decider 2000!')
    print('Your favorite pizzas:')
    print('\n'.join(favorite_pizzas))

    edit_favorite_pizzas()
    print_chosen_pizza()


if __name__ == '__main__':
    main()
