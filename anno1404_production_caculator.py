import tkinter as tk
import tkinter.font as tkFont
import math
import PIL 
from PIL import ImageTk, Image
from tkinter import IntVar
from tkinter import ttk


root = tk.Tk()

# 視窗設定
fontsize = tkFont.Font(family = "Microsoft JhengHei", size = 15)
root.title("Anno 1404 caculator")
root.resizable(0,0)
root.geometry("1200x800")
# root.configure(background = "thistle2")
root.iconbitmap(r"D:/python/python-anno1404/images/anno1404_icon.ico")

# 載入圖片
Nomads_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Nomads.png")
Envoys_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Envoys.png")
Dates_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Dates.png")
Milk_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Milk.png")
Carpets_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Carpets.png")
Coffee_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Coffee.png")
Pearl_necklaces_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Pearl_necklaces.png")
Perfume_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Perfume.png")
Marzipan_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Marzipan.png")
People_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/People.png")
House_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/House.png")
Summary_table_Orient_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Summary_table_Orient.png")
# Summary_table_Occident_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Summary_table_Occident.png")


# Tab Control
tabControl = ttk.Notebook(root)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text = "牧豬")      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text = "貴豬")      # Make second tab visible
# tabControl.pack(expand = 1, fill = "both")
tabControl.grid(row = 0, column = 0)


# Tab1控件
monty1 = ttk.LabelFrame(tab1, text = "牧豬養成計畫") # 輸入區
monty1.grid(row = 0, column = 0, padx = 8, pady = 4, sticky = "w")
monty2 = ttk.LabelFrame(tab1, text = "牧豬養成需求") # 輸出區
monty2.grid(row = 0, column = 1, rowspan = 2, padx = 8, pady = 4, sticky = "n")
monty3 = ttk.LabelFrame(tab1, text = "牧豬養成手冊") # 列表區
monty3.grid(row = 1, column = 0, padx = 8, pady = 4)


    # Tab1內部配置
    ## 輸入區(monty1) ##
    # Radio Button
Rbtn1 = tk.IntVar()
RadioP = ttk.Radiobutton(monty1, value = 1, variable = Rbtn1).grid(row = 1, column = 0, padx = 5, pady = 5)
RadioH = ttk.Radiobutton(monty1, value = 2, variable = Rbtn1).grid(row = 2, column = 0, padx = 5, pady = 5)
Nomads_RadioP = ttk.Radiobutton(monty1, value = 1, variable = Rbtn1).grid(row = 1, column = 2, padx = 5, pady = 5)
Nomads_RadioH = ttk.Radiobutton(monty1, value = 2, variable = Rbtn1).grid(row = 2, column = 2, padx = 5, pady = 5)
Envoys_RadioP = ttk.Radiobutton(monty1, value = 1, variable = Rbtn1).grid(row = 1, column = 6, padx = 5, pady = 5)
Envoys_RadioH = ttk.Radiobutton(monty1, value = 2, variable = Rbtn1).grid(row = 2, column = 6, padx = 5, pady = 5)
    
    # Separator
Separator1 = ttk.Separator(monty1, orient = "vertical").grid(row = 1, column = 1, rowspan = 2, sticky = "ns")
Separator2 = ttk.Separator(monty1, orient = "vertical").grid(row = 1, column = 5, rowspan = 2, sticky = "ns")
    
    # Input
InputNPQ = tk.IntVar()
InputNPQ.set(0)
InputNHQ = tk.IntVar()
InputNHQ.set(0)
InputEPQ = tk.IntVar()
InputEPQ.set(0)
InputEHQ = tk.IntVar()
InputEHQ.set(0)
Nomads_PQEntry = tk.Entry(monty1, font = fontsize, width = 6, bd = 3, textvariable = InputNPQ).grid(row = 1, column = 4, padx = 5, pady = 5)
Nomads_HQEntry = tk.Entry(monty1, font = fontsize, width = 6, bd = 3, textvariable = InputNHQ).grid(row = 2, column = 4, padx = 5, pady = 5)
Envoys_PQEntry = tk.Entry(monty1, font = fontsize, width = 6, bd = 3, textvariable = InputEPQ).grid(row = 1, column = 8, padx = 5, pady = 5)
Envoys_HQEntry = tk.Entry(monty1, font = fontsize, width = 6, bd = 3, textvariable = InputEHQ).grid(row = 2, column = 8, padx = 5, pady = 5)


    # Image
Nomads1 = tk.Label(monty1, image = Nomads_image, relief = "ridge").grid(row = 0, column = 2, columnspan = 2, padx = 5, pady = 5)
Envoys1 = tk.Label(monty1, image = Envoys_image, relief = "ridge").grid(row = 0, column = 6, columnspan = 2, padx = 5, pady = 5)
Nomads_PI1 = tk.Label(monty1, image = People_image, relief = "ridge").grid(row = 1, column = 3, padx = 5, pady = 5)
Nomads_HI = tk.Label(monty1, image = House_image, relief = "ridge").grid(row = 2, column = 3, padx = 5, pady = 5)
Envoys_PI1 = tk.Label(monty1, image = People_image, relief = "ridge").grid(row = 1, column = 7, padx = 5, pady = 5)
Envoys_HI = tk.Label(monty1, image = House_image, relief = "ridge").grid(row = 2, column = 7, padx = 5, pady = 5)

    # caculate1 計算牧民系統
Caculate_Orient = tk.Button(monty1, font = fontsize, text = "Go！").grid(row = 2, column = 9, padx = 5, pady = 5)

    ## 輸入區(monty1) end ##

    ## 輸出區(monty2) ##
    # 設定
Persent = ["DatesPersent", "MilkPersent", "CarpetsPersent", "CoffeePersent", "Pearl_necklacesPersent", "PerfumePersent", "MarzipanPersent"]
Persent = tk.StringVar()
ChosenValues = ["0%", "25%", "50%", "75%"]
    
    # Chosen
DatesChosen = ttk.Combobox(monty2, width = 4, textvariable = "DatesPersent", state = "readonly")
DatesChosen["values"] = ChosenValues
DatesChosen.grid(row = 0, column = 0, padx = 5, pady = 5)
DatesChosen.current(0)  # 設置初始顯示值，值為元组["values"]的下標

MilkChosen = ttk.Combobox(monty2, width = 4, textvariable = "MilkPersent", state = "readonly")
MilkChosen["values"] = ChosenValues
MilkChosen.grid(row = 1, column = 0, padx = 5, pady = 5)
MilkChosen.current(0)

CarpetsChosen = ttk.Combobox(monty2, width = 4, textvariable = "CarpetsPersent", state = "readonly")
CarpetsChosen["values"] = ChosenValues
CarpetsChosen.grid(row = 2, column = 0, padx = 5, pady = 5)
CarpetsChosen.current(0)

CoffeeChosen = ttk.Combobox(monty2, width = 4, textvariable = "CoffeePersent", state = "readonly")
CoffeeChosen["values"] = ChosenValues
CoffeeChosen.grid(row = 3, column = 0, padx = 5, pady = 5)
CoffeeChosen.current(0)

Pearl_necklacesChosen = ttk.Combobox(monty2, width = 4, textvariable = "Pearl_necklacesPersent", state = "readonly")
Pearl_necklacesChosen["values"] = ChosenValues
Pearl_necklacesChosen.grid(row = 4, column = 0, padx = 5, pady = 5)
Pearl_necklacesChosen.current(0)

PerfumeChosen = ttk.Combobox(monty2, width = 4, textvariable = "PerfumePersent", state = "readonly")
PerfumeChosen["values"] = ChosenValues
PerfumeChosen.grid(row = 5, column = 0, padx = 5, pady = 5)
PerfumeChosen.current(0)

MarzipanChosen = ttk.Combobox(monty2, width = 4, textvariable = "MarzipanPersent", state = "readonly")
MarzipanChosen["values"] = ChosenValues
MarzipanChosen.grid(row = 6, column = 0, padx = 5, pady = 5)
MarzipanChosen.current(0)

    # Image
Dates1 = tk.Label(monty2, image = Dates_image, relief = "ridge").grid(row = 0, column = 1, padx = 5, pady = 5)
Milk1 = tk.Label(monty2, image = Milk_image, relief = "ridge").grid(row = 1, column = 1, padx = 5, pady = 5)
Carpets1 = tk.Label(monty2, image = Carpets_image, relief = "ridge").grid(row = 2, column = 1, padx = 5, pady = 5)
Coffee1 = tk.Label(monty2, image = Coffee_image, relief = "ridge").grid(row = 3, column = 1, padx = 5, pady = 5)
Pearl_necklaces1 = tk.Label(monty2, image = Pearl_necklaces_image, relief = "ridge").grid(row = 4, column = 1, padx = 5, pady = 5)
Perfume1 = tk.Label(monty2, image = Perfume_image, relief = "ridge").grid(row = 5, column = 1, padx = 5, pady = 5)
Marzipan1 = tk.Label(monty2, image = Marzipan_image, relief = "ridge").grid(row = 6, column = 1, padx = 5, pady = 5)

    # Caculate Result
BuildQuantity = ["DatesBQ", "MilkBQ", "CarpetsBQ", "CoffeeBQ", "Pearl_necklacesBQ", "PerfumeBQ", "MarzipanBQ"]
BuildQuantity = IntVar()
Dates_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = "DatesBQ").grid(row = 0, column = 2, padx = 5, pady = 5)
Milk_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = "MilkBQ").grid(row = 1, column = 2, padx = 5, pady = 5)
Carpets_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = "CarpetsBQ").grid(row = 2, column = 2, padx = 5, pady = 5)
Coffee_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = "CoffeeBQ").grid(row = 3, column = 2, padx = 5, pady = 5)
Pearl_necklaces_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = "Pearl_necklacesBQ").grid(row = 4, column = 2, padx = 5, pady = 5)
Perfume_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = "PerfumeBQ").grid(row = 5, column = 2, padx = 5, pady = 5)
Marzipan_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = "MarzipanBQ").grid(row = 6, column = 2, padx = 5, pady = 5)

    ## 輸出區(monty2) end ##

    ## 列表區(monty3) ##
    # Separator
Separator3 = ttk.Separator(monty3, orient = "vertical").grid(row = 0, column = 0, rowspan = 11, sticky = "ns", padx = 2, pady = 2)
Separator4 = ttk.Separator(monty3, orient = "vertical").grid(row = 0, column = 2, rowspan = 11, sticky = "ns", padx = 2, pady = 2)
Separator5 = ttk.Separator(monty3, orient = "vertical").grid(row = 0, column = 4, rowspan = 11, sticky = "ns", padx = 2, pady = 2)
Separator6 = ttk.Separator(monty3, orient = "vertical").grid(row = 0, column = 6, rowspan = 11, sticky = "ns", padx = 2, pady = 2)
Separator7 = ttk.Separator(monty3, orient = "vertical").grid(row = 0, column = 8, rowspan = 11, sticky = "ns", padx = 2, pady = 2)
Separator8 = ttk.Separator(monty3, orient = "vertical").grid(row = 0, column = 10, rowspan = 11, sticky = "ns", padx = 2, pady = 2)
Separator9 = ttk.Separator(monty3, orient = "vertical").grid(row = 0, column = 12, rowspan = 11, sticky = "ns", padx = 2, pady = 2)
Separator10 = ttk.Separator(monty3, orient = "vertical").grid(row = 0, column = 14, rowspan = 11, sticky = "ns", padx = 2, pady = 2)
Separator11 = ttk.Separator(monty3, orient = "vertical").grid(row = 0, column = 16, rowspan = 11, sticky = "ns", padx = 2, pady = 2)
Separator12 = ttk.Separator(monty3, orient = "horizontal").grid(row = 0, column = 0, columnspan = 17, sticky = "we", padx = 2, pady = 2)
Separator13 = ttk.Separator(monty3, orient = "horizontal").grid(row = 2, column = 0, columnspan = 17, sticky = "we", padx = 2, pady = 2)
Separator14 = ttk.Separator(monty3, orient = "horizontal").grid(row = 4, column = 0, columnspan = 17, sticky = "we", padx = 2, pady = 2)
Separator15 = ttk.Separator(monty3, orient = "horizontal").grid(row = 6, column = 0, columnspan = 17, sticky = "we", padx = 2, pady = 2)
Separator16 = ttk.Separator(monty3, orient = "horizontal").grid(row = 8, column = 0, columnspan = 17, sticky = "we", padx = 2, pady = 2)
Separator17 = ttk.Separator(monty3, orient = "horizontal").grid(row = 10, column = 0, columnspan = 17, sticky = "we", padx = 2, pady = 2)

    # Lable
ND = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 450).grid(row = 3, column = 3, padx = 5, pady = 5)
NM = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 436).grid(row = 3, column = 5, padx = 5, pady = 5)
NCa = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 909).grid(row = 3, column = 7, padx = 5, pady = 5)
NPD = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 5, column = 3, padx = 5, pady = 5)
NPM = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 145).grid(row = 5, column = 5, padx = 5, pady = 5)
NPCa = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 295).grid(row = 5, column = 7, padx = 5, pady = 5)
ED = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 600).grid(row = 7, column = 3, padx = 5, pady = 5)
EM = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 666).grid(row = 7, column = 5, padx = 5, pady = 5)
ECa = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 1500).grid(row = 7, column = 7, padx = 5, pady = 5)
ECo = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 1000).grid(row = 7, column = 9, padx = 5, pady = 5)
EPN = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 751).grid(row = 7, column = 11, padx = 5, pady = 5)
EPe = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 1250).grid(row = 7, column = 13, padx = 5, pady = 5)
EMa = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 2453).grid(row = 7, column = 15, padx = 5, pady = 5)
EPD = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 9, column = 3, padx = 5, pady = 5)
EPM = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 9, column = 5, padx = 5, pady = 5)
EPCa = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 9, column = 7, padx = 5, pady = 5)
EPCo = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 9, column = 9, padx = 5, pady = 5)
EPPN = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 1040).grid(row = 9, column = 11, padx = 5, pady = 5)
EPPe = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 2600).grid(row = 9, column = 13, padx = 5, pady = 5)
EPMa = tk.Label(monty3, font = fontsize, width = 4, bd = 3, text = 4360).grid(row = 9, column = 15, padx = 5, pady = 5)

    # Image
Dates2 = tk.Label(monty3, image = Dates_image, relief = "ridge").grid(row = 1, column = 3, padx = 5, pady = 5)
Milk2 = tk.Label(monty3, image = Milk_image, relief = "ridge").grid(row = 1, column = 5, padx = 5, pady = 5)
Carpets2 = tk.Label(monty3, image = Carpets_image, relief = "ridge").grid(row = 1, column = 7, padx = 5, pady = 5)
Coffee2 = tk.Label(monty3, image = Coffee_image, relief = "ridge").grid(row = 1, column = 9, padx = 5, pady = 5)
Pearl_necklaces2 = tk.Label(monty3, image = Pearl_necklaces_image, relief = "ridge").grid(row = 1, column = 11, padx = 5, pady = 5)
Perfume2 = tk.Label(monty3, image = Perfume_image, relief = "ridge").grid(row = 1, column = 13, padx = 5, pady = 5)
Marzipan2 = tk.Label(monty3, image = Marzipan_image, relief = "ridge").grid(row = 1, column = 15, padx = 5, pady = 5)
Nomads2 = tk.Label(monty3, image = Nomads_image, relief = "ridge").grid(row = 3, column = 1, padx = 5, pady = 5)
Nomads_PI2 = tk.Label(monty3, image = People_image, relief = "ridge").grid(row = 5, column = 1, padx = 5, pady = 5)
Envoys2 = tk.Label(monty3, image = Envoys_image, relief = "ridge").grid(row = 7, column = 1, padx = 5, pady = 5)
Envoys_PI2 = tk.Label(monty3, image = People_image, relief = "ridge").grid(row = 9, column = 1, padx = 5, pady = 5)

    ## 列表區(monty3) end ##



root.mainloop()



