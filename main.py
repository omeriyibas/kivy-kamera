from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp

from screens.CameraScreen.CameraScreen import CameraScreen

import camera4kivy.preview


class MyApp(MDApp):
    sm = ScreenManager()
    # is_android = get_platform() == "android"

    def load_design(self):
        self.load_kv("screens/CameraScreen/CameraScreen.kv")

    def add_screens(self):
        camera_screen = CameraScreen(name="camera_screen")
        self.sm.add_widget(camera_screen)

    def build(self):

        self.load_design()

        self.add_screens()

        Window.bind(on_keyboard=self.key_input)

        # self.sm.current="init_screen"

        # self.sm.screens[-2]

        return self.sm

    def key_input(self, window, key, scancode, codepoint, modifier):
        if key == 27:
            # print(self.sm.current)
            # if self.sm.current != "main_screen" and self.sm.current != "user_screen" and self.sm.current != "login_register_screen" and self.sm.current != "agree_screen" and self.sm.current != "camera_screen" and self.sm.current!="drug_screen":
            #     self.sm.current = "main_screen"
            # elif self.sm.current=="drug_screen":
            #     self.sm.current="drug_list_screen"
            # elif self.sm.current == "camera_screen":
            #     self.sm.current = "user_screen"
            # elif self.sm.current == "user_screen":
            #     self.sm.get_screen("user_screen").ids.form.opacity = 1
            #     self.sm.get_screen("user_screen").ids.nav_drawer.set_state("close")
            return True
        else:
            return False


Window.size = (1080 // 3, 2340 // 3)
MyApp().run()

# if __name__ == '__main__':