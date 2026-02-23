from manim import *

config.frame_height = 10
config.frame_width = 40
config.pixel_width = 2800
config.pixel_height = 2800

class Question9515(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        q_image = ImageMobject("question1.png")
        q_image.scale(2.9)
        self.add(q_image)