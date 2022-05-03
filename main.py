# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% import packages

import tkinter as tk #tkinter is a GUI-Library for python
import settings
import utils


   
#%% initialize window
root = Tk() #initialize root window (would also bei initialized once I create first widget)
#set settings for window
root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}') #create size for root window
root.title('Minesweeper') #create title for root window
root.resizable(False, False) #prohibit resizing of width and height of window

top_frame=Frame(
        root,
        bg='black',
        width=settings.width,
        height=utils.height_perc(25)) #create the topframe
top_frame.place(x=0,y=0) #place top frame at coordinates 0,0

left_frame=Frame(
        root,
        bg='black',
        width=utils.width_perc(25),
        height=utils.height_perc(75))
left_frame.place(x=0,y=utils.height_perc(25))

center_frame=Frame(
        root,
        bg='black',
        width=utils.width_perc(75),
        height=utils.height_perc(75))
center_frame.place(x=utils.width_perc(25),y=utils.height_perc(25))
root.mainloop()