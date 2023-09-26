import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np
import tkinter as tk

#enter data
X_axis = (34,35,36,37,38,39,40,41)
Y_axis = (1,4,13,6,9,8,9,10)

#plot graph
def plot():
    plt.plot(X_axis, Y_axis)
    plt.scatter(X_axis, Y_axis)
    canvas.draw()

#Tkinter gui
root = tk.Tk()
fig, ax = plt.subplots()

frame = tk.Frame(root)
label = tk.Label(frame, text="Statistics calculator")
label.config(font=("comic sans",32))
label.pack()

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar=False)
toolbar.update()
toolbar.pack()

frame.pack()

tk.Button(frame, text = "Plot graph", command = plot).pack(padx = 10, pady = 0)

#mean calculator
def mean_calc():
    x_mean = np.mean(X_axis)
    emptylabel = tk.Label(frame, text="X - axis Mean: " + str(x_mean))
    emptylabel.pack()

    y_mean = np.mean(Y_axis)

    label = tk.Label(frame, text="Y - axis Mean: " + str(y_mean))
    label.pack()

    return x_mean, y_mean


print_mean = tk.Button(frame, command=mean_calc, text="calculate mean")
print_mean.pack()

#median calculator

def median_calc():
    x_median = np.median(X_axis)
    emptylabel = tk.Label(frame, text="X - axis Median: " + str(x_median))
    emptylabel.pack()

    y_median = np.median(Y_axis)
    label = tk.Label(frame, text="Y - axis Median: " + str(y_median))
    label.pack()

    return x_median, y_median

print_median = tk.Button(frame, command=median_calc, text="calculate median")
print_median.pack()


#standard deviation calculator
def std_calc():
    x_std = np.std(X_axis)
    emptylabel = tk.Label(frame, text="X - axis Standard Deviation: " + str(x_std))
    emptylabel.pack()

    y_std = np.std(Y_axis)
    label = tk.Label(frame, text="Y - axis Standard Deviation: " + str(y_std))
    label.pack()

    return x_std, y_std

print_std = tk.Button(frame, command=std_calc, text="calculate standard deviation")
print_std.pack()

root.mainloop()