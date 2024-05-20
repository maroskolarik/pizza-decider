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

## Contact

For any questions or suggestions, please feel free to open an issue on GitHub or contact the repository owner.