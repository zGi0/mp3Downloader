from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from yt_dlp import YoutubeDL
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.my_input = TextInput(text='Digite aqui')

        self.bColar = Button(text='Colar')
        self.bColar.bind(on_press=self.paste_text)

        self.bDownload = Button(text='Download')
        self.bDownload.bind(on_press= self.prepararDownload) # funcionalidade do botão download
        
        # popup
        self.popup = Popup(title='fodeu')

        self.add_widget(self.my_input)
        self.add_widget(self.bColar)
        self.add_widget(self.bDownload)

    def paste_text(self, instance):
        self.my_input.text = Clipboard.paste()
        
        
    def downloadDefinitivo(self, url_registrada): # formata e realiza o download

        # dicionário com as opções do arquivo
        options = {
            'outtmpl': '%(title)s.%(ext)s',
            'format': 'mp3/bestaudio/best',
            'postprocessors': [{  # extraindo e processando o áudio usando o ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
        }

        
        with YoutubeDL(options) as ydl:
            try:
                ydl.download(url_registrada)
            except Exception as ex:
                self.popup.content = Label(text=ex)
                self.popup.open()
    
    
    def prepararDownload(self, url_musica): # desabilita botões e chama o download
        url_musica = self.my_input.text
        self.downloadDefinitivo(url_musica)
        

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()