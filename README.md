Got it! Here’s the updated README to reflect that the Pizza Decider is meant for individual use to help in making a random pizza choice while considering personal favorites:

---

# Pizza Decider 2000

Pizza Decider is a web application designed to help you decide which pizza to order. Instead of randomly choosing any pizza, the application allows you to input your favorite pizzas, increasing their chances of being selected through a weighted random selection process.

## Features

- **Favorite Pizzas Input**: Enter your favorite pizzas to increase their likelihood of being chosen.
- **Weighted Random Selection**: Enhances the probability of selecting a pizza from your favorites.
- **Simple Interface**: Easy-to-use interface to quickly get a pizza suggestion.

## Installation

### Prerequisites

- Docker
- Python 3.7 or higher (if running without Docker)
- pip (Python Package Installer) (if running without Docker)
- Virtualenv (optional, but recommended if running without Docker)

### Using Docker

1. Clone the repository:
    ```bash
    git clone https://github.com/maroskolarik/pizza-decider.git
    ```
2. Navigate to the project directory:
    ```bash
    cd pizza-decider
    ```
3. Build the Docker image:
    ```bash
    docker build -t pizza-decider .
    ```
4. Run the Docker container:
    ```bash
    docker run -p 5000:5000 pizza-decider
    ```
5. Open your web browser and navigate to:
    ```
    http://localhost:5000
    ```

### Manual Installation (Without Docker)

1. Clone the repository:
    ```bash
    git clone https://github.com/maroskolarik/pizza-decider.git
    ```
2. Navigate to the project directory:
    ```bash
    cd pizza-decider
    ```
3. (Optional) Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Start the development server:
    ```bash
    python app.py
    ```
6. Open your web browser and navigate to:
    ```
    http://localhost:5000
    ```

## Usage

1. Enter your favorite pizzas in the provided interface.
2. Click the button to randomly select a pizza.
3. The application will increase the probability of selecting a pizza from your favorites using weighted random selection.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them with clear messages.
    ```bash
    git commit -m "Description of changes"
    ```
4. Push your changes to your forked repository.
    ```bash
    git push origin feature-name
    ```
5. Create a pull request describing your changes.

## Contact

For any questions or suggestions, please feel free to open an issue on GitHub or contact the repository owner.

---

This README now reflects that the Pizza Decider is an individual tool to help make a random pizza choice while considering personal favorites. Let me know if there are any other adjustments needed!