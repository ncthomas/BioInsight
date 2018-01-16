import tkinter, MyMLFunctions
from tkinter import filedialog
import numpy as np
import pandas as pd

class BioInsight(tkinter.Tk):

    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialise()

    def initialise(self):

        ## TEXT
        #######
        self.txt = tkinter.Text(self)
        self.res = tkinter.Text(self)

        ## LABEL FRAMES
        ###############
        frameOpenSave = tkinter.LabelFrame(self, text=" Open/Save File ")
        frameAbout = tkinter.LabelFrame(self, text=" About ")
        frameResults = tkinter.LabelFrame(self, text=" Analysis ")

        ## LABELS
        #########
        aboutLabel = tkinter.Label(frameAbout, text=" Developed by: - Niclas Thomas niclas.thomas@gmail.com")
        openLabel = tkinter.Label(frameOpenSave, text="Open File:")
        saveLabel = tkinter.Label(frameOpenSave, text="Save File:")
        resultsLabel = tkinter.Label(frameResults, text='Results...')

        # BUTTONS AND ENTRY FIELDS
        ##########################
        openButton = tkinter.Button(frameOpenSave, text="Browse ...", command=self.onOpen)
        saveButton = tkinter.Button(frameOpenSave, text="Browse ...")
        svmButton = tkinter.Button(frameResults, text="Run SVM", command=self.GetResultsSVM)

        ## GRID LAYOUT
        ##############
        frameOpenSave.grid(row=0, column=0, columnspan=2, sticky='EW', padx=5, pady=5, ipadx=5, ipady=5)
        frameAbout.grid(row=2, column=0, columnspan=2, rowspan=2, padx=5, pady=5)
        frameResults.grid(row=1, column=0, columnspan=2, sticky='EW', padx=5, pady=5, ipadx=5, ipady=5)
        aboutLabel.grid(row=0)
        resultsLabel.grid(row=0)
        openButton.grid(row=0, column=1, sticky='E', padx=5, pady=2)
        saveButton.grid(row=1, column=1, sticky='E', padx=5, pady=2)
        openLabel.grid(row=0, column=0, sticky='W', padx=5, pady=2)
        saveLabel.grid(row=1, column=0, sticky='W', padx=5, pady=2)
        svmButton.grid(row=3, column=0, sticky='W', padx=5, pady=2)
        self.txt.grid(row=3, column=0, columnspan=2, sticky='W', padx=5, pady=2)
        self.res.grid(row=3, column=4, columnspan=2, sticky='W', padx=5, pady=2)


    ## OTHER FUNCTIONS
    ##################

    def onOpen(self):
        ftypes = [('CSV files', '*.csv'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        filename = dlg.show()
        if filename != '':
            fileText = self.readFile(filename)
            self.txt.config(state=tkinter.NORMAL)
            self.txt.delete("1.0", tkinter.END)
            self.txt.insert("1.0", fileText)
            self.data = pd.read_csv(filename)
            self.txt.config(state=tkinter.DISABLED)


    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text

    def GetResultsSVM(self):
        svmres = MyMLFunctions.MyMLLibrary().PerformSVM(self.data, cost=2)
        self.res.delete("1.0", tkinter.END)
        self.res.insert("1.0", svmres)

if __name__ == "__main__":
    app = BioInsight(None)
    app.title(' BioInsight ')
    app.mainloop()