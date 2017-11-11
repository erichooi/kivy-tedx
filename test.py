import os
os.environ["KIVY_VIDEO"] = "ffpyplayer"
from kivy.uix.videoplayer import VideoPlayer
from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string("""
VideoPlayer:
    source: "small.mp4"
""")

class testApp(App):
    def build(self):
        return root

if __name__ == "__main__":
    testApp().run()
