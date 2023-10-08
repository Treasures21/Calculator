import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


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
notebook.add(Stats, text="Stats")

Calculus = ttk.Frame(notebook)
notebook.add(Calculus, text="Calculus")



#enter data
X_axis = (34,35,36,37,38,39,40,41)
Y_axis = (1,4,13,6,9,8,9,10)



 #plot graph
def plot():
    plt.plot(X_axis, Y_axis)
    plt.scatter(X_axis, Y_axis)
    canvas.draw()

canvas = FigureCanvasTkAgg(fig, master=Stats)
canvas.get_tk_widget().pack()

#plot graph button

plot_button = tk.Button(Stats, text="plot graph", command=lambda: plot(), relief=tk.GROOVE, borderwidth=.7, padx=1, pady=1, bg = 'white')
plot_button.configure(state="normal")
plot_button.place(x=20, y=540)


toolbar = NavigationToolbar2Tk(canvas, Stats, pack_toolbar=False)
toolbar.update()
toolbar.pack()

    #mean calculator
def mean_calc():
    x_mean = np.mean(X_axis)
    emptylabel = tk.Label(Stats, text="X - axis Mean: " + str(x_mean))
    emptylabel.place(x=120, y=582)



    y_mean = np.mean(Y_axis)

    label = tk.Label(Stats, text="Y - axis Mean: " + str(y_mean))
    label.place(x=120, y=604)

    return x_mean, y_mean


print_mean = tk.Button(Stats, text = "calculate mean", command=lambda : mean_calc(), relief=tk.GROOVE, borderwidth=.7, padx=1, pady=1, bg = 'white')
print_mean.configure(state="normal")
print_mean.place(x=20, y=580)

#median calculator

def median_calc():
    x_median = np.median(X_axis)
    emptylabel = tk.Label(Stats, text="X - axis Median: " + str(x_median))
    emptylabel.place(x=120, y=624)

    y_median = np.median(Y_axis)
    label = tk.Label(Stats, text="Y - axis Median: " + str(y_median))
    label.place(x=120, y=644)

    return x_median, y_median

print_median = tk.Button(Stats, command=median_calc, text="calculate median", relief=tk.GROOVE, borderwidth=.7, padx=1, pady=1, bg = 'white')
print_median.configure(state="normal")
print_median.place(x=20, y=620)


    #standard deviation calculator
def std_calc():
    x_std = np.std(X_axis)
    emptylabel = tk.Label(Stats, text="X - axis Standard Deviation: " + str(x_std))
    emptylabel.place(x=180, y=666)

    y_std = np.std(Y_axis)
    label = tk.Label(Stats, text="Y - axis Standard Deviation: " + str(y_std))
    label.place(x=180, y=686)

    return x_std, y_std

print_std = tk.Button(Stats, command=std_calc, text="calculate standard deviation", relief=tk.GROOVE, borderwidth=.7, padx=1, pady=1, bg = 'white')
print_std.configure(state="normal")
print_std.place(x=20, y=666)

Calculator.mainloop()
