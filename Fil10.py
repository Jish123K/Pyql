import tkinter as tk

from sympy import symbols, solve

import numpy as np

import matplotlib.pyplot as plt

import scipy.optimize as optimize

# Create the main window

window = tk.Tk()

# Create the graphics buttons

add_button = tk.Button(window, text="Add", command=add)

subtract_button = tk.Button(window, text="Subtract", command=subtract)

multiply_button = tk.Button(window, text="Multiply", command=multiply)

divide_button = tk.Button(window, text="Divide", command=divide)

# Create the output window

output_window = tk.Text(window, width=50, height=20)

# Place the buttons and output window in the main window

add_button.pack()

subtract_button.pack()

multiply_button.pack()

divide_button.pack()

output_window.pack()

# Define the functions that are called when the buttons are clicked

def add():

    # Get the numbers from the user

    number1 = float(input("Enter the first number: "))

    number2 = float(input("Enter the second number: "))

    # Add the numbers and print the result

    result = number1 + number2

    print(f"{number1} + {number2} = {result}")

def subtract():

    # Get the numbers from the user

    number1 = float(input("Enter the first number: "))

    number2 = float(input("Enter the second number: "))

    # Subtract the numbers and print the result

    result = number1 - number2

    print(f"{number1} - {number2} = {result}")

def multiply():

    # Get the numbers from the user

    number1 = float(input("Enter the first number: "))

    number2 = float(input("Enter the second number: "))

    # Multiply the numbers and print the result

    result = number1 * number2

    print(f"{number1} * {number2} = {result}")

def divide():

    # Get the numbers from the user

    number1 = float(input("Enter the first number: "))

    number2 = float(input("Enter the second number: "))

    # Divide the numbers and print the result

    result = number1 / number2

    print(f"{number1} / {number2} = {result}")

# Run the main loop

window.mainloop()

