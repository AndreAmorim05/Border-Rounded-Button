from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.core.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.texture import Texture
from kivy.core.image import Image as CoreImage
import os

# ainda preciso descobrir pra que serve essa biblioteca
from kivy.graphics.instructions import *

_image_dir = os.path.join(os.path.dirname(__file__), 'images')


class BoderRoundedButton(ButtonBehavior, Label):
    source_image = StringProperty('')
    image_color = StringProperty('#2c3436')
    image_state = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(BoderRoundedButton, self).__init__(**kwargs)
        self.tex = Texture.create(size=(137, 80), colorfmt='rgba')
        self._scr_image = ''
        self.draw_button()

    def on_source_image(self, *args):
        self._scr_image = self.source_image
        full_path = os.path.join(_image_dir, self._scr_image)
        if os.path.isfile(full_path):
            self._scr_image = full_path
        self.draw_button(*args)

    def on_pos(self, *args):
        self.draw_button()

    def on_size(self, *args):
        self.draw_button()

    def on_state(self, *args):
        self.draw_button()


    # def _draw_label(self, *args):
    #     self._labelIG.clear()
    #     if not self.label and not self.label_icon:
    #         return

    def on_image_color(self, *args):
        self.draw_button()

    def on_image_state(self, *args):
        self.draw_button()



    def draw_button(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # trocar cor não funcionou
            Color(rgba=((get_color_from_hex('2BD62B') if self.state == 'normal' else get_color_from_hex('219321'))))
            Ellipse(size=(self.height, self.height),
                    pos=self.pos)
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height),
                      pos=(self.x + self.height/2.0, self.y))

            if self.image_state:
                Color(rgba = get_color_from_hex(self.image_color))
                Rectangle(pos=(self.x + self.height/4, self.y + self.height * 0.3),
                      size=(self.height * 0.4, self.height * 0.4),
                      source= self._scr_image)
                # self.text_size = self.width - self.height * 0.4


# cor do ícone do botão F5F6F2
