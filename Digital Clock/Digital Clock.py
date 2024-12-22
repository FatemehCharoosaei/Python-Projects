# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:18:20 2023

@author: sara
"""

import tkinter as tk
from time import strftime

bg_color = "white"
fg_color = "darkviolet"


window = tk.Tk()
window.geometry('100x100')
window.configure(background=bg_color)
window.title("Digital Clock")


def show_time():
    text = strftime("%H:%M:%S")
    lbl.config(text=text)
    lbl.after(1000, show_time)
    
lbl = tk.Label(window,
               font = ("digital-7", 35, "bold"),
               background = bg_color,
               foreground = fg_color)

lbl.pack(anchor="center")

show_time()

tk.mainloop()    