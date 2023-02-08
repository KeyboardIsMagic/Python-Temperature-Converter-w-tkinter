import tkinter as tk
import tkinter.messagebox as messagebox

def on_convert_button_click():
    temp = temp_entry.get()
    if temp:
        temp = float(temp)
        if var.get() == 1:
            fahrenheit = (temp * 9.0/5.0 + 32.0)
            fahrenheit_label.config(text=f"{temp} Celsius = {fahrenheit:.2f} Fahrenheit")
        elif var.get() == 2:
            celsius = (temp - 32.0) * 5.0/9.0
            celsius_label.config(text=f"{temp} Fahrenheit = {celsius:.2f} Celsius")
    else:
        messagebox.showerror("Error", "Please enter temperature in the field")

def on_exit_button_click():
    root.destroy()

root = tk.Tk()
root.title("Temperature Converter")

var = tk.IntVar()

temp_label = tk.Label(root, text="Temperature:")
temp_label.grid(row=0, column=0)

temp_entry = tk.Entry(root)
temp_entry.grid(row=0, column=1)

fahrenheit_button = tk.Radiobutton(root, text='Fahrenheit', variable=var, value=1)
fahrenheit_button.grid(row=1, column=0, padx=10, pady=10)

celsius_button = tk.Radiobutton(root, text='Celsius', variable=var, value=2)
celsius_button.grid(row=1, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=on_convert_button_click)
convert_button.grid(row=2, column=0, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", command=on_exit_button_click)
exit_button.grid(row=2, column=1, padx=10, pady=10)

fahrenheit_label = tk.Label(root, text="")
fahrenheit_label.grid(row=3, column=0, columnspan=2)

celsius_label = tk.Label(root, text="")
celsius_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

