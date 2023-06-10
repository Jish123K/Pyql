import tkinter as tk

class MathProblemSolver(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        # Create the buttons

        self.add_button = tk.Button(self, text="Add", command=self.add_numbers)

        self.subtract_button = tk.Button(self, text="Subtract", command=self.subtract_numbers)

        self.multiply_button = tk.Button(self, text="Multiply", command=self.multiply_numbers)

        self.divide_button = tk.Button(self, text="Divide", command=self.divide_numbers)

        # Create the output window

        self.output_window = tk.Text(self)

        # Layout the widgets

        self.add_button.pack()

        self.subtract_button.pack()

        self.multiply_button.pack()

        self.divide_button.pack()

        self.output_window.pack()

    def add_numbers(self):

        # Get the numbers from the user

        number1 = float(self.input_number1.get())

        number2 = float(self.input_number2.get())

        # Add the numbers and print the result

        result = number1 + number2

        self.output_window.insert("end", "The sum is: " + str(result) + "\n")

    def subtract_numbers(self):

        # Get the numbers from the user

        number1 = float(self.input_number1.get())

        number2 = float(self.input_number2.get())

        # Subtract the numbers and print the result

        result = number1 - number2

        self.output_window.insert("end", "The difference is: " + str(result) + "\n")

    def multiply_numbers(self):

        # Get the numbers from the user

        number1 = float(self.input_number1.get())

        number2 = float(self.input_number2.get())

        # Multiply the numbers and print the result

        result = number1 * number2

        self.output_window.insert("end", "The product is: " + str(result) + "\n")

    def divide_numbers(self):

        # Get the numbers from the user

        number1 = float(self.input_number1.get())

        number2 = float(self.input_number2.get())

        # Divide the numbers and print the result

        result = number1 / number2

        self.output_window.insert("end", "The quotient is: " + str(result) + "\n")

if __name__ == "__main__":

    # Create the main window

    root = tk.Tk()

    # Create the math problem solver

    solver = MathProblemSolver(root)

    # Set the window title

    root.title("Math Problem Solver")

    # Start the main loop

    root.mainloop()

