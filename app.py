from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

available_pizzas = {
    1: 'Cassa', 2: 'Syrová bomba', 3: 'Pekelníček', 4: 'Tropical',
    5: 'Pizza Taxi', 6: 'Vegetariánska', 7: 'Western', 8: 'Labužnícka',
    9: 'Margherita', 10: 'Svieži dych', 11: 'Študentská', 12: 'Eufória',
    13: 'Bačov sen', 14: 'Vidiecka', 15: 'Fitness pizza', 16: 'Tuniaková',
    17: 'Slivopizza', 18: 'Špenátová', 19: 'Kebab pizza', 20: 'Pivárska',
    21: 'Stagioni', 22: 'Šunková', 23: 'Dubáková', 24: 'Pizza štangle'
}

favorite_pizzas = []


def choose_pizza(available, favorite):
    weights = [4 if pizza in favorite else 1 for pizza in available.values()]
    chosen_pizza = random.choices(list(available.values()), weights=weights, k=1)[0]

    pizza_number = 0
    for number, pizza in available.items():
        if pizza == chosen_pizza:
            pizza_number = number

    return pizza_number, chosen_pizza


@app.route('/')
def index():
    return render_template('index.html', favorite_pizzas=favorite_pizzas)


@app.route('/edit', methods=['GET', 'POST'])
def edit_favorite_pizzas():
    if request.method == 'POST':
        selected_pizzas = request.form.getlist('favorite_pizzas')
        global favorite_pizzas
        favorite_pizzas = [available_pizzas[int(pizza)] for pizza in selected_pizzas]
        return redirect(url_for('index'))

    return render_template('edit.html', available_pizzas=available_pizzas)


@app.route('/choose', methods=['POST'])
def print_chosen_pizza():
    try:
        pizza_count = int(request.form['pizza_count'])
    except ValueError:
        pizza_count = 1

    if pizza_count < 1:
        pizza_count = 1

    chosen_pizzas = [choose_pizza(available_pizzas, favorite_pizzas) for _ in range(pizza_count)]
    chosen_pizzas = sorted(chosen_pizzas)

    return render_template('chosen.html', chosen_pizzas=chosen_pizzas)


if __name__ == '__main__':
    app.run(debug=False)
