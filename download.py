from pytube import YouTube
from choise_folder import choise_folder


class download:
    def __init__(self, res, only_audio, progressive, path):
        self.res = res
        self.only_audio = only_audio
        self.progressive = progressive
        self.path = path
    def main_function(self):
        yt = YouTube(self.path)
        stream = yt.streams.filter(res=self.res, file_extension='mp4', only_audio=self.only_audio, progressive=self.progressive).first()
        stream.download(choise_folder().get_path())

    def show(self):
        yt = YouTube(self.path)
        for i in yt.streams.filter(res=self.res, file_extension='mp4', only_audio=self.only_audio, progressive=self.progressive):
            print(i)
        print('bittii')


"""
Tkinter ile belge seçme
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

"""