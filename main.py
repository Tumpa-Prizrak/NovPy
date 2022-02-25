from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class TestApp(App):
    def build(self):
        return Builder.load_file("Markup.np")

TestApp().run()