from TempClient import *
from Tkinter import *


class TempGui:
    def __init__(self):
        self.root = None
        self.temp_string = None
        self.temp_label = None
        self.connection = TempClient()
        self.connection.connect("192.168.1.13", "30000")
        self.build_gui()

    def build_gui(self):
        self.root = Tk()
        self.temp_string = StringVar()
        self.root.wm_title("Pi Temp")
        self.temp_label = Label(self.root, textvariable=self.temp_string)
        self.temp_label.config(font=("Courier", 44))
        self.temp_label.pack()

    def update_temp(self):
        if self.connection is not None:
            self.temp_string.set(self.connection.read())
        else:
            exit(1)
        self.root.update()
        self.root.after(1000, self.update_temp())

if __name__ == "__main__":
    gui = TempGui()
    gui.update_temp()
