# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

import tkinter as tk #tkinter is a GUI-Library for python

#%%
width=720
height=400
root = Tk() #initialize root window (would also bei initialized once I create first widget)
root.configure(bg="black")
root.geometry(str(width)+'x'+str(height)) #create size for root window
root.title('Minesweeper') #create title for root window
root.resizable(False, False) #prohibit resizing of width and height of window
top_frame=Frame(
        root,
        bg='red',
        width=width,
        height=height/4) #create the topframe
top_frame.place(x=0,y=0) #place top frame at coordinates 0,0
root.mainloop()