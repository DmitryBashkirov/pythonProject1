from kivy.animation import Animation
from kivy.lang import Builder

from kivymd.app import MDApp


KV = """
<CommonLabel@MDLabel>
    opacity: 0
    adaptive_height: True
    halign: "center"
    y: -self.height

MDScreen:
    on_touch_down: app.start_animation()

    CommonLabel:
        id: lbl_1
        font_size: "50sp"
        text: "Y O U"

    CommonLabel:
        id: lbl_2
        font_size: "50sp"
        text: "P I D R"
"""


class TestAnimation(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def complete_animation(self, animation, animated_instance):
        """
        :type animation: <kivy.animation.Animation object>
        :type animated_instance: <WeakProxy to <kivy.factory.CommonLabel object>>
        """

        # Анимируем масштаб и цвет первой метки.
        #Animation(scale=1.4, d=1, t="in_out_back").start(animated_instance)
        Animation(color=(1, 0, 1, 1), d=1).start(animated_instance)

    def start_animation(self):
        # Получаем объекты меток из KV разметки
        lbl_1 = self.root.ids.lbl_1
        lbl_2 = self.root.ids.lbl_2
        animation = Animation(
            opacity=1, y= lbl_1.height*4.5, d=1, t="linear"
        )
        animation.bind(on_complete=self.complete_animation)
        animation.start(lbl_1)
        animation = Animation(
            opacity=1, y=lbl_1.height * 5.5, d=3, t="linear"
        )
        animation.bind(on_complete=self.complete_animation)
        animation.start(lbl_2)

TestAnimation().run()
