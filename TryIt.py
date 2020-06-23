import tkinter as tk
from tkinter import ttk

root = tk.Tk()


### RB value get ###
# Rbtn1 = tk.IntVar()
# Rbtn1.set(2)
# # Rbtn2 = tk.StringVar()
# RadioP = tk.Radiobutton(root, value = 1, variable = Rbtn1).grid(row = 1, column = 0, padx = 5, pady = 5)
# RadioH = tk.Radiobutton(root, value = 2, variable = Rbtn1).grid(row = 2, column = 0, padx = 5, pady = 5)
# x = Rbtn1.get()
# print(x)

### Entry value get ###
# InputNPQ = tk.IntVar()
# InputNPQ.set(1)
# InputNHQ = tk.IntVar()
# InputNHQ.set(0)
# InputEPQ = tk.IntVar()
# InputEPQ.set(0)
# InputEHQ = tk.IntVar()
# InputEHQ.set(0)
# Nomads_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNPQ).grid(row = 1, column = 4, padx = 5, pady = 5)
# Nomads_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNHQ).grid(row = 2, column = 4, padx = 5, pady = 5)
# Envoys_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEPQ).grid(row = 1, column = 8, padx = 5, pady = 5)
# Envoys_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEHQ).grid(row = 2, column = 8, padx = 5, pady = 5)

# x = InputNPQ.get()
# print(x)

### Combobox value get ###
# DatesPersent = tk.StringVar()
# ChosenValues = ["0%", "25%", "50%", "75%"]
# DatesChosen = ttk.Combobox(root, width = 4, textvariable = "DatesPersent", state = "readonly")
# DatesChosen["values"] = ChosenValues
# DatesChosen.grid(row = 0, column = 0, padx = 5, pady = 5)
# DatesChosen.current(1)

# x = DatesChosen.get()
# print(x)


### label text cget ###
# DatesBQ = tk.IntVar()
# Dates_BQ = tk.Label(root, width = 5, bd = 3, text = "2")
# Dates_BQ.grid(row = 0, column = 2, padx = 5, pady = 5)
# x = Dates_BQ.cget("text")
# print(x)

Caculate_Orient = tk.Button(root, text = "Go！").grid(row = 2, column = 9, padx = 5, pady = 5)



root.mainloop()
