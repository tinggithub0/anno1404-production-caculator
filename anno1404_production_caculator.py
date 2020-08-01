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
    # 牧豬
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

# Create ToolTip
class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 300     #miliseconds
        # self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        # self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 40
        y += self.widget.winfo_rooty() + 40
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       )
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

# button command
    # def
def Caculate_Orient_Go():
    NPQG = int(InputNPQ.get())
    EPQG = int(InputEPQ.get())
    DC = (DatesChosen.current() * 0.25 + 1)
    MC = (MilkChosen.current() * 0.25 + 1)
    CaC = (CarpetsChosen.current() * 0.25 + 1)
    CoC = (CoffeeChosen.current() * 0.25 + 1)
    PnC = (Pearl_necklacesChosen.current() * 0.25 + 1)
    PeC = (PerfumeChosen.current() * 0.25 + 1)
    MaC = (MarzipanChosen.current() * 0.25 + 1)
    
    # BQ set
    if EPQG >= 4360: # 7 + 7
        DatesBQ.set(round((((NPQG / 450) + (EPQG / 600)) / DC), 2))
        MilkBQ.set(round((((NPQG / 436) + (EPQG / 666)) / MC), 2))
        CarpetsBQ.set(round((((NPQG / 909) + (EPQG / 1500)) / CaC), 2))
        CoffeeBQ.set(round(((EPQG / 1000) / CoC), 2))
        Pearl_necklacesBQ.set(round(((EPQG / 751) / PnC), 2))
        PerfumeBQ.set(round(((EPQG / 1250) / PeC), 2))
        MarzipanBQ.set(round(((EPQG / 2453) / MaC), 2))
    elif EPQG >= 2600: # 6 + 6
        DatesBQ.set(round((((NPQG / 450) + (EPQG / 600)) / DC), 2))
        MilkBQ.set(round((((NPQG / 436) + (EPQG / 666)) / MC), 2))
        CarpetsBQ.set(round((((NPQG / 909) + (EPQG / 1500)) / CaC), 2))
        CoffeeBQ.set(round(((EPQG / 1000) / CoC), 2))
        Pearl_necklacesBQ.set(round(((EPQG / 751) / PnC), 2))
        PerfumeBQ.set(round(((EPQG / 1250) / PeC), 2))
        MarzipanBQ.set("")
    elif EPQG >= 1040: # 5 + 5
        DatesBQ.set(round((((NPQG / 450) + (EPQG / 600)) / DC), 2))
        MilkBQ.set(round((((NPQG / 436) + (EPQG / 666)) / MC), 2))
        CarpetsBQ.set(round((((NPQG / 909) + (EPQG / 1500)) / CaC), 2))
        CoffeeBQ.set(round(((EPQG / 1000) / CoC), 2))
        Pearl_necklacesBQ.set(round(((EPQG / 751) / PnC), 2))
        PerfumeBQ.set("")
        MarzipanBQ.set("")
    elif EPQG >= 1: # 4 + 4
        DatesBQ.set(round((((NPQG / 450) + (EPQG / 600)) / DC), 2))
        MilkBQ.set(round((((NPQG / 436) + (EPQG / 666)) / MC), 2))
        CarpetsBQ.set(round((((NPQG / 909) + (EPQG / 1500)) / CaC), 2))
        CoffeeBQ.set(round(((EPQG / 1000) / CoC), 2))
        Pearl_necklacesBQ.set("")
        PerfumeBQ.set("")
        MarzipanBQ.set("")
    elif EPQG == 0 and NPQG >= 295: # 3 + 0
        DatesBQ.set(round((NPQG / 450), 2))
        MilkBQ.set(round((NPQG / 436), 2))
        CarpetsBQ.set(round((NPQG / 909), 2))
        CoffeeBQ.set("")
        Pearl_necklacesBQ.set("")
        PerfumeBQ.set("")
        MarzipanBQ.set("")
    elif EPQG == 0 and NPQG >= 145: # 2 + 0
        DatesBQ.set(round((NPQG / 450), 2))
        MilkBQ.set(round((NPQG / 436), 2))
        CarpetsBQ.set("")
        CoffeeBQ.set("")
        Pearl_necklacesBQ.set("")
        PerfumeBQ.set("")
        MarzipanBQ.set("")
    else: # 1 + 0
        DatesBQ.set(round((NPQG / 450), 2))
        MilkBQ.set("")
        CarpetsBQ.set("")
        CoffeeBQ.set("")
        Pearl_necklacesBQ.set("")
        PerfumeBQ.set("")
        MarzipanBQ.set("")
    
# Tab Control
tabControl = ttk.Notebook(root)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text = "牧豬")      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text = "貴豬")      # Make second tab visible
tabControl.grid(row = 0, column = 0)


#####     牧豬區     #####

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
def convert1(Rbtn1):
    Rbtn1 = Rbtn1.get()

Rbtn1 = tk.IntVar()
Rbtn1.set(2)
RadioP = ttk.Radiobutton(monty1, value = 1, variable = Rbtn1).grid(row = 1, column = 0, padx = 5, pady = 5)
RadioH = ttk.Radiobutton(monty1, value = 2, variable = Rbtn1).grid(row = 2, column = 0, padx = 5, pady = 5)
Nomads_RadioP = ttk.Radiobutton(monty1, value = 1, variable = Rbtn1).grid(row = 1, column = 2, padx = 5, pady = 5)
Nomads_RadioH = ttk.Radiobutton(monty1, value = 2, variable = Rbtn1).grid(row = 2, column = 2, padx = 5, pady = 5)
Envoys_RadioP = ttk.Radiobutton(monty1, value = 1, variable = Rbtn1).grid(row = 1, column = 6, padx = 5, pady = 5)
Envoys_RadioH = ttk.Radiobutton(monty1, value = 2, variable = Rbtn1).grid(row = 2, column = 6, padx = 5, pady = 5)
Rbtn1.trace("w", lambda name, index, mode, Rbtn1 = Rbtn1: convert1(Rbtn1))
    
    # Separator
Separator1 = ttk.Separator(monty1, orient = "vertical").grid(row = 1, column = 1, rowspan = 2, sticky = "ns")
Separator2 = ttk.Separator(monty1, orient = "vertical").grid(row = 1, column = 5, rowspan = 2, sticky = "ns")
    
    # Input  
        # PQ.HQ convert by Radiobutton def
def convert2(*args):
    try:
        if Rbtn1.get() == 1:
            InputNHQ.set((InputNPQ.get())/15)
            InputEHQ.set((InputEPQ.get())/15)
        else:
            InputNPQ.set((InputNHQ.get())*15)
            InputEPQ.set((InputEHQ.get())*15)
    except Exception:
        time.sleep(0.01)

InputNPQ = tk.IntVar()
InputNPQ.set(0)
InputNPQ.trace("w", lambda name, index, mode, InputNPQ = InputNPQ: convert2(InputNPQ))
InputNHQ = tk.IntVar()
InputNHQ.set(0)
InputNHQ.trace("w", lambda name, index, mode, InputNHQ = InputNHQ: convert2(InputNHQ))
InputEPQ = tk.IntVar()
InputEPQ.set(0)
InputEPQ.trace("w", lambda name, index, mode, InputEPQ = InputEPQ: convert2(InputEPQ))
InputEHQ = tk.IntVar()
InputEHQ.set(0)
InputEHQ.trace("w", lambda name, index, mode, InputEHQ = InputEHQ: convert2(InputEHQ))
Nomads_PQEntry = tk.Entry(monty1, font = fontsize, width = 6, bd = 3, textvariable = InputNPQ).grid(row = 1, column = 4, padx = 5, pady = 5)
Nomads_HQEntry = tk.Entry(monty1, font = fontsize, width = 6, bd = 3, textvariable = InputNHQ).grid(row = 2, column = 4, padx = 5, pady = 5)
Envoys_PQEntry = tk.Entry(monty1, font = fontsize, width = 6, bd = 3, textvariable = InputEPQ).grid(row = 1, column = 8, padx = 5, pady = 5)
Envoys_HQEntry = tk.Entry(monty1, font = fontsize, width = 6, bd = 3, textvariable = InputEHQ).grid(row = 2, column = 8, padx = 5, pady = 5)


    # Image
Nomads1 = tk.Label(monty1, image = Nomads_image, relief = "ridge")
Nomads1.grid(row = 0, column = 2, columnspan = 2, padx = 5, pady = 5)
Envoys1 = tk.Label(monty1, image = Envoys_image, relief = "ridge")
Envoys1.grid(row = 0, column = 6, columnspan = 2, padx = 5, pady = 5)
Nomads_PI1 = tk.Label(monty1, image = People_image, relief = "ridge").grid(row = 1, column = 3, padx = 5, pady = 5)
Nomads_HI = tk.Label(monty1, image = House_image, relief = "ridge").grid(row = 2, column = 3, padx = 5, pady = 5)
Envoys_PI1 = tk.Label(monty1, image = People_image, relief = "ridge").grid(row = 1, column = 7, padx = 5, pady = 5)
Envoys_HI = tk.Label(monty1, image = House_image, relief = "ridge").grid(row = 2, column = 7, padx = 5, pady = 5)

        # Image Tool Tips
Nomads1TT = CreateToolTip(Nomads1, "牧民")
Envoys1TT = CreateToolTip(Envoys1, "牧主")


    # caculate1 計算牧豬系統
Caculate_Orient = tk.Button(monty1, font = fontsize, text = "Go！", command = Caculate_Orient_Go).grid(row = 2, column = 9, padx = 5, pady = 5)

    ## 輸入區(monty1) end ##

    ## 輸出區(monty2) ##    
    # 設定
Persent1 = ["DatesPersent", "MilkPersent", "CarpetsPersent", "CoffeePersent", "Pearl_necklacesPersent", "PerfumePersent", "MarzipanPersent"]
Persent1 = tk.StringVar()
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
Dates1 = tk.Label(monty2, image = Dates_image, relief = "ridge")
Dates1.grid(row = 0, column = 1, padx = 5, pady = 5)
Milk1 = tk.Label(monty2, image = Milk_image, relief = "ridge")
Milk1.grid(row = 1, column = 1, padx = 5, pady = 5)
Carpets1 = tk.Label(monty2, image = Carpets_image, relief = "ridge")
Carpets1.grid(row = 2, column = 1, padx = 5, pady = 5)
Coffee1 = tk.Label(monty2, image = Coffee_image, relief = "ridge")
Coffee1.grid(row = 3, column = 1, padx = 5, pady = 5)
Pearl_necklaces1 = tk.Label(monty2, image = Pearl_necklaces_image, relief = "ridge")
Pearl_necklaces1.grid(row = 4, column = 1, padx = 5, pady = 5)
Perfume1 = tk.Label(monty2, image = Perfume_image, relief = "ridge")
Perfume1.grid(row = 5, column = 1, padx = 5, pady = 5)
Marzipan1 = tk.Label(monty2, image = Marzipan_image, relief = "ridge")
Marzipan1.grid(row = 6, column = 1, padx = 5, pady = 5)

        # Image Tool Tips
Dates1TT = CreateToolTip(Dates1, "椰棗")
Milk1TT = CreateToolTip(Milk1, "羊奶")
Carpets1TT = CreateToolTip(Carpets1, "織毯")
Coffee1TT = CreateToolTip(Coffee1, "咖啡")
Pearl_necklaces1TT = CreateToolTip(Pearl_necklaces1, "珍珠項鍊")
Perfume1TT = CreateToolTip(Perfume1, "香水")
Marzipan1TT = CreateToolTip(Marzipan1, "扁桃仁膏")

    # Caculate Result
DatesBQ = tk.StringVar()
Dates_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = DatesBQ).grid(row = 0, column = 2, padx = 5, pady = 5)
MilkBQ = tk.StringVar()
Milk_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = MilkBQ).grid(row = 1, column = 2, padx = 5, pady = 5)
CarpetsBQ = tk.StringVar()
Carpets_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = CarpetsBQ).grid(row = 2, column = 2, padx = 5, pady = 5)
CoffeeBQ = tk.StringVar()
Coffee_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = CoffeeBQ).grid(row = 3, column = 2, padx = 5, pady = 5)
Pearl_necklacesBQ = tk.StringVar()
Pearl_necklaces_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = Pearl_necklacesBQ).grid(row = 4, column = 2, padx = 5, pady = 5)
PerfumeBQ = tk.StringVar()
Perfume_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = PerfumeBQ).grid(row = 5, column = 2, padx = 5, pady = 5)
MarzipanBQ = tk.StringVar()
Marzipan_BQ = tk.Label(monty2, font = fontsize, width = 5, bd = 3, textvariable = MarzipanBQ).grid(row = 6, column = 2, padx = 5, pady = 5)

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
Dates2 = tk.Label(monty3, image = Dates_image, relief = "ridge")
Dates2.grid(row = 1, column = 3, padx = 5, pady = 5)
Milk2 = tk.Label(monty3, image = Milk_image, relief = "ridge")
Milk2.grid(row = 1, column = 5, padx = 5, pady = 5)
Carpets2 = tk.Label(monty3, image = Carpets_image, relief = "ridge")
Carpets2.grid(row = 1, column = 7, padx = 5, pady = 5)
Coffee2 = tk.Label(monty3, image = Coffee_image, relief = "ridge")
Coffee2.grid(row = 1, column = 9, padx = 5, pady = 5)
Pearl_necklaces2 = tk.Label(monty3, image = Pearl_necklaces_image, relief = "ridge")
Pearl_necklaces2.grid(row = 1, column = 11, padx = 5, pady = 5)
Perfume2 = tk.Label(monty3, image = Perfume_image, relief = "ridge")
Perfume2.grid(row = 1, column = 13, padx = 5, pady = 5)
Marzipan2 = tk.Label(monty3, image = Marzipan_image, relief = "ridge")
Marzipan2.grid(row = 1, column = 15, padx = 5, pady = 5)
Nomads2 = tk.Label(monty3, image = Nomads_image, relief = "ridge")
Nomads2.grid(row = 3, column = 1, padx = 5, pady = 5)
Nomads_PI2 = tk.Label(monty3, image = People_image, relief = "ridge").grid(row = 5, column = 1, padx = 5, pady = 5)
Envoys2 = tk.Label(monty3, image = Envoys_image, relief = "ridge")
Envoys2.grid(row = 7, column = 1, padx = 5, pady = 5)
Envoys_PI2 = tk.Label(monty3, image = People_image, relief = "ridge").grid(row = 9, column = 1, padx = 5, pady = 5)

        # Image Tool Tips
Dates2TT = CreateToolTip(Dates2, "椰棗")
Milk2TT = CreateToolTip(Milk2, "羊奶")
Carpets2TT = CreateToolTip(Carpets2, "織毯")
Coffee2TT = CreateToolTip(Coffee2, "咖啡")
Pearl_necklaces2TT = CreateToolTip(Pearl_necklaces2, "珍珠項鍊")
Perfume2TT = CreateToolTip(Perfume2, "香水")
Marzipan2TT = CreateToolTip(Marzipan2, "扁桃仁膏")
Nomads2TT = CreateToolTip(Nomads2, "牧民")
Envoys2TT = CreateToolTip(Envoys2, "牧主")

    ## 列表區(monty3) end ##


#####     牧豬區 end     #####

#####     貴豬區     #####













#####     貴豬區 end     #####

root.mainloop()



