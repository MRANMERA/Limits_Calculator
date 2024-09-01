import tkinter as tk
import sympy as sp
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class LimitCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Limit Calculator')
        self.root.geometry('700x800')
        self.root.config(bg='black')
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        for i in range(10):
            self.root.grid_rowconfigure(i, weight=1)
        self.symbol_var = tk.StringVar()
        self.limit_var = tk.StringVar(value='Custom')
        self.custom_limit_var = tk.StringVar()
        self.expression_var = tk.StringVar()
        self.direction_var = tk.StringVar(value='both')
        self.create_widgets()
        self.sym = None
        self.lim = None
        self.dark_mode = True
        self.symbol_var.trace('w', lambda *args: self.check_entries())
        self.limit_var.trace('w', lambda *args: self.check_entries())
        self.expression_var.trace('w', lambda *args: self.check_entries())
        self.custom_limit_var.trace('w', lambda *args: self.check_entries())
        self.root.mainloop()
    def create_widgets(self):
        self.symbol_label = tk.Label(self.root, text='Symbol', font=('Arial', 14), bg='black', fg='white')
        self.symbol_label.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        self.symbol_text = tk.Entry(self.root, textvariable=self.symbol_var, font=('Arial', 14), bg='black', fg='white', insertbackground='white')
        self.symbol_text.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        self.limit_label = tk.Label(self.root, text='Limit', font=('Arial', 14), bg='black', fg='white')
        self.limit_label.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        self.limit_menu = tk.OptionMenu(self.root, self.limit_var, 'Custom', 'Infinity', '-Infinity', command=self.check_limit_selection)
        self.limit_menu.config(font=('Arial', 14), bg='black', fg='white')
        self.limit_menu.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')
        self.custom_limit_text = tk.Entry(self.root, textvariable=self.custom_limit_var, font=('Arial', 14), bg='black', fg='white', insertbackground='white')
        self.custom_limit_text.grid(row=2, column=1, padx=20, pady=20, sticky='nsew')
        self.custom_limit_text.grid_remove()
        self.expression_label = tk.Label(self.root, text='Expression', font=('Arial', 14), bg='black', fg='white')
        self.expression_label.grid(row=3, column=0, padx=20, pady=20, sticky='nsew')
        self.expression_text = tk.Entry(self.root, textvariable=self.expression_var, font=('Arial', 14), bg='black', fg='white', insertbackground='white')
        self.expression_text.grid(row=3, column=1, padx=20, pady=20, sticky='nsew')
        self.direction_label = tk.Label(self.root, text='Direction', font=('Arial', 14), bg='black', fg='white')
        self.direction_label.grid(row=4, column=0, padx=20, pady=20, sticky='nsew')
        self.direction_menu = tk.OptionMenu(self.root, self.direction_var, 'both', 'right', 'left')
        self.direction_menu.config(font=('Arial', 14), bg='black', fg='white')
        self.direction_menu.grid(row=4, column=1, padx=20, pady=20, sticky='nsew')
        self.buttons_frame = tk.Frame(self.root, bg='black')
        self.buttons_frame.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky='nsew')
        self.add_manual_buttons()
        self.calculate_button = tk.Button(self.root, text='Calculate Limit', command=self.calculate_limit, font=('Arial', 14), bg='black', fg='white', state='disabled')
        self.calculate_button.grid(row=6, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')
        self.result_label = tk.Label(self.root, text='Result will be displayed here', font=('Arial', 14), bg='black', fg='white', wraplength=350)
        self.result_label.grid(row=7, column=0, columnspan=2, padx=20, pady=20)
        self.plot_button = tk.Button(self.root, text='Plot Graph', command=self.plot_graph, font=('Arial', 14), bg='black', fg='white', state='disabled')
        self.plot_button.grid(row=8, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')
        self.mode_button = tk.Button(self.root, text='🌞', command=self.switch_mode, font=('Arial', 14), bg='black', fg='white')
        self.mode_button.grid(row=9, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')
    def add_manual_buttons(self):
        buttons = [
            ("log", "log()"), ("exp", "exp()"), ("sin", "sin()"),
            ("cos", "cos()"), ("tan", "tan()"), ("∞", "oo"),
            ("√", "sqrt()"), ("π", "pi"), ("e", "E"),
            ("sinh", "sinh()"), ("cosh", "cosh()"), ("tanh", "tanh()"),
            ("arcsin", "asin()"), ("arccos", "acos()"), ("arctan", "atan()")
        ]
        for i, (label, symbol) in enumerate(buttons):
            button = tk.Button(self.buttons_frame, text=label, command=lambda s=symbol: self.insert_symbol(s),
                               font=('Arial', 12), bg='black', fg='white', width=5)
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky='nsew')
    def insert_symbol(self, symbol):
        current_text = self.expression_var.get()
        self.expression_var.set(current_text + symbol)
    def check_limit_selection(self, selection):
        if selection == 'Custom':
            self.custom_limit_text.grid()
        else:
            self.custom_limit_text.grid_remove()
    def check_entries(self):
        if all([self.symbol_var.get(), self.expression_var.get(),
                self.limit_var.get() != 'Custom' or self.custom_limit_var.get()]):
            self.calculate_button.config(state='normal')
        else:
            self.calculate_button.config(state='disabled')
    def calculate_limit(self):
        try:
            self.sym = sp.Symbol(self.symbol_text.get().strip())
            expression = sp.sympify(self.expression_text.get().strip())
            limit_input = self.limit_var.get()
            if limit_input == 'Infinity':
                limit_value = sp.oo
            elif limit_input == '-Infinity':
                limit_value = -sp.oo
            else:
                limit_value = float(self.custom_limit_var.get())
            direction = self.direction_var.get()
            if direction == 'right':
                direction = '+'
            elif direction == 'left':
                direction = '-'
            else:
                direction = '+-'
            result = sp.limit(expression, self.sym, limit_value, dir=direction)
            self.result_label.config(text=f"Limit Result: {result}")
            self.plot_button.config(state='normal')  # Enable the plot button after calculation
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
            self.plot_button.config(state='disabled')
    def plot_graph(self):
        try:
            expression = sp.sympify(self.expression_var.get().strip())
            limit_value = float(self.custom_limit_var.get()) if self.limit_var.get() == 'Custom' else None
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)
            x_vals = sp.symbols('x')
            func = sp.lambdify(x_vals, expression, "numpy")
            x = np.linspace(-10, 10, 400)
            y = func(x)
            ax.plot(x, y, label=str(expression))
            if limit_value is not None:
                ax.axvline(x=limit_value, color='r', linestyle='--', label=f'Limit x={limit_value}')
            ax.legend()
            ax.set_title('Graph of Expression')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.grid(True)
            for widget in self.root.grid_slaves():
                if int(widget.grid_info()['row']) >= 6:
                    widget.grid_forget()
            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas.draw()
            canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=20, pady=20)
            self.back_button = tk.Button(self.root, text='Back', command=self.go_back, font=('Arial', 14), bg='black', fg='white')
            self.back_button.grid(row=7, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')
        except Exception as e:
            self.result_label.config(text=f"Error in plotting: {str(e)}")
    def go_back(self):
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()['row']) >= 6:  # Clear only rows after the input fields
                widget.grid_forget()
        self.result_label.grid(row=7, column=0, columnspan=2, padx=20, pady=20)
        self.plot_button.grid(row=8, column=0, columnspan=2, padx=20, pady=20)
        self.mode_button.grid(row=9, column=0, columnspan=2, padx=20, pady=20)
        self.plot_button.config(state='disabled')
    def switch_mode(self):
        if self.dark_mode:
            self.update_theme('white', 'black', '🌙')
        else:
            self.update_theme('black', 'white', '🌞')
    def update_theme(self, bg_color, fg_color, button_text):
        self.dark_mode = not self.dark_mode
        widgets = [self.symbol_label, self.limit_label, self.expression_label, self.direction_label,
                   self.result_label, self.calculate_button, self.plot_button, self.mode_button]
        for widget in widgets:
            widget.config(bg=bg_color, fg=fg_color)
        self.root.config(bg=bg_color)
        self.symbol_text.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        self.custom_limit_text.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        self.expression_text.config(bg=bg_color, fg=fg_color, insertbackground=fg_color)
        self.direction_menu.config(bg=bg_color, fg=fg_color)
        self.limit_menu.config(bg=bg_color, fg=fg_color)
        for widget in self.buttons_frame.winfo_children():
            widget.config(bg=bg_color, fg=fg_color)
        self.mode_button.config(text=button_text)
if __name__ == "__main__":
    app = LimitCalculator()
