import tkinter as tk

root = tk.Tk()
def keyin(event):
    print(x), event.x, event.y
frame = tk.Frame(root, width=100, height=100)
frame.bind("<Button-1>", keyin)
frame.grid(row = 0, column = 0)


Rbtn1 = tk.StringVar()
# Rbtn2 = tk.StringVar()
RadioP = tk.Radiobutton(root, value = 1, variable = Rbtn1).grid(row = 1, column = 0, padx = 5, pady = 5)
RadioH = tk.Radiobutton(root, value = 2, variable = Rbtn1).grid(row = 2, column = 0, padx = 5, pady = 5)
# x = Rbtn1.get()
x = 1

InputNPQ = tk.IntVar()
InputNPQ.set(0)
InputNHQ = tk.IntVar()
InputNHQ.set(0)
InputEPQ = tk.IntVar()
InputEPQ.set(0)
InputEHQ = tk.IntVar()
InputEHQ.set(0)
Nomads_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNPQ).grid(row = 1, column = 4, padx = 5, pady = 5)
Nomads_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputNHQ).grid(row = 2, column = 4, padx = 5, pady = 5)
Envoys_PQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEPQ).grid(row = 1, column = 8, padx = 5, pady = 5)
Envoys_HQEntry = tk.Entry(root, width = 6, bd = 3, textvariable = InputEHQ).grid(row = 2, column = 8, padx = 5, pady = 5)


root.mainloop()
