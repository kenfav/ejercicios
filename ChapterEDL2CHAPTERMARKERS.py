import csv
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Image Viewer')

root.filename = filedialog.askopenfilename(initialdir=".", title="Select a file", filetypes=[("Csv Files", "*.csv")])
