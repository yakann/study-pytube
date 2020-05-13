from pytube import YouTube

def mainee(res2, only_audio2, progressive2):
    yt = YouTube(input('İşlem yapmak istediğiniz linki buraya yapıştırın: '))
    for i in yt.streams.filter(res=res2, file_extension='mp4', only_audio=only_audio2, progressive=progressive2):
        print(i)

    ##stream = yt.streams.filter(only_audio=True , file_extension='mp4').first()
    ##stream.download('C:/Users/mahmu/OneDrive/Masaüstü')
    print('bittii')

if __name__ == "__main__":
    
    res = '720p'
    only_audio = False
    progressive = True
    print("""
    Yapmak istediğiniz işlemi seçin.

    Video olarak indir(1)
    Ses dosyası olarak indir(2)

    """)
    
    inp = input()
    if inp == '1':
        res = input('Video kalitesini girin: ')+'p'
        only_audio=False
        if input('Videoda ses olsun mu?(e/h)') == 'h':
            progressive = False
    elif inp == '2':
        only_audio=True
        progressive = False
        res = ''
    mainee(res, only_audio, progressive)