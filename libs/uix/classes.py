from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDFlatButton
from kivymd.uix.dialog import MDDialog


class RoundButton(MDFillRoundFlatButton):
    padding = [0, dp(20), 0, dp(20)]
    _radius = dp(20), dp(20)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(primary_hue=self.update_md_bg_color)


class RoundIconButton(MDFillRoundFlatIconButton):
    _radius = dp(20)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(primary_hue=self.update_md_bg_color)

    def update_text_color(self, *args):
        if self.text_color in (
                [0.0, 0.0, 0.0, 0.87],
                [0.0, 0.0, 0.0, 1.0],
                [1.0, 1.0, 1.0, 1.0],
        ):
            self.text_color = [1, 1, 1, 1]

    def update_icon_color(self, interval):
        if not self.icon_color:
            self.icon_color = [1, 1, 1, 1]

    def update_md_bg_color(self, instance, value):
        super().update_md_bg_color(instance, value)
        self.icon_color = [1, 1, 1, 1]


class Dialog(MDDialog):
    radius = [dp(30)] * 4

    def update_bg_color(self, *args):
        self.md_bg_color = MDApp.get_running_app().primary_accent

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = MDApp.get_running_app().primary_accent
        self.theme_cls.bind(theme_style=self.update_bg_color)


class DialogButton(MDFlatButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_text_color = "Custom"
        self.font_name = "RobotoMedium"
        self.font_size = "16sp"
        self.text_color = self.theme_cls.primary_color


class CheckboxLabel(ThemableBehavior, RectangularRippleBehavior, MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_color = self.theme_cls.primary_light
        self.ripple_alpha = .2