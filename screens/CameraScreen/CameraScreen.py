import base64
import json

import numpy as np
import requests
from camera4kivy import Preview
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp


class CameraScreen(Screen):

    def on_pre_enter(self, *args):
        self.ids.preview.connect_camera(enable_analyze_pixels=True,mirrored=False)

        self.ids.shot_btn.on_press=self.take_pic

        # Clock.schedule_once(self.analyze, 2)

    def take_pic(self):
        requests.post("http://127.0.0.1:5000/getefw", files={"pixels":self.ids.preview.pixels,"img_size":json.dumps(self.ids.preview.image_size)})


    def on_pre_leave(self, *args):
        self.ids.preview.disconnect()



class MyApp(MDApp):
    sm = ScreenManager()

    # Window.size = (1080, 2340)
    def build(self):
        self.load_kv("CameraScreen.kv")
        camera_screen = CameraScreen(name="camera_screen")
        self.sm.add_widget(camera_screen)

        return self.sm

    # def on_start(self):
    #     self.sm.get_screen("camera_screen").ids.preview.connect_camera(analyze_pixels_resolution = 720,
    #                                            enable_analyze_pixels = True)


if __name__ == '__main__':
    Window.size = (1080 // 3, 2340 // 3)
    MyApp().run()
