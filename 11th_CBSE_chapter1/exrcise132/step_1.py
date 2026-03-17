from manim import *
config.background_color = WHITE
config.frame_width =15
config.frame_height =10
config.pixel_width = 3000
config.pixel_height = 3000
class Exeecise132(Scene):
    def construct(self):

        box =Rectangle(width=3.5,height=3.2,stroke_width=3,color=BLACK)
        line1 = MathTex(r"\subset ", color=BLACK)
        text1 = Text("is a subset", font_size=30,color=BLACK).next_to(line1, RIGHT)
        line2 = MathTex(r" \not\subset ", color=BLACK)
        text2 = Text("is not a subset", font_size=30,color=BLACK).next_to(line2, RIGHT)
        line3 = MathTex(r" \in ", color=BLACK)
        text3 = Text("belongs to", font_size=30,color=BLACK).next_to(line3, RIGHT)
        line4 = MathTex(r" \notin ", color=BLACK)
        text4 = Text("not belongs to", font_size=30,color=BLACK).next_to(line4, RIGHT)
        group = VGroup(VGroup(line1, text1),
                       VGroup(line2, text2),
                       VGroup(line3, text3),
                       VGroup(line4, text4)).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        group.move_to(box.get_center())
        self.add(box, group)