import kivy.app
import kivy.lang

class _TestApp(kivy.app.App):
    def __init__(self, file: str):
        super().__init__()
        self.justuniquename = file

    def build(self):
        return kivy.lang.Builder.load_file(self.justuniquename)

class screen:
    def __init__(self, *, markupFile: str):
        self.__class = _TestApp(markupFile)
    
    def start(self):
        self.__class.run()