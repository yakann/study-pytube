from pytube import YouTube
import download
from choise_folder import choise_folder


def islem():
    work_object = download
    work_object.download(res, only_audio, progressive, yt).show()
    work_object.download(res, only_audio, progressive, yt).main_function()

def choise_link():
    return input('İşlem yapmak istediğiniz linki buraya yapıştırın: ')
# İndirileceği yeri sabitleme++
# İndirileceği yeri seçme ++
# Görüntü kalitelerini gösterme
# Ana işlemin yapıldığı yeri farklı bir classa çekme ++
if __name__ == "__main__":
    yt = choise_link()
    res = '720p'
    only_audio = False
    progressive = True

    while True:
        print("""
        Yapmak istediğiniz işlemi seçin.

        Video olarak indir(1)
        Ses dosyası olarak indir(2)

        İndirilecek yeri seçmek(s)

        Farklı bir link indirmek için(3)
        Çıkmak için (q)'ya basın.
        """)
        
        inp = input()
        if inp == 's':
            choise_folder().set_path()
        if inp == 'q':
            break
        if inp == '3':
            yt = choise_link()
        if inp == '1':
            res = input('Video kalitesini girin: ')+'p'
            only_audio=False
            if input('Videoda ses olsun mu?(e/h)') == 'h':
                progressive = False
            islem()
        elif inp == '2':
            only_audio=True
            progressive = False
            res = ''
            islem()

