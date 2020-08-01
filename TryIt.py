import tkinter as tk
import tkinter.font as tkFont
import math
from tkinter import ttk
import time


root = tk.Tk()

# 視窗設定
fontsize = tkFont.Font(family = "Microsoft JhengHei", size = 15)
root.title("Anno 1404 caculator")
root.resizable(0,0)
root.geometry("1000x700")
# root.configure(background = "thistle2")
root.iconbitmap(r"D:/python/python-anno1404/images/anno1404_icon.ico")

# 載入圖片
    # 貴豬
Begger_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Begger.png")
Peasants_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Peasants.png")
Citizens_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Citizens.png")
Patrician_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Patrician.png")
Nobleman_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Nobleman.png")
Fish = tk.PhotoImage(file = "D:/python/python-anno1404/images/Fish.png")
Cider = tk.PhotoImage(file = "D:/python/python-anno1404/images/Cider.png")
Spices = tk.PhotoImage(file = "D:/python/python-anno1404/images/Spices.png")
Linen_garments = tk.PhotoImage(file = "D:/python/python-anno1404/images/Linen_garments.png")
Bread = tk.PhotoImage(file = "D:/python/python-anno1404/images/Bread.png")
Beer = tk.PhotoImage(file = "D:/python/python-anno1404/images/Beer.png")
Leather_jerkins = tk.PhotoImage(file = "D:/python/python-anno1404/images/Leather_jerkins.png")
Books = tk.PhotoImage(file = "D:/python/python-anno1404/images/Books.png")
Meat = tk.PhotoImage(file = "D:/python/python-anno1404/images/Meat.png")
Fur_coats = tk.PhotoImage(file = "D:/python/python-anno1404/images/Fur_coats.png")
Wine = tk.PhotoImage(file = "D:/python/python-anno1404/images/Wine.png")
Glasses = tk.PhotoImage(file = "D:/python/python-anno1404/images/Glasses.png")
Candlestick = tk.PhotoImage(file = "D:/python/python-anno1404/images/Candlestick.png")
Brocade_robes = tk.PhotoImage(file = "D:/python/python-anno1404/images/Brocade_robes.png")

# 待刪!!!
People_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/People.png")
House_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/House.png")
    
# Create ToolTip


# button command


# Tab Control
tabControl = ttk.Notebook(root)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text = "牧豬")      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text = "貴豬")      # Make second tab visible
tabControl.grid(row = 0, column = 0)


#####     貴豬區     #####

# Tab2控件
monty01 = ttk.LabelFrame(tab2, text = "貴豬養成計畫") # 輸入區
monty01.grid(row = 0, column = 0, padx = 8, pady = 4, sticky = "w")
monty02 = ttk.LabelFrame(tab2, text = "貴豬養成需求") # 輸出區
monty02.grid(row = 0, column = 1, rowspan = 2, padx = 8, pady = 4, sticky = "n")
monty02 = ttk.LabelFrame(tab2, text = "貴豬養成手冊") # 列表區
monty02.grid(row = 1, column = 0, padx = 8, pady = 4)


    # Tab2內部配置
    ## 輸入區(monty4) ##
    # Radio Button
def convert01(Rbtn01):
    Rbtn01 = Rbtn01.get()

Rbtn01 = tk.IntVar()
Rbtn01.set(2)
RadioP = ttk.Radiobutton(monty01, value = 1, variable = Rbtn01).grid(row = 1, column = 0)
RadioH = ttk.Radiobutton(monty01, value = 2, variable = Rbtn01).grid(row = 2, column = 0)
Begger_RadioP = ttk.Radiobutton(monty01, value = 1, variable = Rbtn01).grid(row = 1, column = 2)
Begger_RadioH = ttk.Radiobutton(monty01, value = 2, variable = Rbtn01).grid(row = 2, column = 2)
Peasants_RadioP = ttk.Radiobutton(monty01, value = 1, variable = Rbtn01).grid(row = 1, column = 6)
Peasants_RadioH = ttk.Radiobutton(monty01, value = 2, variable = Rbtn01).grid(row = 2, column = 6)
Citizens_RadioP = ttk.Radiobutton(monty01, value = 1, variable = Rbtn01).grid(row = 1, column = 10)
Citizens_RadioH = ttk.Radiobutton(monty01, value = 2, variable = Rbtn01).grid(row = 2, column = 10)
Patrician_RadioP = ttk.Radiobutton(monty01, value = 1, variable = Rbtn01).grid(row = 1, column = 14)
Patrician_RadioH = ttk.Radiobutton(monty01, value = 2, variable = Rbtn01).grid(row = 2, column = 14)
Nobleman_RadioP = ttk.Radiobutton(monty01, value = 1, variable = Rbtn01).grid(row = 1, column = 18)
Nobleman_RadioH = ttk.Radiobutton(monty01, value = 2, variable = Rbtn01).grid(row = 2, column = 18)
Rbtn01.trace("w", lambda name, index, mode, Rbtn01 = Rbtn01: convert2(Rbtn01))


    # Separator
Separator1 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 1, rowspan = 2, sticky = "ns")
Separator2 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 5, rowspan = 2, sticky = "ns")
Separator3 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 9, rowspan = 2, sticky = "ns")
Separator4 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 13, rowspan = 2, sticky = "ns")
Separator5 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 17, rowspan = 2, sticky = "ns")


    # Input  
        # PQ.HQ convert by Radiobutton def
def convert02(*args):
    try:
        if Rbtn01.get() == 1:
            InputBgHQ.set((InputBgPQ.get())/15)
            InputPsHQ.set((InputPsPQ.get())/15)
            InputCzHQ.set((InputCzPQ.get())/15)
            InputPaHQ.set((InputPaPQ.get())/15)
            InputNbHQ.set((InputNbPQ.get())/15)
        else:
            InputBgPQ.set((InputBgHQ.get())*15)
            InputPsPQ.set((InputPsHQ.get())*15)
            InputCzPQ.set((InputCzHQ.get())*15)
            InputPaPQ.set((InputPaHQ.get())*15)
            InputNbPQ.set((InputNbHQ.get())*15)
    except Exception:
        time.sleep(0.01)

InputBgPQ = tk.IntVar()
InputBgPQ.set(0)
InputBgPQ.trace("w", lambda name, index, mode, InputBgPQ = InputBgPQ: convert02(InputBgPQ))
InputBgHQ = tk.IntVar()
InputBgHQ.set(0)
InputBgHQ.trace("w", lambda name, index, mode, InputBgHQ = InputBgHQ: convert02(InputBgHQ))
InputPsPQ = tk.IntVar()
InputPsPQ.set(0)
InputPsPQ.trace("w", lambda name, index, mode, InputPsPQ = InputPsPQ: convert02(InputPsPQ))
InputPsHQ = tk.IntVar()
InputPsHQ.set(0)
InputPsHQ.trace("w", lambda name, index, mode, InputPsHQ = InputPsHQ: convert02(InputPsHQ))
InputCzPQ = tk.IntVar()
InputCzPQ.set(0)
InputCzPQ.trace("w", lambda name, index, mode, InputCzPQ = InputCzPQ: convert02(InputCzPQ))
InputCzHQ = tk.IntVar()
InputCzHQ.set(0)
InputCzHQ.trace("w", lambda name, index, mode, InputCzHQ = InputCzHQ: convert02(InputCzHQ))
InputPaPQ = tk.IntVar()
InputPaPQ.set(0)
InputPaPQ.trace("w", lambda name, index, mode, InputPaPQ = InputPaPQ: convert02(InputPaPQ))
InputPaHQ = tk.IntVar()
InputPaHQ.set(0)
InputPaHQ.trace("w", lambda name, index, mode, InputPaHQ = InputPaHQ: convert02(InputPaHQ))
InputNbPQ = tk.IntVar()
InputNbPQ.set(0)
InputNbPQ.trace("w", lambda name, index, mode, InputNbPQ = InputNbPQ: convert02(InputNbPQ))
InputNbHQ = tk.IntVar()
InputNbHQ.set(0)
InputNbHQ.trace("w", lambda name, index, mode, InputNbHQ = InputNbHQ: convert02(InputNbHQ))
Begger_PQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputBgPQ).grid(row = 1, column = 4, padx = 5, pady = 5)
Begger_HQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputBgHQ).grid(row = 2, column = 4, padx = 5, pady = 5)
Peasants_PQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputPsPQ).grid(row = 1, column = 8, padx = 5, pady = 5)
Peasants_HQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputPsHQ).grid(row = 2, column = 8, padx = 5, pady = 5)
Citizens_PQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputCzPQ).grid(row = 1, column = 12, padx = 5, pady = 5)
Citizens_HQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputCzHQ).grid(row = 2, column = 12, padx = 5, pady = 5)
Patrician_PQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputPaPQ).grid(row = 1, column = 16, padx = 5, pady = 5)
Patrician_HQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputPaHQ).grid(row = 2, column = 16, padx = 5, pady = 5)
Nobleman_PQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputNbPQ).grid(row = 1, column = 20, padx = 5, pady = 5)
Nobleman_HQEntry = tk.Entry(monty01, font = fontsize, width = 6, bd = 3, textvariable = InputNbHQ).grid(row = 2, column = 20, padx = 5, pady = 5)


    # Image
Begger1 = tk.Label(monty01, image = Begger_image, relief = "ridge")
Begger1.grid(row = 0, column = 2, columnspan = 2, padx = 5, pady = 5)
Peasants1 = tk.Label(monty01, image = Peasants_image, relief = "ridge")
Peasants1.grid(row = 0, column = 6, columnspan = 2, padx = 5, pady = 5)
Citizens1 = tk.Label(monty01, image = Citizens_image, relief = "ridge")
Citizens1.grid(row = 0, column = 10, columnspan = 2, padx = 5, pady = 5)
Patrician1 = tk.Label(monty01, image = Patrician_image, relief = "ridge")
Patrician1.grid(row = 0, column = 14, columnspan = 2, padx = 5, pady = 5)
Nobleman1 = tk.Label(monty01, image = Nobleman_image, relief = "ridge")
Nobleman1.grid(row = 0, column = 18, columnspan = 2, padx = 5, pady = 5)
Begger_PI1 = tk.Label(monty01, image = People_image, relief = "ridge").grid(row = 1, column = 3, padx = 5, pady = 5)
Begger_HI = tk.Label(monty01, image = House_image, relief = "ridge").grid(row = 2, column = 3, padx = 5, pady = 5)
Peasants_PI1 = tk.Label(monty01, image = People_image, relief = "ridge").grid(row = 1, column = 7, padx = 5, pady = 5)
Peasants_HI = tk.Label(monty01, image = House_image, relief = "ridge").grid(row = 2, column = 7, padx = 5, pady = 5)
Citizens_PI1 = tk.Label(monty01, image = People_image, relief = "ridge").grid(row = 1, column = 11, padx = 5, pady = 5)
Citizens_HI = tk.Label(monty01, image = House_image, relief = "ridge").grid(row = 2, column = 11, padx = 5, pady = 5)
Patrician_PI1 = tk.Label(monty01, image = People_image, relief = "ridge").grid(row = 1, column = 15, padx = 5, pady = 5)
Patrician_HI = tk.Label(monty01, image = House_image, relief = "ridge").grid(row = 2, column = 15, padx = 5, pady = 5)
Nobleman_PI1 = tk.Label(monty01, image = People_image, relief = "ridge").grid(row = 1, column = 19, padx = 5, pady = 5)
Nobleman_HI = tk.Label(monty01, image = House_image, relief = "ridge").grid(row = 2, column = 19, padx = 5, pady = 5)


        # Image Tool Tips


    # caculate1 計算貴豬系統
Caculate_Occident = tk.Button(monty01, font = fontsize, text = "Go！").grid(row = 2, column = 21, padx = 5, pady = 5)

    ## 輸入區(monty4) end ##

    ## 輸出區(monty5) ##    
    # 設定



    # Chosen



    # Image



        # Image Tool Tips


    # Caculate Result



    ## 輸出區(monty5) end ##

    ## 列表區(monty6) ##
    # Separator



    # Lable



    # Image



        # Image Tool Tips


    ## 列表區(monty6) end ##

#####     貴豬區 end     #####


root.mainloop()



