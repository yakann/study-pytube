from pytube import YouTube
from tkinter import Tk
from tkinter import filedialog


class download:
    def __init__(self, res, only_audio, progressive, path):
        self.res = res
        self.only_audio = only_audio
        self.progressive = progressive
        self.path = path
    def main_function(self):
        yt = YouTube(self.path)
        stream = yt.streams.filter(res=self.res, file_extension='mp4', only_audio=self.only_audio, progressive=self.progressive).first()
        stream.download(self.get_path())

    def show(self):
        yt = YouTube(self.path)
        for i in yt.streams.filter(res=self.res, file_extension='mp4', only_audio=self.only_audio, progressive=self.progressive):
            print(i)
        print('bittii')
    
    def get_path(self):
        
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        return str(filedialog.askdirectory())


"""
Tkinter ile belge seçme
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

"""