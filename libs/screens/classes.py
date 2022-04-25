from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.modalview import ModalView
from kivymd.uix.snackbar import Snackbar

from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import (
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
    MDFlatButton,
)
from kivymd.uix.dialog import MDDialog


class LoadingScreen(ModalView):
    is_open = False
    Builder.load_string("""
<LoadingScreen>:
    auto_dismiss: False
    background_color: 0, 0, 0, 0
    overlay_color: 0, 0, 0, 0.2
    text: "Checking..." 
    FloatLayout:
        MDLabel:
            font_size:"40dp"
            font_name:"Poppins"
            theme_text_color:"Custom"
            pos_hint:{"center_y":.5}
            text_color: app.text_color
            halign:"center"
            text:root.text   
    """
    )

    def on_open(self):
        self.is_open = True
        super().on_open()

    def on_dismiss(self):
        self.is_open = False
        super().on_dismiss()


class RoundButton(MDFillRoundFlatButton):
    Builder.load_string("""
<RoundButton>
	canvas:
		RoundedRectangle:
			size: self.size
			pos: self.pos
			radius:self._radius
			texture: Gradient.horizontal([1,1,1,0], [1,1,1,.2])
"""
    )
    padding = [0, dp(20), 0, dp(20)]
    _radius = dp(25), dp(25)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(primary_hue=self.update_md_bg_color)


class RoundIconButton(MDFillRoundFlatIconButton):
    _radius = dp(20)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.bind(primary_hue=self.update_md_bg_color)


# ------- The below string loads the update dialog box content --------
Builder.load_string("""
<UpdateContent@MDBoxLayout>
    adaptive_height: True
    padding: 0, dp(15), 0, 0
    orientation: "vertical"
    spacing: "5dp"
    MDTextField:
        id: name
        hint_text: "Name"
    MDTextField:
        id: password
        hint_text: "Password"
"""
)


class Dialog(MDDialog):
    radius = [dp(30)] * 4

    def update_bg_color(self, *args):
        self.md_bg_color = MDApp.get_running_app().primary_accent

    # def update_title_color(self, *args):
    #     self.title_color = MDApp.get_running_app().text_color

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.update_title_color()
        self.md_bg_color = MDApp.get_running_app().primary_accent
        self.theme_cls.bind(theme_style=self.update_bg_color)
        # self.theme_cls.bind(theme_style=self.update_title_color)


class DialogButton(MDFlatButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_text_color = "Custom"
        self.font_name = "RobotoMedium"
        self.font_size = "16sp"
        self.text_color = self.theme_cls.primary_color


class CheckboxLabel(ThemableBehavior, RectangularRippleBehavior, MDBoxLayout):
    Builder.load_string("""
<ButtonLabel@ButtonBehavior+MDLabel>
<CheckboxLabel>
	adaptive_size:True
	size_hint_x:.8
	pos_hint: {'center_x': .5}
	spacing:'12dp'
	on_active: None
    active: True
	radius:dp(5),dp(5)
	text:''
	MDCheckbox:
		id: check
		size_hint: None, None
		size: "36dp", "36dp"
        active: root.active
		selected_color:app.theme_cls.primary_light
		unselected_color: [.8,.8,.8,1]
        on_active: 
            root.active = check.active
		pos_hint: {'center_x': .5}
	ButtonLabel:
        theme_text_color:"Custom"
        text_color:app.text_color
		on_release:
			check.active = not check.active
		text: root.text
"""
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ripple_color = self.theme_cls.primary_light
        self.ripple_alpha = 0.2


class CustomSnackbar(Snackbar):
    is_open = False

    def on_open(self, *args):
        self.is_open = True

    def on_leave(self):
        self.is_open = False
