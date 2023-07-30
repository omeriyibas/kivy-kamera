import json

import requests
from camera4kivy import Preview
from kivy.clock import mainthread
from kivy.graphics.texture import Texture


class PreviewCamera(Preview):

    def analyze_pixels_callback(self, pixels, image_size, image_pos,
                                image_scale, mirror):

        # print(mirror)

        self.pixels=pixels
        self.image_size=image_size

# @mainthread
    # def make_thread_safe(self, pixels, size):
    #     # print(pixels)
    #     if not self.analyzed_texture or \
    #             self.analyzed_texture.size[0] != size[0] or \
    #             self.analyzed_texture.size[1] != size[1]:
    #         self.analyzed_texture = Texture.create(size=size, colorfmt='rgba')
    #         self.analyzed_texture.flip_vertical()
    #     self.analyzed_texture.blit_buffer(pixels, colorfmt='rgba')
