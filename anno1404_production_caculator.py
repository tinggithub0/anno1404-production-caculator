import tkinter as tk
import tkinter.font as tkFont
import math
from tkinter import ttk
import time


root = tk.Tk()

# 視窗設定
fontsize = tkFont.Font(family = "Source Han Sans", size = 14)
root.title("Anno 1404 caculator")
root.resizable(0,0)
root.geometry("1235x900")
root.iconbitmap(r"D:/python/python-anno1404/images/anno1404_icon.ico")

# 載入圖片
People_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/People.png")
House_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/House.png")

    # 牧主
Nomads_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Nomads.png")
Envoys_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Envoys.png")
Dates_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Dates.png")
Milk_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Milk.png")
Carpets_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Carpets.png")
Coffee_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Coffee.png")
Pearl_necklaces_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Pearl_necklaces.png")
Perfume_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Perfume.png")
Marzipan_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Marzipan.png")

    # 貴族
Begger_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Begger.png")
Peasants_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Peasants.png")
Citizens_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Citizens.png")
Patrician_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Patrician.png")
Nobleman_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Nobleman.png")
Fish_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Fish.png")
Cider_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Cider.png")
Spices_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Spices.png")
Linen_garments_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Linen_garments.png")
Bread_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Bread.png")
Beer_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Beer.png")
Leather_jerkins_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Leather_jerkins.png")
Books_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Books.png")
Meat_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Meat.png")
Fur_coats_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Fur_coats.png")
Wine_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Wine.png")
Glasses_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Glasses.png")
Candlestick_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Candlestick.png")
Brocade_robes_image = tk.PhotoImage(file = "D:/python/python-anno1404/images/Brocade_robes.png")

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
    # Orient
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
    if EPQG >= 4360: # 3 + 7
        DatesBQ.set(round((((NPQG / 450) + (EPQG / 600)) / DC), 2))
        MilkBQ.set(round((((NPQG / 436) + (EPQG / 666)) / MC), 2))
        CarpetsBQ.set(round((((NPQG / 909) + (EPQG / 1500)) / CaC), 2))
        CoffeeBQ.set(round(((EPQG / 1000) / CoC), 2))
        Pearl_necklacesBQ.set(round(((EPQG / 751) / PnC), 2))
        PerfumeBQ.set(round(((EPQG / 1250) / PeC), 2))
        MarzipanBQ.set(round(((EPQG / 2453) / MaC), 2))
    elif EPQG >= 2600: # 3 + 6
        DatesBQ.set(round((((NPQG / 450) + (EPQG / 600)) / DC), 2))
        MilkBQ.set(round((((NPQG / 436) + (EPQG / 666)) / MC), 2))
        CarpetsBQ.set(round((((NPQG / 909) + (EPQG / 1500)) / CaC), 2))
        CoffeeBQ.set(round(((EPQG / 1000) / CoC), 2))
        Pearl_necklacesBQ.set(round(((EPQG / 751) / PnC), 2))
        PerfumeBQ.set(round(((EPQG / 1250) / PeC), 2))
        MarzipanBQ.set("")
    elif EPQG >= 1040: # 3 + 5
        DatesBQ.set(round((((NPQG / 450) + (EPQG / 600)) / DC), 2))
        MilkBQ.set(round((((NPQG / 436) + (EPQG / 666)) / MC), 2))
        CarpetsBQ.set(round((((NPQG / 909) + (EPQG / 1500)) / CaC), 2))
        CoffeeBQ.set(round(((EPQG / 1000) / CoC), 2))
        Pearl_necklacesBQ.set(round(((EPQG / 751) / PnC), 2))
        PerfumeBQ.set("")
        MarzipanBQ.set("")
    elif EPQG >= 1: # 3 + 4
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

    # Occident
        # def
def Caculate_Occident_Go():
    BgPQG = int(InputBgPQ.get())
    PsPQG = int(InputPsPQ.get())
    CzPQG = int(InputCzPQ.get())
    PaPQG = int(InputPaPQ.get())
    NbPQG = int(InputNbPQ.get())
    FsC = (FishChosen.current() * 0.25 + 1)
    CdC = (CiderChosen.current() * 0.25 + 1)
    SpC = (SpicesChosen.current() * 0.25 + 1)
    LgC = (Linen_garmentsChosen.current() * 0.25 + 1)
    BrC = (BreadChosen.current() * 0.25 + 1)
    BeC = (BeerChosen.current() * 0.25 + 1)
    LjC = (Leather_jerkinsChosen.current() * 0.25 + 1)
    BoC = (BooksChosen.current() * 0.25 + 1)
    MeC = (MeatChosen.current() * 0.25 + 1)
    FcC = (Fur_coatsChosen.current() * 0.25 + 1)
    WiC = (WineChosen.current() * 0.25 + 1)
    GlC = (GlassesChosen.current() * 0.25 + 1)
    CaC = (CandlestickChosen.current() * 0.25 + 1)
    BrC = (Brocade_robesChosen.current() * 0.25 + 1)
    
        # BQ set
    if NbPQG >= 4000: # 2 + 2 + 4 + 9 + 14
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652) + (NbPQG / 1153)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052) + (NbPQG / 2500)) / LgC), 2))
        BreadBQ.set(round((((PaPQG / 727) + (NbPQG / 1025)) / BrC), 2))
        BeerBQ.set(round((((PaPQG / 625) + (NbPQG / 1071)) / BeC), 2))
        Leather_jerkinsBQ.set(round((((PaPQG / 1428) + (NbPQG / 2500)) / LjC), 2))
        BooksBQ.set(round((((PaPQG / 1875) + (NbPQG / 3333)) / BoC), 2))
        MeatBQ.set(round(((NbPQG / 1136) / MeC), 2))
        Fur_coatsBQ.set(round(((NbPQG / 1562) / FcC), 2))
        WineBQ.set(round(((NbPQG / 1000) / WiC), 2))
        GlassesBQ.set(round(((NbPQG / 1709) / GlC), 2))
        CandlestickBQ.set(round((((PaPQG / 2500) + (NbPQG / 3333)) / CaC), 2))
        Brocade_robesBQ.set(round(((NbPQG / 2112) / BrC), 2))
    elif NbPQG >= 3000: # 2 + 2 + 4 + 9 + 13
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652) + (NbPQG / 1153)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052) + (NbPQG / 2500)) / LgC), 2))
        BreadBQ.set(round((((PaPQG / 727) + (NbPQG / 1025)) / BrC), 2))
        BeerBQ.set(round((((PaPQG / 625) + (NbPQG / 1071)) / BeC), 2))
        Leather_jerkinsBQ.set(round((((PaPQG / 1428) + (NbPQG / 2500)) / LjC), 2))
        BooksBQ.set(round((((PaPQG / 1875) + (NbPQG / 3333)) / BoC), 2))
        MeatBQ.set(round(((NbPQG / 1136) / MeC), 2))
        Fur_coatsBQ.set(round(((NbPQG / 1562) / FcC), 2))
        WineBQ.set(round(((NbPQG / 1000) / WiC), 2))
        GlassesBQ.set(round(((NbPQG / 1709) / GlC), 2))
        CandlestickBQ.set(round((((PaPQG / 2500) + (NbPQG / 3333)) / CaC), 2))
        Brocade_robesBQ.set("")
    elif NbPQG >= 2200: # 2 + 2 + 4 + 8 + 12
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652) + (NbPQG / 1153)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052) + (NbPQG / 2500)) / LgC), 2))
        BreadBQ.set(round((((PaPQG / 727) + (NbPQG / 1025)) / BrC), 2))
        BeerBQ.set(round((((PaPQG / 625) + (NbPQG / 1071)) / BeC), 2))
        Leather_jerkinsBQ.set(round((((PaPQG / 1428) + (NbPQG / 2500)) / LjC), 2))
        BooksBQ.set(round((((PaPQG / 1875) + (NbPQG / 3333)) / BoC), 2))
        MeatBQ.set(round(((NbPQG / 1136) / MeC), 2))
        Fur_coatsBQ.set(round(((NbPQG / 1562) / FcC), 2))
        WineBQ.set(round(((NbPQG / 1000) / WiC), 2))
        GlassesBQ.set(round(((NbPQG / 1709) / GlC), 2))
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG >= 1500: # 2 + 2 + 4 + 8 + 11
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652) + (NbPQG / 1153)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052) + (NbPQG / 2500)) / LgC), 2))
        BreadBQ.set(round((((PaPQG / 727) + (NbPQG / 1025)) / BrC), 2))
        BeerBQ.set(round((((PaPQG / 625) + (NbPQG / 1071)) / BeC), 2))
        Leather_jerkinsBQ.set(round((((PaPQG / 1428) + (NbPQG / 2500)) / LjC), 2))
        BooksBQ.set(round((((PaPQG / 1875) + (NbPQG / 3333)) / BoC), 2))
        MeatBQ.set(round(((NbPQG / 1136) / MeC), 2))
        Fur_coatsBQ.set(round(((NbPQG / 1562) / FcC), 2))
        WineBQ.set(round(((NbPQG / 1000) / WiC), 2))
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG >= 950: # 2 + 2 + 4 + 8 + 10
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652) + (NbPQG / 1153)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052) + (NbPQG / 2500)) / LgC), 2))
        BreadBQ.set(round((((PaPQG / 727) + (NbPQG / 1025)) / BrC), 2))
        BeerBQ.set(round((((PaPQG / 625) + (NbPQG / 1071)) / BeC), 2))
        Leather_jerkinsBQ.set(round((((PaPQG / 1428) + (NbPQG / 2500)) / LjC), 2))
        BooksBQ.set(round((((PaPQG / 1875) + (NbPQG / 3333)) / BoC), 2))
        MeatBQ.set(round(((NbPQG / 1136) / MeC), 2))
        Fur_coatsBQ.set(round(((NbPQG / 1562) / FcC), 2))
        WineBQ.set("")
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG >= 1: # 2 + 2 + 4 + 8 + 9
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652) + (NbPQG / 1153)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909) + (NbPQG / 1250)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052) + (NbPQG / 2500)) / LgC), 2))
        BreadBQ.set(round((((PaPQG / 727) + (NbPQG / 1025)) / BrC), 2))
        BeerBQ.set(round((((PaPQG / 625) + (NbPQG / 1071)) / BeC), 2))
        Leather_jerkinsBQ.set(round((((PaPQG / 1428) + (NbPQG / 2500)) / LjC), 2))
        BooksBQ.set(round((((PaPQG / 1875) + (NbPQG / 3333)) / BoC), 2))
        MeatBQ.set(round(((NbPQG / 1136) / MeC), 2))
        Fur_coatsBQ.set("")
        WineBQ.set("")
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG == 0 and PaPQG >= 940: # 2 + 2 + 4 + 8 + 0
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052)) / LgC), 2))
        BreadBQ.set(round(((PaPQG / 727) / BrC), 2))
        BeerBQ.set(round(((PaPQG / 625) / BeC), 2))
        Leather_jerkinsBQ.set(round(((PaPQG / 1428) / LjC), 2))
        BooksBQ.set(round(((PaPQG / 1875) / BoC), 2))
        MeatBQ.set("")
        Fur_coatsBQ.set("")
        WineBQ.set("")
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG == 0 and PaPQG >= 690: # 2 + 2 + 4 + 7 + 0
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052)) / LgC), 2))
        BreadBQ.set(round(((PaPQG / 727) / BrC), 2))
        BeerBQ.set(round(((PaPQG / 625) / BeC), 2))
        Leather_jerkinsBQ.set(round(((PaPQG / 1428) / LjC), 2))
        BooksBQ.set("")
        MeatBQ.set("")
        Fur_coatsBQ.set("")
        WineBQ.set("")
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG == 0 and PaPQG >= 510: # 2 + 2 + 4 + 6 + 0
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052)) / LgC), 2))
        BreadBQ.set(round(((PaPQG / 727) / BrC), 2))
        BeerBQ.set(round(((PaPQG / 625) / BeC), 2))
        Leather_jerkinsBQ.set("")
        BooksBQ.set("")
        MeatBQ.set("")
        Fur_coatsBQ.set("")
        WineBQ.set("")
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG == 0 and PaPQG >= 1: # 2 + 2 + 4 + 5 + 0
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500) + (PaPQG / 909)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340) + (PaPQG / 652)) / CdC), 2))
        SpicesBQ.set(round((((CzPQG / 500) + (PaPQG / 909)) / SpC), 2))
        Linen_garmentsBQ.set(round((((CzPQG / 476) + (PaPQG / 1052)) / LgC), 2))
        BreadBQ.set(round(((PaPQG / 727) / BrC), 2))
        BeerBQ.set("")
        Leather_jerkinsBQ.set("")
        BooksBQ.set("")
        MeatBQ.set("")
        Fur_coatsBQ.set("")
        WineBQ.set("")
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG == 0 and PaPQG == 0 and CzPQG >= 1: # 2 + 2 + 4 + 0 + 0
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200) + (CzPQG / 500)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340) + (CzPQG / 340)) / CdC), 2))
        SpicesBQ.set(round(((CzPQG / 500) / SpC), 2))
        Linen_garmentsBQ.set(round(((CzPQG / 476) / LgC), 2))
        BreadBQ.set("")
        BeerBQ.set("")
        Leather_jerkinsBQ.set("")
        BooksBQ.set("")
        MeatBQ.set("")
        Fur_coatsBQ.set("")
        WineBQ.set("")
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG == 0 and PaPQG == 0 and CzPQG == 0 and PsPQG >= 60: # 2 + 2 + 0 + 0 + 0
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200)) / FsC), 2))
        CiderBQ.set(round((((BgPQG / 500) + (PsPQG / 340)) / CdC), 2))
        SpicesBQ.set("")
        Linen_garmentsBQ.set("")
        BreadBQ.set("")
        BeerBQ.set("")
        Leather_jerkinsBQ.set("")
        BooksBQ.set("")
        MeatBQ.set("")
        Fur_coatsBQ.set("")
        WineBQ.set("")
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")
    elif NbPQG == 0 and PaPQG == 0 and CzPQG == 0 and PsPQG >= 1: # 2 + 1 + 0 + 0 + 0
        FishBQ.set(round((((BgPQG / 285) + (PsPQG / 200)) / FsC), 2))
        CiderBQ.set(round(((BgPQG / 500) / CdC), 2))
        SpicesBQ.set("")
        Linen_garmentsBQ.set("")
        BreadBQ.set("")
        BeerBQ.set("")
        Leather_jerkinsBQ.set("")
        BooksBQ.set("")
        MeatBQ.set("")
        Fur_coatsBQ.set("")
        WineBQ.set("")
        GlassesBQ.set("")
        CandlestickBQ.set("")
        Brocade_robesBQ.set("")    

# Tab Control
tabControl = ttk.Notebook(root)          # Create Tab Control
tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text = "牧主看這裡")      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text = "貴族看這裡")      # Make second tab visible
tabControl.grid(row = 0, column = 0)




#####     牧主區     #####


# Tab1控件
monty1 = ttk.LabelFrame(tab1, text = "牧主養成計畫") # 輸入區
monty1.grid(row = 0, column = 0, padx = 8, pady = 4, sticky = "w")
monty2 = ttk.LabelFrame(tab1, text = "牧主養成需求") # 輸出區
monty2.grid(row = 0, column = 1, rowspan = 2, padx = 8, pady = 4, sticky = "n")
monty3 = ttk.LabelFrame(tab1, text = "牧主養成手冊") # 列表區
monty3.grid(row = 1, column = 0, padx = 8, pady = 4)

    # Tab1內部配置

    ###   輸入區(monty1)   ###

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

            # InputQ  
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


        # 計算牧主系統
Caculate_Orient = tk.Button(monty1, font = fontsize, text = "Go！", command = Caculate_Orient_Go).grid(row = 2, column = 9, padx = 5, pady = 5)

    ###   輸入區(monty1) end   ###



    ###   輸出區(monty2)   ###  

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

    ###   輸出區(monty2) end   ###



    ###   列表區(monty3)   ###

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

    ###   列表區(monty3) end   ###




#####     牧主區 end     #####





#####     貴族區     #####


# Tab2控件
monty01 = ttk.LabelFrame(tab2, text = "貴族養成計畫") # 輸入區
monty01.grid(row = 0, column = 0, padx = 8, pady = 4, sticky = "w")
monty02 = ttk.LabelFrame(tab2, text = "貴族養成需求") # 輸出區
monty02.grid(row = 0, column = 1, rowspan = 2, padx = 8, pady = 4, sticky = "n")
monty03 = ttk.LabelFrame(tab2, text = "貴族養成手冊") # 列表區
monty03.grid(row = 1, column = 0, padx = 8, pady = 4)

    # Tab2內部配置

        ###   輸入區(monty01)   ###

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
Rbtn01.trace("w", lambda name, index, mode, Rbtn01 = Rbtn01: convert01(Rbtn01))

        # Separator
Separator01 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 1, rowspan = 2, sticky = "ns")
Separator02 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 5, rowspan = 2, sticky = "ns")
Separator03 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 9, rowspan = 2, sticky = "ns")
Separator04 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 13, rowspan = 2, sticky = "ns")
Separator05 = ttk.Separator(monty01, orient = "vertical").grid(row = 1, column = 17, rowspan = 2, sticky = "ns")

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

            # InputQ 
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
Begger1TT = CreateToolTip(Begger1, "乞丐")
Peasants1TT = CreateToolTip(Peasants1, "農民")
Citizens1TT = CreateToolTip(Citizens1, "市民")
Patrician1TT = CreateToolTip(Patrician1, "紳士")
Nobleman1TT = CreateToolTip(Nobleman1, "貴族")

        # 計算貴族系統
Caculate_Occident = tk.Button(monty01, font = fontsize, text = "Go！", command = Caculate_Occident_Go).grid(row = 2, column = 21, padx = 5, pady = 5)

    ###   輸入區(monty01) end   ###



    ###   輸出區(monty02)   ###    

        # 設定
Persent01 = ["FishPersent", "CiderPersent", "SpicesPersent", "Linen_garmentsPersent", "BreadPersent", "BeerPersent", "Leather_jerkinsPersent", 
            "BooksPersent", "MeatPersent", "Fur_coatsPersent", "WinePersent", "GlassesPersent", "CandlestickPersent", "Brocade_robesPersent"]
Persent01 = tk.StringVar()
ChosenValues = ["0%", "25%", "50%", "75%"]
    
        # Chosen
FishChosen = ttk.Combobox(monty02, width = 4, textvariable = "FishPersent", state = "readonly")
FishChosen["values"] = ChosenValues
FishChosen.grid(row = 0, column = 0, padx = 5, pady = 5)
FishChosen.current(0)

CiderChosen = ttk.Combobox(monty02, width = 4, textvariable = "CiderPersent", state = "readonly")
CiderChosen["values"] = ChosenValues
CiderChosen.grid(row = 1, column = 0, padx = 5, pady = 5)
CiderChosen.current(0)

SpicesChosen = ttk.Combobox(monty02, width = 4, textvariable = "SpicesPersent", state = "readonly")
SpicesChosen["values"] = ChosenValues
SpicesChosen.grid(row = 2, column = 0, padx = 5, pady = 5)
SpicesChosen.current(0)

Linen_garmentsChosen = ttk.Combobox(monty02, width = 4, textvariable = "Linen_garmentsPersent", state = "readonly")
Linen_garmentsChosen["values"] = ChosenValues
Linen_garmentsChosen.grid(row = 3, column = 0, padx = 5, pady = 5)
Linen_garmentsChosen.current(0)

BreadChosen = ttk.Combobox(monty02, width = 4, textvariable = "BreadPersent", state = "readonly")
BreadChosen["values"] = ChosenValues
BreadChosen.grid(row = 4, column = 0, padx = 5, pady = 5)
BreadChosen.current(0)

BeerChosen = ttk.Combobox(monty02, width = 4, textvariable = "BeerPersent", state = "readonly")
BeerChosen["values"] = ChosenValues
BeerChosen.grid(row = 5, column = 0, padx = 5, pady = 5)
BeerChosen.current(0)

Leather_jerkinsChosen = ttk.Combobox(monty02, width = 4, textvariable = "Leather_jerkinsPersent", state = "readonly")
Leather_jerkinsChosen["values"] = ChosenValues
Leather_jerkinsChosen.grid(row = 6, column = 0, padx = 5, pady = 5)
Leather_jerkinsChosen.current(0)

BooksChosen = ttk.Combobox(monty02, width = 4, textvariable = "BooksPersent", state = "readonly")
BooksChosen["values"] = ChosenValues
BooksChosen.grid(row = 7, column = 0, padx = 5, pady = 5)
BooksChosen.current(0)

MeatChosen = ttk.Combobox(monty02, width = 4, textvariable = "MeatPersent", state = "readonly")
MeatChosen["values"] = ChosenValues
MeatChosen.grid(row = 8, column = 0, padx = 5, pady = 5)
MeatChosen.current(0)

Fur_coatsChosen = ttk.Combobox(monty02, width = 4, textvariable = "Fur_coatsPersent", state = "readonly")
Fur_coatsChosen["values"] = ChosenValues
Fur_coatsChosen.grid(row = 9, column = 0, padx = 5, pady = 5)
Fur_coatsChosen.current(0)

WineChosen = ttk.Combobox(monty02, width = 4, textvariable = "WinePersent", state = "readonly")
WineChosen["values"] = ChosenValues
WineChosen.grid(row = 10, column = 0, padx = 5, pady = 5)
WineChosen.current(0)

GlassesChosen = ttk.Combobox(monty02, width = 4, textvariable = "GlassesPersent", state = "readonly")
GlassesChosen["values"] = ChosenValues
GlassesChosen.grid(row = 11, column = 0, padx = 5, pady = 5)
GlassesChosen.current(0)

CandlestickChosen = ttk.Combobox(monty02, width = 4, textvariable = "CandlestickPersent", state = "readonly")
CandlestickChosen["values"] = ChosenValues
CandlestickChosen.grid(row = 12, column = 0, padx = 5, pady = 5)
CandlestickChosen.current(0)

Brocade_robesChosen = ttk.Combobox(monty02, width = 4, textvariable = "Brocade_robesPersent", state = "readonly")
Brocade_robesChosen["values"] = ChosenValues
Brocade_robesChosen.grid(row = 13, column = 0, padx = 5, pady = 5)
Brocade_robesChosen.current(0)

        # Image
Fish1 = tk.Label(monty02, image = Fish_image, relief = "ridge")
Fish1.grid(row = 0, column = 1, padx = 5, pady = 5)
Cider1 = tk.Label(monty02, image = Cider_image, relief = "ridge")
Cider1.grid(row = 1, column = 1, padx = 5, pady = 5)
Spices1 = tk.Label(monty02, image = Spices_image, relief = "ridge")
Spices1.grid(row = 2, column = 1, padx = 5, pady = 5)
Linen_garments1 = tk.Label(monty02, image = Linen_garments_image, relief = "ridge")
Linen_garments1.grid(row = 3, column = 1, padx = 5, pady = 5)
Bread1 = tk.Label(monty02, image = Bread_image, relief = "ridge")
Bread1.grid(row = 4, column = 1, padx = 5, pady = 5)
Beer1 = tk.Label(monty02, image = Beer_image, relief = "ridge")
Beer1.grid(row = 5, column = 1, padx = 5, pady = 5)
Leather_jerkins1 = tk.Label(monty02, image = Leather_jerkins_image, relief = "ridge")
Leather_jerkins1.grid(row = 6, column = 1, padx = 5, pady = 5)
Books1 = tk.Label(monty02, image = Books_image, relief = "ridge")
Books1.grid(row = 7, column = 1, padx = 5, pady = 5)
Meat1 = tk.Label(monty02, image = Meat_image, relief = "ridge")
Meat1.grid(row = 8, column = 1, padx = 5, pady = 5)
Fur_coats1 = tk.Label(monty02, image = Fur_coats_image, relief = "ridge")
Fur_coats1.grid(row = 9, column = 1, padx = 5, pady = 5)
Wine1 = tk.Label(monty02, image = Wine_image, relief = "ridge")
Wine1.grid(row = 10, column = 1, padx = 5, pady = 5)
Glasses1 = tk.Label(monty02, image = Glasses_image, relief = "ridge")
Glasses1.grid(row = 11, column = 1, padx = 5, pady = 5)
Candlestick1 = tk.Label(monty02, image = Candlestick_image, relief = "ridge")
Candlestick1.grid(row = 12, column = 1, padx = 5, pady = 5)
Brocade_robes1 = tk.Label(monty02, image = Brocade_robes_image, relief = "ridge")
Brocade_robes1.grid(row = 13, column = 1, padx = 5, pady = 5)

            # Image Tool Tips
Fish1TT = CreateToolTip(Fish1, "魚肉")
Cider1TT = CreateToolTip(Cider1, "果汁")
Spices1TT = CreateToolTip(Spices1, "香料")
Linen_garments1TT = CreateToolTip(Linen_garments1, "亞麻服裝")
Bread1TT = CreateToolTip(Bread1, "麵包")
Beer1TT = CreateToolTip(Beer1, "啤酒")
Leather_jerkins1TT = CreateToolTip(Leather_jerkins1, "皮革上衣")
Books1TT = CreateToolTip(Books1, "書籍")
Meat1TT = CreateToolTip(Meat1, "醃肉")
Fur_coats1TT = CreateToolTip(Fur_coats1, "毛皮大氅")
Wine1TT = CreateToolTip(Wine1, "葡萄酒")
Glasses1TT = CreateToolTip(Glasses1, "眼鏡")
Candlestick1TT = CreateToolTip(Candlestick1, "燭台")
Brocade_robes1TT = CreateToolTip(Brocade_robes1, "金縷衣")

        # Caculate Result
FishBQ = tk.StringVar()
Fish_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = FishBQ).grid(row = 0, column = 2, padx = 5, pady = 5)
CiderBQ = tk.StringVar()
Cider_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = CiderBQ).grid(row = 1, column = 2, padx = 5, pady = 5)
SpicesBQ = tk.StringVar()
Spices_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = SpicesBQ).grid(row = 2, column = 2, padx = 5, pady = 5)
Linen_garmentsBQ = tk.StringVar()
Linen_garments_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = Linen_garmentsBQ).grid(row = 3, column = 2, padx = 5, pady = 5)
BreadBQ = tk.StringVar()
Bread_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = BreadBQ).grid(row = 4, column = 2, padx = 5, pady = 5)
BeerBQ = tk.StringVar()
Beer_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = BeerBQ).grid(row = 5, column = 2, padx = 5, pady = 5)
Leather_jerkinsBQ = tk.StringVar()
Leather_jerkins_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = Leather_jerkinsBQ).grid(row = 6, column = 2, padx = 5, pady = 5)
BooksBQ = tk.StringVar()
Books_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = BooksBQ).grid(row = 7, column = 2, padx = 5, pady = 5)
MeatBQ = tk.StringVar()
Meat_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = MeatBQ).grid(row = 8, column = 2, padx = 5, pady = 5)
Fur_coatsBQ = tk.StringVar()
Fur_coats_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = Fur_coatsBQ).grid(row = 9, column = 2, padx = 5, pady = 5)
WineBQ = tk.StringVar()
Wine_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = WineBQ).grid(row = 10, column = 2, padx = 5, pady = 5)
GlassesBQ = tk.StringVar()
Glasses_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = GlassesBQ).grid(row = 11, column = 2, padx = 5, pady = 5)
CandlestickBQ = tk.StringVar()
Candlestick_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = CandlestickBQ).grid(row = 12, column = 2, padx = 5, pady = 5)
Brocade_robesBQ = tk.StringVar()
Brocade_robes_BQ = tk.Label(monty02, font = fontsize, width = 5, bd = 3, textvariable = Brocade_robesBQ).grid(row = 13, column = 2, padx = 5, pady = 5)

    ###   輸出區(monty02) end   ###



    ###   列表區(monty03)   ###

        # Separator (v * 11格, h * 15格) 
Separator06 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 0, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator07 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 2, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator08 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 4, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator09 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 6, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator010 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 8, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator011 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 10, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator012 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 12, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator013 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 14, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator014 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 16, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator015 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 18, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator016 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 20, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator017 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 22, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator018 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 24, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator019 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 26, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator020 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 28, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator021 = ttk.Separator(monty03, orient = "vertical").grid(row = 0, column = 30, rowspan = 23, sticky = "ns", padx = 2, pady = 2)
Separator022 = ttk.Separator(monty03, orient = "horizontal").grid(row = 0, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator023 = ttk.Separator(monty03, orient = "horizontal").grid(row = 2, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator024 = ttk.Separator(monty03, orient = "horizontal").grid(row = 4, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator025 = ttk.Separator(monty03, orient = "horizontal").grid(row = 6, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator026 = ttk.Separator(monty03, orient = "horizontal").grid(row = 8, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator027 = ttk.Separator(monty03, orient = "horizontal").grid(row = 10, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator028 = ttk.Separator(monty03, orient = "horizontal").grid(row = 12, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator029 = ttk.Separator(monty03, orient = "horizontal").grid(row = 14, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator030 = ttk.Separator(monty03, orient = "horizontal").grid(row = 16, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator031 = ttk.Separator(monty03, orient = "horizontal").grid(row = 18, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator032 = ttk.Separator(monty03, orient = "horizontal").grid(row = 20, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)
Separator032 = ttk.Separator(monty03, orient = "horizontal").grid(row = 22, column = 0, columnspan = 31, sticky = "we", padx = 2, pady = 2)

        # Lable
BgFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 285).grid(row = 3, column = 3, padx = 5, pady = 5)
BgCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 500).grid(row = 3, column = 5, padx = 5, pady = 5)
BgPFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 5, column = 3, padx = 5, pady = 5)
BgPCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 5, column = 5, padx = 5, pady = 5)
PsFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 200).grid(row = 7, column = 3, padx = 5, pady = 5)
PsCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 340).grid(row = 7, column = 5, padx = 5, pady = 5)
PsPFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 9, column = 3, padx = 5, pady = 5)
PsPCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 60).grid(row = 9, column = 5, padx = 5, pady = 5)
CzFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 500).grid(row = 11, column = 3, padx = 5, pady = 5)
CzCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 340).grid(row = 11, column = 5, padx = 5, pady = 5)
CzSp = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 500).grid(row = 11, column = 7, padx = 5, pady = 5)
CzLg = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 476).grid(row = 11, column = 9, padx = 5, pady = 5)
CzPFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 13, column = 3, padx = 5, pady = 5)
CzPCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 13, column = 5, padx = 5, pady = 5)
CzPSp = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 13, column = 7, padx = 5, pady = 5)
CzPLg = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 13, column = 9, padx = 5, pady = 5)
PaFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 909).grid(row = 15, column = 3, padx = 5, pady = 5)
PaCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 652).grid(row = 15, column = 5, padx = 5, pady = 5)
PaSp = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 909).grid(row = 15, column = 7, padx = 5, pady = 5)
PaLg = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1052).grid(row = 15, column = 9, padx = 5, pady = 5)
PaBr = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 727).grid(row = 15, column = 11, padx = 5, pady = 5)
PaBe = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 625).grid(row = 15, column = 13, padx = 5, pady = 5)
PaLj = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1428).grid(row = 15, column = 15, padx = 5, pady = 5)
PaBo = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1875).grid(row = 15, column = 17, padx = 5, pady = 5)
PaCa = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 2500).grid(row = 15, column = 27, padx = 5, pady = 5)
PaPFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 17, column = 3, padx = 5, pady = 5)
PaPCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 17, column = 5, padx = 5, pady = 5)
PaPSp = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 17, column = 7, padx = 5, pady = 5)
PaPLg = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 17, column = 9, padx = 5, pady = 5)
PaPBr = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 17, column = 11, padx = 5, pady = 5)
PaPBe = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 510).grid(row = 17, column = 13, padx = 5, pady = 5)
PaPLj = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 690).grid(row = 17, column = 15, padx = 5, pady = 5)
PaPBo = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 940).grid(row = 17, column = 17, padx = 5, pady = 5)
PaPCa = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 17, column = 27, padx = 5, pady = 5)
NbFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1250).grid(row = 19, column = 3, padx = 5, pady = 5)
NbCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1153).grid(row = 19, column = 5, padx = 5, pady = 5)
NbSp = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1250).grid(row = 19, column = 7, padx = 5, pady = 5)
NbLg = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 2500).grid(row = 19, column = 9, padx = 5, pady = 5)
NbBr = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1025).grid(row = 19, column = 11, padx = 5, pady = 5)
NbBe = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1071).grid(row = 19, column = 13, padx = 5, pady = 5)
NbLj = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 2500).grid(row = 19, column = 15, padx = 5, pady = 5)
NbBo = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 3333).grid(row = 19, column = 17, padx = 5, pady = 5)
NbMe = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1136).grid(row = 19, column = 19, padx = 5, pady = 5)
NbFc = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1562).grid(row = 19, column = 21, padx = 5, pady = 5)
NbWi = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1000).grid(row = 19, column = 23, padx = 5, pady = 5)
NbGl = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1709).grid(row = 19, column = 25, padx = 5, pady = 5)
NbCa = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 3333).grid(row = 19, column = 27, padx = 5, pady = 5)
NbBr = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 2112).grid(row = 19, column = 29, padx = 5, pady = 5)
NbPFs = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 21, column = 3, padx = 5, pady = 5)
NbPCd = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 21, column = 5, padx = 5, pady = 5)
NbPSp = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 21, column = 7, padx = 5, pady = 5)
NbPLg = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 21, column = 9, padx = 5, pady = 5)
NbPBr = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 21, column = 11, padx = 5, pady = 5)
NbPBe = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 21, column = 13, padx = 5, pady = 5)
NbPLj = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 21, column = 15, padx = 5, pady = 5)
NbPBo = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 21, column = 17, padx = 5, pady = 5)
NbPMe = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1).grid(row = 21, column = 19, padx = 5, pady = 5)
NbPFc = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 950).grid(row = 21, column = 21, padx = 5, pady = 5)
NbPWi = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 1500).grid(row = 21, column = 23, padx = 5, pady = 5)
NbPGl = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 2200).grid(row = 21, column = 25, padx = 5, pady = 5)
NbPCa = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 3000).grid(row = 21, column = 27, padx = 5, pady = 5)
NbPBr = tk.Label(monty03, font = fontsize, width = 4, bd = 3, text = 4000).grid(row = 21, column = 29, padx = 5, pady = 5)

        # Image
Fish2 = tk.Label(monty03, image = Fish_image, relief = "ridge")
Fish2.grid(row = 1, column = 3, padx = 5, pady = 5)
Cider2 = tk.Label(monty03, image = Cider_image, relief = "ridge")
Cider2.grid(row = 1, column = 5, padx = 5, pady = 5)
Spices2 = tk.Label(monty03, image = Spices_image, relief = "ridge")
Spices2.grid(row = 1, column = 7, padx = 5, pady = 5)
Linen_garments2 = tk.Label(monty03, image = Linen_garments_image, relief = "ridge")
Linen_garments2.grid(row = 1, column = 9, padx = 5, pady = 5)
Bread2 = tk.Label(monty03, image = Bread_image, relief = "ridge")
Bread2.grid(row = 1, column = 11, padx = 5, pady = 5)
Beer2 = tk.Label(monty03, image = Beer_image, relief = "ridge")
Beer2.grid(row = 1, column = 13, padx = 5, pady = 5)
Leather_jerkins2 = tk.Label(monty03, image = Leather_jerkins_image, relief = "ridge")
Leather_jerkins2.grid(row = 1, column = 15, padx = 5, pady = 5)
Books2 = tk.Label(monty03, image = Books_image, relief = "ridge")
Books2.grid(row = 1, column = 17, padx = 5, pady = 5)
Meat2 = tk.Label(monty03, image = Meat_image, relief = "ridge")
Meat2.grid(row = 1, column = 19, padx = 5, pady = 5)
Fur_coats2 = tk.Label(monty03, image = Fur_coats_image, relief = "ridge")
Fur_coats2.grid(row = 1, column = 21, padx = 5, pady = 5)
Wine2 = tk.Label(monty03, image = Wine_image, relief = "ridge")
Wine2.grid(row = 1, column = 23, padx = 5, pady = 5)
Glasses2 = tk.Label(monty03, image = Glasses_image, relief = "ridge")
Glasses2.grid(row = 1, column = 25, padx = 5, pady = 5)
Candlestick2 = tk.Label(monty03, image = Candlestick_image, relief = "ridge")
Candlestick2.grid(row = 1, column = 27, padx = 5, pady = 5)
Brocade_robes2 = tk.Label(monty03, image = Brocade_robes_image, relief = "ridge")
Brocade_robes2.grid(row = 1, column = 29, padx = 5, pady = 5)

Begger2 = tk.Label(monty03, image = Begger_image, relief = "ridge")
Begger2.grid(row = 3, column = 1, padx = 5, pady = 5)
Begger_PI2 = tk.Label(monty03, image = People_image, relief = "ridge").grid(row = 5, column = 1, padx = 5, pady = 5)
Peasants2 = tk.Label(monty03, image = Peasants_image, relief = "ridge")
Peasants2.grid(row = 7, column = 1, padx = 5, pady = 5)
Peasants_PI2 = tk.Label(monty03, image = People_image, relief = "ridge").grid(row = 9, column = 1, padx = 5, pady = 5)
Citizens2 = tk.Label(monty03, image = Citizens_image, relief = "ridge")
Citizens2.grid(row = 11, column = 1, padx = 5, pady = 5)
Citizens_PI2 = tk.Label(monty03, image = People_image, relief = "ridge").grid(row = 13, column = 1, padx = 5, pady = 5)
Patrician2 = tk.Label(monty03, image = Patrician_image, relief = "ridge")
Patrician2.grid(row = 15, column = 1, padx = 5, pady = 5)
Patrician_PI2 = tk.Label(monty03, image = People_image, relief = "ridge").grid(row = 17, column = 1, padx = 5, pady = 5)
Nobleman2 = tk.Label(monty03, image = Nobleman_image, relief = "ridge")
Nobleman2.grid(row = 19, column = 1, padx = 5, pady = 5)
Nobleman_PI2 = tk.Label(monty03, image = People_image, relief = "ridge").grid(row = 21, column = 1, padx = 5, pady = 5)

            # Image Tool Tips
Fish2TT = CreateToolTip(Fish2, "魚肉")
Cider2TT = CreateToolTip(Cider2, "果汁")
Spices2TT = CreateToolTip(Spices2, "香料")
Linen_garments2TT = CreateToolTip(Linen_garments2, "亞麻服裝")
Bread2TT = CreateToolTip(Bread2, "麵包")
Beer2TT = CreateToolTip(Beer2, "啤酒")
Leather_jerkins2TT = CreateToolTip(Leather_jerkins2, "皮革上衣")
Books2TT = CreateToolTip(Books2, "書籍")
Meat2TT = CreateToolTip(Meat2, "醃肉")
Fur_coats2TT = CreateToolTip(Fur_coats2, "毛皮大氅")
Wine2TT = CreateToolTip(Wine2, "葡萄酒")
Glasses2TT = CreateToolTip(Glasses2, "眼鏡")
Candlestick2TT = CreateToolTip(Candlestick2, "燭台")
Brocade_robes2TT = CreateToolTip(Brocade_robes2, "金縷衣")

Begger2TT = CreateToolTip(Begger2, "乞丐")
Peasants2TT = CreateToolTip(Peasants2, "農民")
Citizens2TT = CreateToolTip(Citizens2, "市民")
Patrician2TT = CreateToolTip(Patrician2, "紳士")
Nobleman2TT = CreateToolTip(Nobleman2, "貴族")

        ###   列表區(monty03) end   ###


#####     貴族區 end     #####



root.mainloop()



