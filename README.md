## Overview of Limit Calculator Code

The limit calculator offers a user-friendly interface for calculating limits of mathematical expressions. It utilizes symbolic mathematics to handle complex expressions and provides options for custom limits, graphing, and theme switching. The calculator is designed to be accessible to users with varying levels of mathematical expertise, offering a valuable tool for exploring and understanding limits in various contexts.

**Imports:**

* `tkinter as tk`: Imports the Tkinter library for creating the GUI elements.
* `sympy as sp`: Imports the SymPy library for symbolic mathematics, used to manipulate and solve mathematical expressions.
* `numpy as np`: Imports the NumPy library for numerical computations, used for plotting the expression's graph (optional).
* `from matplotlib.figure import Figure`: Imports the Figure class from Matplotlib to create the plot.
* `from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg`: Imports the FigureCanvasTkAgg class from Matplotlib to embed the plot within the Tkinter window.

**Class Definition (`LimitCalculator`):**

* This class defines the main application logic.
* `__init__(self)`: The constructor initializes the application window using Tkinter. It sets the window title, size, background color, grid layout, and various variables to store user input and internal states.
* `create_widgets(self)`: This method creates all the GUI elements within the window:
    * Labels for "Symbol," "Limit," "Expression," and "Direction."
    * Entry fields for the symbol (variable), expression, and optional custom limit value.
    * Dropdown menus for selecting the limit type ("Custom," "Infinity," "-Infinity") and direction ("both," "right," "left").
    * Buttons for "Calculate Limit," "Plot Graph," and a theme toggle button ("" or "").
    * A label to display the calculation result.

* Helper methods:
    * `add_manual_buttons(self)`: Creates buttons with mathematical symbols (log, sin, cos, etc.) that users can insert into the expression field.
    * `insert_symbol(self, symbol)`: Inserts the clicked symbol from the manual buttons into the expression entry field.
    * `check_limit_selection(self, selection)`: Shows or hides the custom limit entry field based on the selected limit type.
    * `check_entries(self)`: Enables the "Calculate Limit" button only if all required fields (symbol, expression, valid limit) have values.

* Calculation and Plotting:
    * `calculate_limit(self)`: This method handles the limit calculation:
        * Converts user input (symbol, expression, limit) into symbolic objects using SymPy.
        * Translates the chosen direction ("both," "right," "left") into the appropriate syntax for SymPy's `limit` function.
        * Calculates the limit using SymPy's `limit` function and displays the result in the label.
        * Enables the "Plot Graph" button after successful calculation.
    * `plot_graph(self)`: This method generates a plot of the expression using Matplotlib and NumPy:
        * Converts the user's expression into a Python function using SymPy's `lambdify`.
        * Defines the x-axis range and generates numerical data points for the function.
        * Creates a plot using Matplotlib's Figure and axes objects.
        * Optionally, plots a vertical line at the custom limit value (if provided).
        * Hides all widgets except the result and plot within the window.
        * Creates a "Back" button to return to the main interface after plotting.

* Theme Switching (`switch_mode(self)` and `update_theme(self, bg_color, fg_color, button_text)`):
    * These methods allow the user to switch between light and dark themes for the application's GUI.
    * They update the background and foreground colors of various widgets based on the current theme state.

* `__main__` block:
    * Creates an instance of the `LimitCalculator` class and starts the main event loop of the Tkinter application to handle user interactions.

## Using the Application

1. **Run the script:** Save the code as a Python file (e.g., `limit_calculator.py`) and execute it from the command line using `python limit_calculator.py`.
2. **Enter symbol and expression:** In the provided text fields, enter the variable name (symbol) and the mathematical expression for which you want to calculate the limit.
3. **Select limit type:** Choose the limit type from the dropdown menu ("Custom," "Infinity," or "-Infinity"). If you choose "Custom," enter the specific limit value in the additional field.
4. **Select direction (optional):** If desired, select the direction from which the limit is approached ("both," "right," or "left").
5. **Calculate limit:** This will calculate the limit.
6. **Plot Graph:** This will plot the graph.

## Mathematical Concepts Used in the Limit Calculator

The limit calculator primarily leverages symbolic mathematics to perform its calculations. Here are the key mathematical concepts employed:

* **Symbolic expressions:** The SymPy library allows users to represent mathematical expressions symbolically, using variables and operators. This enables precise manipulation and analysis of mathematical formulas.
* **Limits:** The core concept of the calculator is the calculation of limits. A limit is the value that a function approaches as its input approaches a certain value. The calculator uses SymPy's limit function to compute limits.
* **Variables and symbols:** The calculator uses variables (symbols) to represent unknown quantities within expressions. These variables can be manipulated and substituted with specific values during calculations.
* **Functions:** Mathematical functions are represented using expressions and variables. The calculator can evaluate functions at different points and determine their limits.

## Tkinter Interface

Tkinter is a Python GUI toolkit used to create the user interface for the limit calculator. It provides a set of widgets and methods for building interactive applications. Here's how Tkinter is used in the calculator:

* **Window creation:** Tkinter is used to create the main window (or frame) of the application, which contains the various GUI elements.
* **Widgets:** The calculator uses various Tkinter widgets to create the user interface elements, such as:
    * **Labels:** Used to display text information, like labels for "Symbol," "Limit," "Expression," and "Direction."
    * **Entry fields:** Allow users to input text, such as the symbol and expression.
    * **Dropdown menus:** Provide options for selecting limit type and direction.
    * **Buttons:** Trigger actions when clicked, such as calculating the limit or plotting the graph.
    * **Option menus:** Used to create dropdown menus for selecting limit type and direction.
* **Layout management:** Tkinter provides methods to arrange widgets within the window, such as grid, pack, and place, to create a visually appealing layout.
* **Event handling:** Tkinter allows you to handle user interactions, such as button clicks and text entry changes, using event handlers.
* **Other features:** Tkinter offers additional features like color customization, font selection, and window management.

By incorporating these features and enhancements, the limit calculator can become a powerful tool for students, researchers, and mathematicians, facilitating the exploration and understanding of limits in various mathematical contexts.

## Author

You can connect with the author on [LinkedIn](https://www.linkedin.com/in/anmol1701/).
