# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 08:48:43 2018

@author: hp
"""

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from threading import Thread

#to convert to text to speech
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("hello")
speak.Speak("welcome to Voice Syntesizer")

#creation of GUI windows
root=Tk()

#giving title of windows
root.title("Text to Speech Synthesizer")

#defining function whatever written in textAREA BOX is speak
#after speaking ,delete that wriiten text
def callback1():
    speak.Speak(entry.get('1.0',END))
    entry.delete('1.0',END)
    
    
    
#to prevent the app on fREEZE  
def threading1():
    t1=Thread(target=callback1)
    t1.start()


#for text areaa scroll bar    
entry=scrolledtext.ScrolledText(root,width=30,height=10,wrap=WORD)
entry.grid(row=0,column=0)

#to create SPEAK button
button=ttk.Button(root,text='SPEAK',command=threading1)
button.grid(row=0,column=1,sticky=N)

#to focus the written bar in text area box
entry.focus()
root.mainloop()