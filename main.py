import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np
import tkinter as tk
from tkinter import ttk
from scipy.stats import norm
from sympy import *
import sympy as sp
from sympy.interactive import printing
printing.init_printing(use_latex=True)


#Tkinter gui
Calculator = tk.Tk()
Calculator.geometry("1000x800")

Calculator.title("Calculator")

fig, ax = plt.subplots()

frame = tk.Frame(Calculator)
label = tk.Label(frame, text="calculator", font=("Comic Sans MS", 32))
label.pack() 


frame.pack()

#add tabs
notebook = ttk.Notebook(Calculator)
notebook.pack(fill=tk.BOTH, expand=True)

Stats = ttk.Frame(notebook)
notebook.add(Stats, text="Statistics")

Calculus = ttk.Frame(notebook)
notebook.add(Calculus, text="Calculus")


# Nested Tab
NestedTab = ttk.Notebook(Stats)
NestedTab.pack()

BS = ttk.Frame(NestedTab)
NestedTab.add(BS, text="Basic Statistics")
NestedTab.pack(expand=1, fill="both")

ND = ttk.Frame(NestedTab)
NestedTab.add(ND, text="Normal Distribution")
NestedTab.pack(expand=1, fill="both")

# Nested Tab
NestedTab = ttk.Notebook(Calculus)
Diff = ttk.Frame(NestedTab)
NestedTab.add(Diff, text="Differential Calculus")
NestedTab.pack(expand=1, fill="both")



#enter data
def enter_data():
    X_axis = (34, 35, 36, 37, 38, 39, 40, 41)
    Y_axis = (1, 4, 13, 6, 9, 8, 9, 10)
    return X_axis, Y_axis

X_axis, Y_axis = enter_data()

#subplots
fig_bstats, ax_bstats = plt.subplots()
canvas_bstats = FigureCanvasTkAgg(fig_bstats, master=BS)
canvas_bstats.get_tk_widget().pack()

 #plot graph
def plot():
    ax_bstats.plot(X_axis, Y_axis)
    ax_bstats.scatter(X_axis, Y_axis)
    ax_bstats.set_xlabel("Graph")
    canvas_bstats.draw()

#plot graph button
plot_button = tk.Button(BS, text="plot graph", command=lambda: plot(), relief=tk.GROOVE, borderwidth=.7, padx=1, pady=1, bg = 'white')
plot_button.place(x=120, y=520)
plot_button.configure(state="normal")
plot_button.place()


#mean calculator
def mean_calc():
    x_mean = np.mean(X_axis)
    label = tk.Label(BS, text="X - axis Mean: " + str(x_mean))
    label.place(x=360, y=560)


    y_mean = np.mean(Y_axis)

    label = tk.Label(BS, text="Y - axis Mean: " + str(y_mean))
    label.place(x=360, y=580)

    return x_mean, y_mean



#median calculator

def median_calc():
    x_median = np.median(X_axis)
    label = tk.Label(BS, text="X - axis Median: " + str(x_median))
    label.place(x=360, y=600)

    y_median = np.median(Y_axis)
    label = tk.Label(BS, text="Y - axis Median: " + str(y_median))
    label.place(x=360, y=620)

    return x_median, y_median



    #standard deviation calculator
def std_calc():
    x_std = np.std(X_axis)
    x_std_rounded = np.around(x_std, 4)
    label = tk.Label(BS, text="X - axis Standard Deviation: " + str(x_std_rounded))
    label.place(x=360, y=640)

    y_std = np.std(Y_axis)
    y_std_rounded = np.around(y_std, 4)
    label = tk.Label(BS, text="Y - axis Standard Deviation: " + str(y_std_rounded))
    label.place(x=360, y=660)

    return x_std_rounded, y_std_rounded

#Buttons

toolbar = NavigationToolbar2Tk(canvas_bstats, BS, pack_toolbar=False)
toolbar.update()
toolbar.place()

mean_button = tk.Button(BS, text="Calculate Mean", command=lambda: mean_calc())
mean_button.configure(state="normal")
mean_button.place(x=120, y=560)

median_button = tk.Button(BS, text="Calculate Median", command=lambda: median_calc())
median_button.configure(state="normal")
median_button.place(x=120, y=600)

std_button = tk.Button(BS, text="Calculate Standard Deviation", command=lambda: std_calc())
std_button.configure(state="normal")
std_button.place(x=120, y=640)


#Normal Distribution

def enter_data():
    mean = 0
    std_dev = 1
    variance = np.square(std_dev)
    return mean, std_dev, variance

mean, std_dev, variance = enter_data()


# Generate x-axis values
x = np.arange(-5, 5, 0.1)

# Calculate the probability density function (PDF) of the normal distribution
pdf = np.exp(-np.square(x-mean)/2*variance) / (np.sqrt(2*np.pi*variance))

#input z value
x_input = tk.Entry(ND, justify='center')
x_input.place(x=480, y=493)

x_input_label = tk.Label(ND, text="Enter x value: ")
x_input_label.place(x=400, y=490)


# Create a subplot and canvas for the plot
fig_nd, ax = plt.subplots()
canvas_nd = FigureCanvasTkAgg(fig_nd, master=ND)
canvas_nd.get_tk_widget().pack()

def plot_nd():
    try:
        # Calculate z-score from raw data
        raw_value = float(x_input.get())
        z_value = round((raw_value - mean) / std_dev, 4)

        # Calculate probability values
        probability = round(norm.pdf(z_value, mean, std_dev), 4)
        cumulative_probability = round(norm.cdf(z_value, mean, std_dev), 4)

        # Plot normal distribution
        ax.plot(x, pdf)
        ax.axvline(x=z_value, color='r', label='Z-score: {}'.format(z_value))

        # Display z-score and z-probability and cumulative probability
        label = tk.Label(ND, text="Z-score: {}".format(z_value))
        label.place(x=450, y=580)

        label = tk.Label(ND, text="Probability Density at Z: {}".format(probability))
        label.place(x=450, y=600)

        label = tk.Label(ND, text="Cumulative Probability at Z: {}".format(cumulative_probability))
        label.place(x=450, y=620)

        ax.set_xlabel('X-axis')
        ax.set_ylabel('Probability Density')
        ax.set_title('Normal Distribution (μ = {}, σ = {})'.format(mean, std_dev))
        ax.legend()
        canvas_nd.draw()
    except ValueError:
        # Display an error message if the input is not a valid number
        error_label = tk.Label(ND, text="Invalid z-score input. Please enter a valid number.", fg='red')
        error_label.place(x=20, y=520)
        error_label.pack()

plot_button = tk.Button(ND, text="plot graph", command=lambda: plot_nd(), relief=tk.GROOVE, borderwidth=.7, padx=1, pady=1, bg = 'white')
plot_button.place(x=460, y=520)
plot_button.configure(state="normal")

label = tk.Label(ND, text="Output", font=("TkDefault", 14))
label.place(x=450, y=550)

#Differential Calculus

#input function
input_label = tk.Label(Diff, text="Enter function: ")
input_label.place(x=10, y=10)


wrt = tk.StringVar(Diff)
wrt.set("x")
wrt_label = tk.Label(Diff, text="With respect to: ")

choices = ["x", "y", "z"]
drop = ttk.Combobox(Diff, textvariable=wrt, values=choices)
drop.place(x=240, y=10)
drop.current()
drop.config(width=5)


def derivative():
    x = Symbol('wrt.get()')
    func = input.get()
    derivative = diff(func, wrt.get())
    label = tk.Label(Diff, text="Derivative: " + str(derivative))
    label.place(x=10, y=70)


input = tk.Entry(Diff, justify='center')
input.place(x=95, y=12)

button = tk.Button(Diff, text="Calculate Derivative", command=lambda: derivative())
button.place(x=10, y=40)



def plot_derv():
    func = input.get()
    derv = diff(func, wrt.get())

    # Lambdify the expressions for numerical evaluation
    func_lambda = lambdify(wrt.get(), func, 'numpy')
    derv_lambda = lambdify(wrt.get(), derv, 'numpy')

    # Generate x values for the plot
    x_values = np.linspace(-10, 10, 100)

    # Clear the previous plot and create a new one with adjusted size and position
    fig_derv, ax_derv = plt.subplots(figsize=(6, 4))
    ax_derv.plot(x_values, func_lambda(x_values), label='Function')

    # Evaluate the derivative at each x value
    derv_values = np.array([derv_lambda(x) for x in x_values])

    ax_derv.plot(x_values, derv_values, label='Derivative')

    # Add axis labels and a grid
    ax_derv.set_xlabel('X-axis')
    ax_derv.set_ylabel('Y-axis')
    ax_derv.grid(True)

    # Add x and y axes
    ax_derv.axhline(0, color='black', linewidth=0.5)
    ax_derv.axvline(0, color='black', linewidth=0.5)

    # Add legend
    ax_derv.legend()

    # Create the canvas only once and pack it
    canvas_derv = FigureCanvasTkAgg(fig_derv, master=Diff)
    canvas_derv.get_tk_widget().pack()

    # Place the canvas after packing
    canvas_derv.get_tk_widget().place(x=320, y=50, width=550, height=550)

    # Update the toolbar for interactivity
    toolbar_derv = NavigationToolbar2Tk(canvas_derv, Diff, pack_toolbar=False)
    toolbar_derv.update()
    toolbar_derv.place()




# Plot graph button for the derivative
plot_button_derv = tk.Button(Diff, text="Plot Function and Derivative", command=lambda: plot_derv(),
                             relief=tk.GROOVE, borderwidth=.7, padx=1, pady=1, bg='white')
plot_button_derv.place(x=10, y=100)
plot_button_derv.configure(state="normal")
plot_button_derv.place()

Calculator.mainloop()