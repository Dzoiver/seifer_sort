import tkinter as tk
from tkinter import filedialog
import os


class App:
    def __init__(self):
        self.HEIGHT = 150
        self.WIDTH = 400
        self.dir = ''
        self.application_window = tk.Tk()
        self.entry = tk.Entry()

    def dialog_open(self):
        self.dir = filedialog.askdirectory(parent=self.application_window,
                                           initialdir=os.getcwd(),
                                           title="Please select a folder:")
        self.entry.insert(0, self.dir)

    def sort(self):
        list_of_files = os.listdir(path=self.dir)
        print(list_of_files)
        for item in list_of_files:
            extension_start_index = item.find('.')
            extension_name = item[extension_start_index+1:]
            if not os.path.isdir(self.dir + '/' + item) and not os.path.exists(self.dir + '/' + extension_name):
                os.mkdir(self.dir + '/' + extension_name)
                print("Folder created")
            else:
                print("Didn't create a folder")
                print("os.path.exists = ", os.path.exists(self.dir + '/' + item))
            print(self.dir + '/' + extension_name)
            if os.path.exists(self.dir + '/' + extension_name) and not os.path.isdir(self.dir + '/' + item):
                os.replace(self.dir + '/' + item, self.dir + '/' + extension_name + '/' + item)

    def loop(self):
        canvas = tk.Canvas(self.application_window, height=self.HEIGHT, width=self.WIDTH)
        canvas.pack()

        frame = tk.Frame(self.application_window, bg='#7d9cce')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)

        bottom_frame = tk.Frame(self.application_window)
        bottom_frame.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)

        button_hello = tk.Button(frame, text="Choose", command=self.dialog_open)
        button_hello.pack(side='right', fill='both')

        button_action = tk.Button(bottom_frame, text="Sort", command=self.sort)
        button_action.pack(side='bottom')

        self.entry = tk.Entry(frame)
        self.entry.pack(side='bottom', fill='both')

        label = tk.Label(frame, text="Choose a path", bg='#7d9cce')
        label.pack(side='bottom', fill='both')
        self.application_window.mainloop()

