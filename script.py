#!/usr/bin/env python3

import random
import re
import socket
import threading
import time
import sqlite3



# 1. Number classification with while loop
def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def test_classify():
    while True:
        try:
            num = int(input("Enter a number (0 to quit): "))
            if num == 0:
                break
            print(f"{num} is {classify_number(num)}")
        except ValueError:
            print("Invalid input! Enter a valid number.")


# 2. Calculate average with *args
def calculate_average(*args):
    """
    Calculate average of numbers.
    Args: Variable number of numbers
    Returns: Average as float
    """
    if not args:
        return 0
    return sum(args) / len(args)


# 3. Input validation with try-except
def get_valid_number():
    while True:
        try:
            num = float(input("Enter a number: "))
            print(f"You entered: {num}")
            return num
        except ValueError:
            print("Error: Please enter a valid number.")


# 4. File operations
def file_demo():
    names = ["Alice", "Bob", "Charlie", "Diana"]

    # Write to file
    with open('names.txt', 'w') as f:
        for name in names:
            f.write(name + '\n')

    # Read from file
    with open('names.txt', 'r') as f:
        print("Names from file:")
        for line in f:
            print(line.strip())


# 5. Temperature conversion with lambda and map
def temp_conversion():
    celsius = [0, 10, 20, 30, 100]
    fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))

    print("Celsius to Fahrenheit:")
    for c, f in zip(celsius, fahrenheit):
        print(f"{c}°C = {f}°F")


# 6. Division with exception handling
def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input types!")
        return None


# 7. Custom exception
class NegativeNumberError(Exception):
    pass


def check_positive(number):
    if number < 0:
        raise NegativeNumberError(f"Number {number} is negative!")


def test_custom_exception():
    numbers = [5, -3, 10, -1]
    for num in numbers:
        try:
            check_positive(num)
            print(f"{num} is positive")
        except NegativeNumberError as e:
            print(f"Error: {e}")


# 8. Random numbers
def random_demo():
    numbers = [random.randint(1, 100) for _ in range(10)]
    avg = sum(numbers) / len(numbers)
    print(f"Random numbers: {numbers}")
    print(f"Average: {avg:.2f}")


# 9. Regular expressions
def regex_demo():
    text = "Contact: john@email.com or mary@company.org"

    # Extract emails
    emails = re.findall(r'\b\w+@\w+\.\w+\b', text)
    print(f"Emails found: {emails}")

    # Validate date
    dates = ["2023-12-25", "invalid-date", "2024-01-01"]
    for date in dates:
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            print(f"{date}: Valid")
        else:
            print(f"{date}: Invalid")

    # Replace words
    new_text = re.sub(r'cat', 'dog', "The cat sat on the mat")
    print(f"Replaced: {new_text}")

    # Split by non-alphanumeric
    words = re.split(r'[^a-zA-Z0-9]', "hello,world!test")
    print(f"Split words: {[w for w in words if w]}")


# 10. Simple client-server
def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 12345))
        server.listen(1)
        print("Server started on port 12345")

        conn, addr = server.accept()
        conn.send(b"Hello from server!")
        conn.close()
        server.close()
    except Exception as e:
        print(f"Server error: {e}")


def start_client():
    try:
        time.sleep(1)  # Wait for server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 12345))
        message = client.recv(1024).decode()
        print(f"Client received: {message}")
        client.close()
    except Exception as e:
        print(f"Client error: {e}")


def network_demo():
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    start_client()
    server_thread.join()


# 11. API demo
def api_demo():
    print("API: Application Programming Interface")
    print("Used for communication between applications")

    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        if response.status_code == 200:
            data = response.json()
            print(f"API Response - Title: {data['title']}")
        else:
            print("API request failed")
    except Exception as e:
        print(f"API error: {e}")


# 12. SQLite demo
def sqlite_demo():
    print("SQLite Database Steps:")
    print("1. Connect to database")
    print("2. Create cursor")
    print("3. Execute SQL")
    print("4. Commit changes")
    print("5. Close connection")

    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (
                              id
                              INTEGER
                              PRIMARY
                              KEY,
                              name
                              TEXT,
                              age
                              INTEGER
                          )''')

        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("John", 25))
        conn.commit()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print(f"Database records: {rows}")

        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")


# Run all demos
if __name__ == "__main__":
    print("=== PYTHON PROGRAMMING EXAMPLES ===\n")

    print("1. Number Classification:")
    print(f"5 is {classify_number(5)}")
    print(f"-3 is {classify_number(-3)}")

    print("\n2. Calculate Average:")
    print(f"Average of 1,2,3,4,5: {calculate_average(1, 2, 3, 4, 5)}")

    print("\n3. File Operations:")
    file_demo()

    print("\n4. Temperature Conversion:")
    temp_conversion()

    print("\n5. Division Examples:")
    print(f"10 ÷ 2 = {divide_numbers(10, 2)}")
    print(f"10 ÷ 0 = {divide_numbers(10, 0)}")

    print("\n6. Custom Exception:")
    test_custom_exception()

    print("\n7. Random Numbers:")
    random_demo()

    print("\n8. Regular Expressions:")
    regex_demo()

    print("\n9. Networking:")
    network_demo()

    print("\n10. API Demo:")
    api_demo()

    print("\n11. SQLite Demo:")
    sqlite_demo()

    print("\nTo test interactive functions, call:")
    print("test_classify() - for number classification")
    print("get_valid_number() - for input validation")
