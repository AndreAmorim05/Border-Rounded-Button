from kivy.app import App
#from border_rounded_bt import *
from button_style import ButtonStyle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

Builder.load_string('''

#:import ButtonStyle button_style.ButtonStyle
#:import BRB border_rounded_bt.BoderRoundedButton


<Manager>:
    Botao:

<Botao>:
    FloatLayout:

        BoxLayout:
            orientation: 'vertical'
            size_hint: (.5,.3)
            pos_hint: {'center_x':.5, 'center_y':.5}
            spacing: '5dp'

            ButtonStyle:
                source_image: 'images/book.png'
                on_release: self.source_image = 'images/book.png' if self.source_image != 'images/book.png' else 'images/book_alterado.png'

            BoderRoundedButton:
                id: brdbt
                text: 'Botao de teste Arredondado AAAAAAAAAAAAAAABBBBBBBBBBBBBCCCCCCCCCCCCC'
                source_image: 'images/book.png'
                bold: True
                text_size: self.width, None
                size_hint: 1, 1
                halign: 'center'
                valign: 'center'
                height: self.texture_size[1]
                on_release: self.source_image = 'images/book.png' if self.source_image != 'images/book.png' else 'images/book_alterado.png'


        BoxLayout:
            size_hint: .6,.075
            pos_hint: {'center_x':.5, 'botton':.9}
            spacing: '5dp'
            TextInput:
                id: texinp
            Button:
                size_hint_x: .4
                text: 'Mudar Cor'
                on_release: brdbt.image_color = texinp.text if texinp.text != '' else brdbt.image_color
            Button:
                size_hint_x: .2
                text: 'Imagem'
                on_release: brdbt.image_state = True if brdbt.image_state == False else False




''')



class Manager(ScreenManager):
    pass

class Botao(Screen):
    # layout = FloatLayout()
    # # botao = BoderRoundedButton(source_image='images/book.png', pos_hint={'center_x':.5, 'center_y':.5}, size_hint=(.5,.5))
    # botao = ButtonStyle(source_image='images/book.png', pos_hint={'center_x':.5, 'center_y':.5}, size_hint=(.5,.5))
    # layout.add_widget(botao)
    # return layout
    pass

class Principal(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    Principal().run()
