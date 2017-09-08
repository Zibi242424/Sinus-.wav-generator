from tkinter import *
import os
from config import runApp

class GUI(Frame):
    
    
    def __init__(self,master=None):
        Frame.__init__(self, master)        
        self.grid()
        
        
        self.filenameLabel = Label(master, text="File Name")
        self.filenameLabel.config(font=("Times New Roman", 15))
        self.filenameLabel.grid()

        self.filenameEntry = StringVar()
        self.filenameEntry = Entry(textvariable=self.filenameEntry, width=80)
        self.filenameEntry.grid()

        self.freq1Label = Label(master, text="Put frequency no. 1 here [Hz] (left channel")
        self.freq1Label.config(font=("Times New Roman", 15))
        self.freq1Label.grid()

        self.freq1Entry = IntVar()
        self.freq1Entry = Entry(textvariable=self.freq1Entry, width=80)        
        self.freq1Entry.grid()

        self.freq2Label = Label(master, text="Put frequency no. 2 here [Hz] (right channel)")
        self.freq2Label.config(font=("Times New Roman", 15))
        self.freq2Label.grid()

        self.freq2Entry = IntVar()
        self.freq2Entry = Entry(textvariable=self.freq2Entry, width=80)
        self.freq2Entry.grid()

        self.timeLabel = Label(master, text="Duration time [s]")
        self.timeLabel.config(font=("Times New Roman", 15))
        self.timeLabel.grid()

        self.timeEntry = IntVar()
        self.timeEntry = Entry(textvariable=self.timeEntry, width=80)
        self.timeEntry.grid()

        def returnSpecs():
            self.specs = {"filename": self.filenameEntry.get(), "freq_1": self.freq1Entry.get(),\
            "freq_2": self.freq2Entry.get(), "time": self.timeEntry.get()}
            return self.specs        
        
        self.submitButton = Button(master, text="Submit", command=lambda: runApp(returnSpecs()))
        self.submitButton.grid()
