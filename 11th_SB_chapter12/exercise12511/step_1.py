from manim import *

from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500
config.background_color=WHITE

class Exercise12511(Scene):
    def construct(self):

        circle = Circle(radius=3.5,color=BLACK,stroke_width=4)
        circle2 = Circle(radius=1.5,color=BLACK,stroke_width=4)
        label = Text("A", color=BLACK)
        label.move_to(circle.get_center())
        label2 = Text("B", color=BLACK)
        label2.move_to(circle2).shift(RIGHT*3+UP)

        self.add(circle,circle2,label,label2)