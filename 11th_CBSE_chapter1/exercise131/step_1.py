from manim import *
config.background_color = WHITE
config.frame_width =15
config.frame_height =10
config.pixel_width = 3000
config.pixel_height = 3000
class Exercise131(Scene):
    def construct(self):

        box = Rectangle(width=7,height=3,stroke_width=3,color=BLACK)
        line1 = MathTex(r"\subset ", color=BLACK)
        text1 = Text("is a subset", font_size=30,color=BLACK).next_to(line1, RIGHT)
        line2 = MathTex(r" \not\subset ", color=BLACK)
        text2 = Text("is not a subset", font_size=30,color=BLACK).next_to(line2, RIGHT)
        line3 = MathTex(r"A \subset B", color=BLACK)
        text3 = Text("All elements of A are in B", font_size=30,color=BLACK).next_to(line3, RIGHT)
        group = VGroup(VGroup(line1, text1),
                       VGroup(line2, text2),
                       VGroup(line3, text3)).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        group.move_to(box.get_center())
        self.add(box, group)