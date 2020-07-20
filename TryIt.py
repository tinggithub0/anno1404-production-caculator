import tkinter as tk
from tkinter import *
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
# def Go():
#     print(MilkChosen.current()*0.25+1)
#     print(MilkChosen.get())

# Persent = ["DatesPersent", "MilkPersent", "CarpetsPersent", "CoffeePersent", "Pearl_necklacesPersent", "PerfumePersent", "MarzipanPersent"]
# Persent = tk.IntVar()
# ChosenValues = ["0%", "25%", "50%", "75%"]
# DatesChosen = ttk.Combobox(root, width = 4, textvariable = "DatesPersent", state = "readonly")
# DatesChosen["values"] = ChosenValues
# DatesChosen.grid(row = 0, column = 0, padx = 5, pady = 5)
# DatesChosen.current(0)
# MilkChosen = ttk.Combobox(root, width = 4, textvariable = "MilkPersent", state = "readonly")
# MilkChosen["values"] = ChosenValues
# MilkChosen.grid(row = 1, column = 0, padx = 5, pady = 5)
# MilkChosen.current(0)

# Caculate_Orient = tk.Button(root, text = "Go！", command = Go).grid(row = 2, column = 9, padx = 5, pady = 5)




### label text cget ###
# DatesBQ = tk.IntVar()
# Dates_BQ = tk.Label(root, width = 5, bd = 3, text = "2")
# Dates_BQ.grid(row = 0, column = 2, padx = 5, pady = 5)
# x = Dates_BQ.cget("text")
# print(x)



### PQ.HQ convert ###
# def convert(InputNHQ):
#     InputNPQ.set((InputNHQ.get())*15)
#     # print(InputNPQ)

# InputNPQ = tk.IntVar()
# InputNPQ.set(1)
# InputNHQ = tk.IntVar()
# InputNHQ.set(0)
# InputNHQ.trace("w", lambda name, index, mode, InputNHQ = InputNHQ: convert(InputNHQ))
# InputEPQ = tk.IntVar()
# InputEPQ.set(0)
# InputEHQ = tk.IntVar()
# InputEHQ.set(0)
# Nomads_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNPQ).grid(row = 1, column = 4, padx = 5, pady = 5)
# Nomads_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNHQ).grid(row = 2, column = 4, padx = 5, pady = 5)
# Envoys_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEPQ).grid(row = 1, column = 8, padx = 5, pady = 5)
# Envoys_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEHQ).grid(row = 2, column = 8, padx = 5, pady = 5)

# Caculate_Orient = tk.Button(root, text = "Go！").grid(row = 2, column = 9, padx = 5, pady = 5)



### PQ.HQ convert by Radiobutton ###
# def convert0(Rbtn1):
#     Rbtn1 = Rbtn1.get()
#     # print(Rbtn1)

# Rbtn1 = tk.IntVar()
# # Rbtn1.set(1)
# RadioP = tk.Radiobutton(root, value = 1, variable = Rbtn1).grid(row = 1, column = 0, padx = 5, pady = 5)
# RadioH = tk.Radiobutton(root, value = 2, variable = Rbtn1).grid(row = 2, column = 0, padx = 5, pady = 5)
# Rbtn1.trace("w", lambda name, index, mode, Rbtn1 = Rbtn1: convert0(Rbtn1))

# def convert(*args):
#     if Rbtn1.get() == 1:
#         InputNHQ.set((InputNPQ.get())/15)
#         # print(Rbtn1.get())
#     else:
#         InputNPQ.set((InputNHQ.get())*15)
#         # print(Rbtn1.get())

# InputNPQ = tk.IntVar()
# InputNPQ.set(0)
# InputNPQ.trace("w", lambda name, index, mode, InputNPQ = InputNPQ: convert(InputNPQ))
# InputNHQ = tk.IntVar()
# InputNHQ.set(0)
# InputNHQ.trace("w", lambda name, index, mode, InputNHQ = InputNHQ: convert(InputNHQ))
# InputEPQ = tk.IntVar()
# InputEPQ.set(0)
# InputEHQ = tk.IntVar()
# InputEHQ.set(0)
# Nomads_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNPQ).grid(row = 1, column = 4, padx = 5, pady = 5)
# Nomads_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNHQ).grid(row = 2, column = 4, padx = 5, pady = 5)
# Envoys_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEPQ).grid(row = 1, column = 8, padx = 5, pady = 5)
# Envoys_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEHQ).grid(row = 2, column = 8, padx = 5, pady = 5)



### button command ###
# def Caculate_Orient_Go():
#     NPQG = int(InputNPQ.get())
#     EPQG = int(InputEPQ.get())
#     DC = (DatesChosen.current() * 0.25 + 1)
#     MC = (MilkChosen.current() * 0.25 + 1)
#     DatesBQ.set(((round((NPQG / 450), 2)) + (round((EPQG / 600), 2))) / DC)
#     MilkBQ.set(((round((NPQG / 436), 2)) + (round((EPQG / 666), 2))) / MC)

#     ## 輸入區(monty1) ##
#     # Radio Button
# def convert0(Rbtn1):
#     Rbtn1 = Rbtn1.get()

# Rbtn1 = tk.IntVar()
# RadioP = ttk.Radiobutton(root, value = 1, variable = Rbtn1).grid(row = 1, column = 0, padx = 5, pady = 5)
# RadioH = ttk.Radiobutton(root, value = 2, variable = Rbtn1).grid(row = 2, column = 0, padx = 5, pady = 5)
# Nomads_RadioP = ttk.Radiobutton(root, value = 1, variable = Rbtn1).grid(row = 1, column = 2, padx = 5, pady = 5)
# Nomads_RadioH = ttk.Radiobutton(root, value = 2, variable = Rbtn1).grid(row = 2, column = 2, padx = 5, pady = 5)
# Envoys_RadioP = ttk.Radiobutton(root, value = 1, variable = Rbtn1).grid(row = 1, column = 6, padx = 5, pady = 5)
# Envoys_RadioH = ttk.Radiobutton(root, value = 2, variable = Rbtn1).grid(row = 2, column = 6, padx = 5, pady = 5)
# Rbtn1.trace("w", lambda name, index, mode, Rbtn1 = Rbtn1: convert0(Rbtn1))

#     # Input  
#         # PQ.HQ convert by Radiobutton def
# def convert(*args):
#     if Rbtn1.get() == 1:
#         InputNHQ.set((InputNPQ.get())/15)
#         InputEHQ.set((InputEPQ.get())/15)
#     else:
#         InputNPQ.set((InputNHQ.get())*15)
#         InputEPQ.set((InputEHQ.get())*15)

# InputNPQ = tk.IntVar()
# InputNPQ.set(0)
# InputNPQ.trace("w", lambda name, index, mode, InputNPQ = InputNPQ: convert(InputNPQ))
# InputNHQ = tk.IntVar()
# InputNHQ.set(0)
# InputNHQ.trace("w", lambda name, index, mode, InputNHQ = InputNHQ: convert(InputNHQ))
# InputEPQ = tk.IntVar()
# InputEPQ.set(0)
# InputEPQ.trace("w", lambda name, index, mode, InputEPQ = InputEPQ: convert(InputEPQ))
# InputEHQ = tk.IntVar()
# InputEHQ.set(0)
# InputEHQ.trace("w", lambda name, index, mode, InputEHQ = InputEHQ: convert(InputEHQ))
# Nomads_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNPQ).grid(row = 1, column = 4, padx = 5, pady = 5)
# Nomads_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNHQ).grid(row = 2, column = 4, padx = 5, pady = 5)
# Envoys_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEPQ).grid(row = 1, column = 8, padx = 5, pady = 5)
# Envoys_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEHQ).grid(row = 2, column = 8, padx = 5, pady = 5)

#     ## 輸出區(monty2) ##  
#     # 設定
# Persent = ["DatesPersent", "MilkPersent", "CarpetsPersent", "CoffeePersent", "Pearl_necklacesPersent", "PerfumePersent", "MarzipanPersent"]
# Persent = tk.StringVar()
# ChosenValues = ["0%", "25%", "50%", "75%"]
    
#     # Chosen
# DatesChosen = ttk.Combobox(root, width = 4, textvariable = "DatesPersent", state = "readonly")
# DatesChosen["values"] = ChosenValues
# DatesChosen.grid(row = 0, column = 0, padx = 5, pady = 5)
# DatesChosen.current(3)  # 設置初始顯示值，值為元组["values"]的下標

# MilkChosen = ttk.Combobox(root, width = 4, textvariable = "MilkPersent", state = "readonly")
# MilkChosen["values"] = ChosenValues
# MilkChosen.grid(row = 1, column = 0, padx = 5, pady = 5)
# MilkChosen.current(0)

#     # Caculate Result
# DatesBQ = tk.StringVar()
# Dates_BQ = tk.Label(root, width = 15, bd = 3, textvariable = DatesBQ, relief = "ridge").grid(row = 10, column = 10, padx = 5, pady = 5)
# MilkBQ = tk.StringVar()
# Milk_BQ = tk.Label(root, width = 15, bd = 3, textvariable = MilkBQ, relief = "ridge").grid(row = 10, column = 11, padx = 5, pady = 5)

#     # caculate1 計算牧民系統
# Caculate_Orient = tk.Button(root, text = "Go！", command = Caculate_Orient_Go).grid(row = 2, column = 9, padx = 5, pady = 5)




root.mainloop()
