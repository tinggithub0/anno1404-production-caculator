import tkinter as tk
import tkinter.font as tkFont
import math
from tkinter import ttk
import time
import base64
from Nomads_png import img as Nomads
import os

root = tk.Tk()
# Nomads_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Nomads.png")
# Nomads1 = tk.Label(root, image = Nomads_image, relief = "ridge")
# Nomads1.grid(row = 0, column = 2, columnspan = 2, padx = 5, pady = 5)


with open("Nomads.png", mode = "wb") as file:
    file.write(base64.b64decode(Nomads))
    
Nomads_image = tk.PhotoImage(file = "Nomads.png")
Nomads1 = tk.Label(root, image = Nomads_image, relief = "ridge")
Nomads1.grid(row = 0, column = 2, columnspan = 2, padx = 5, pady = 5)

os.remove("Nomads.png") 


# tmp = open("Nomads.png", "wb")        #创建临时的文件
# tmp.write(base64.b64decode(Nomads))    ##把这个one图片解码出来，写入文件中去。
# tmp.close()     
# image = Nomads
# image.show()

# Nomads1 = tk.Label(root, image = Nomads_image, relief = "ridge")

root.mainloop()