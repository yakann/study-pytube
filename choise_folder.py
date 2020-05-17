from tkinter import Tk
from tkinter import filedialog

class choise_folder:
    def set_path(self): #Dosya yolu belirleyen method
            
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        path = str(filedialog.askdirectory())
        #save txt
        ths = open("path.txt", "w")
        ths.write(path)
        ths.close()

    def get_path(self): #
        ths = open("path.txt", "r")
        return ths.read()