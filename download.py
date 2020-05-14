from pytube import YouTube

class download:
    def __init__(self, res, only_audio, progressive, path):
        self.res = res
        self.only_audio = only_audio
        self.progressive = progressive
        self.path = path
    def main_function(self):
        yt = YouTube(self.path)
        for i in yt.streams.filter(res=self.res, file_extension='mp4', only_audio=self.only_audio, progressive=self.progressive):
            print(i)
        print('bittii')