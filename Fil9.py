import tkinter as tk

import numpy as np

import sympy as sym

import matplotlib.pyplot as plt

import scipy.integrate as integrate

class MathSolver(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        # Create the graphics buttons

        self.add_button = tk.Button(self, text="Add", command=self.add)

        self.subtract_button = tk.Button(self, text="Subtract", command=self.subtract)

        self.multiply_button = tk.Button(self, text="Multiply", command=self.multiply)

        self.divide_button = tk.Button(self, text="Divide", command=self.divide)

        # Create the output window

        self.output_window = tk.Text(self, width=50, height=20)

        # Layout the graphics buttons and output window

        self.add_button.grid(row=0, column=0)

        self.subtract_button.grid(row=1, column=0)

        self.multiply_button.grid(row=2, column=0)

        self.divide_button.grid(row=3, column=0)

        self.output_window.grid(row=0, column=1, sticky="nsew")

        # Bind the graphics buttons to their respective functions

        self.add_button.bind("<Button-1>", self.add)

        self.subtract_button.bind("<Button-1>", self.subtract)

        self.multiply_button.bind("<Button-1>", self.multiply)

        self.divide_button.bind("<Button-1>", self.divide)

    def add(self, event):

        # Get the input numbers from the user

        number1 = float(input("Enter the first number: "))

        number2 = float(input("Enter the second number: "))

        # Add the numbers and display the result in the output window

        result = number1 + number2

        self.output_window.insert("end", "{} + {} = {}".format(number1, number2, result))

    def subtract(self, event):

        # Get the input numbers from the user

        number1 = float(input("Enter the first number: "))

        number2 = float(input("Enter the second number: "))

        # Subtract the numbers and display the result in the output window

        result = number1 - number2

        self.output_window.insert("end", "{} - {} = {}".format(number1, number2, result))

    def multiply(self, event):

        # Get the input numbers from the user

        number1 = float(input("Enter the first number: "))

        number2 = float(input("Enter the second number: "))

        # Multiply the numbers and display the result in the output window

        result = number1 * number2

        self.output_window.insert("end", "{} * {} = {}".format(number1, number2, result))

    def divide(self, event):

        # Get the input numbers from the user

        number1 = float(input("Enter the first number: "))

        number2 = float(input("Enter the second number: "))

        # Divide the numbers and display the result in the output window

        result = number1 / number2

        self.output_window.insert("end", "{} / {} = {}".format(number1, number2, result))

if __name__ == "__main__":

    root = tk.Tk()

    math_solver = MathSolver(root)

    root.mainloop()

