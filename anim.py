from manim import *

config.background_color=WHITE

class Animation(Scene):
    def construct(self):
        #BLUE DOT
        dot_1=Dot([-2.5,-2.0,0],color="#2746F5").scale(2).set_z_index(10)
        label_1=Text("left",color=BLACK).next_to(dot_1,DOWN*1)
        #RED DOT
        dot_2=Dot([2.5,-2.0,0],color="#C8092F").scale(2).set_z_index(10)
        label_2=Text("right",color=BLACK).next_to(dot_2,DOWN*1)
        line_1=Line(start=[-2.5,-2.0,0],end=[2.5,-2.0,0],color=BLACK).set_stroke(width=5)
        #BLACK DOT
        dot_3=Dot([0,-2,0],color=BLACK).scale(2)
        dot_4=Dot([0,2,0],color=BLACK).scale(2)
        line_2=always_redraw(lambda:Line(dot_3.get_center(),end=dot_4.get_center(),color=BLACK).set_stroke(width=4).add_tip())
        label_3=Text("center",color=BLACK).next_to(dot_4,UP*1)
        line_3=always_redraw(lambda:Line(start=dot_4.get_center(),end=dot_1.get_center(),color=BLACK).set_stroke(width=4))
        line_4=always_redraw(lambda:Line(start=dot_4.get_center(),end=dot_2.get_center(),color=BLACK).set_stroke(width=4))

        self.play(FadeIn(dot_1,label_1))
        self.play(FadeIn(dot_2,label_2))

        self.play(FadeOut(label_1,label_2))
        self.play(Create(line_1))
        self.play(FadeIn(dot_3))

        self.play(Create(line_2),FadeIn(dot_4))
        self.play(Create(line_3))
        self.play(Create(line_4))
  
        self.play(dot_4.animate.shift(DOWN*2.3))
        self.play(dot_4.animate.shift(UP*2.3))

        self.play(FadeIn(label_1,label_2,label_3),FadeOut(line_1,line_2,dot_3))
        self.wait(1) 