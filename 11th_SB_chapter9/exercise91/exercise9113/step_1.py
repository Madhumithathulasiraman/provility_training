from manim import *
import numpy as np

config.background_color = WHITE

class ExerciseAnswer9113(Scene):
    def construct(self):
        axes=Axes(x_range=[-1.5,2.5,1],y_range=[-1.5,1.5,1],axis_config={"color":BLACK},tips=True,x_axis_config={"include_numbers":False,"include_ticks": False,},y_axis_config={"include_numbers":False},).set_z_index(1)
        axes.x_axis.set_stroke(width=4)
        axes.y_axis.set_stroke(width=4)
        axes.x_axis.add_tip(at_start=True)
        axes.y_axis.add_tip(at_start=True)
        tick_1=axes.x_axis.get_tick(-1).shift(LEFT*0)
        tick_2=axes.x_axis.get_tick(1).shift(LEFT*0)
        tick_3=axes.x_axis.get_tick(2).shift(LEFT*0)
        

        labels=axes.get_axis_labels(MathTex("x",color=BLACK),MathTex("y",color=BLACK))
        axis_label1=MathTex("x'",font_size=55,color=BLACK).next_to(axes.c2p(-2,0),RIGHT*4.5+UP*0.5)
        axis_label2=MathTex("y'",font_size=55,color=BLACK).next_to(axes.c2p(0,-2),UP*2.5+RIGHT)
        labels_left=VGroup(MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(-1.1, 0), DOWN*0.5),)
        y_labels=VGroup(MathTex("1",font_size=40,color=BLACK).next_to(axes.c2p(0,1),LEFT*0.5),MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(0,-0.9),LEFT*0.6),)
        labels_right=VGroup(MathTex("1",font_size=40,color=BLACK).next_to(axes.c2p(1, 0), DOWN*0.8+LEFT*0.2),MathTex("2",font_size=40,color=BLACK).next_to(axes.c2p(2.03, 0), DOWN*0.5),)
        dot=Dot(axes.coords_to_point(1,0),color="#483AE4").set_z_index(10)
        
        # Curve
        curve = axes.plot(lambda x:np.sin(np.pi * x),x_range=[-1,2.5],color="#F5276C",stroke_width=4).set_z_index(1)

        self.add(axes,tick_1,tick_2,tick_3,labels,axis_label1,axis_label2,labels_left,y_labels,labels_right,dot,curve)

        arrow_1=Arrow(LEFT*3,RIGHT*3,color="#6A0B37",stroke_width=4,tip_length=0.25).shift(DOWN*0.7+LEFT).scale(0.8)
        arrow_2=Arrow(RIGHT*3,LEFT*3,color="#6A0B37",stroke_width=4,tip_length=0.25).shift(DOWN*0.7+RIGHT*3.7).scale(0.8)
        arrow_3=Arrow(DOWN*2,UP*3,color="#6A0B37",stroke_width=3,tip_length=0.25).shift(DOWN*1.8+RIGHT*1.4).scale(0.2)
        label_1=MathTex("1^{-}",color=BLACK,font_size=30)
        label_2=MathTex("1^{+}",color=BLACK,font_size=30)
        label_3=MathTex("y=\\sin(\\pi x)",color=BLACK,font_size=35).next_to(axes.c2p(0.5,1),UP*0.2)

        label_1.next_to(arrow_1.get_end(),LEFT*1.5+DOWN*0.6)
        label_2.next_to(arrow_2.get_end(),RIGHT*1.5+DOWN*0.6)
        self.add(arrow_1,arrow_2,arrow_3,label_1,label_2,label_3)

        hole=Circle(radius=0.20,color="#D5E33B",stroke_width=6)
        hole.move_to(axes.c2p(1,0)).shift(DOWN*0.33+LEFT*0.12)
        self.add(hole)

        zero_label = MathTex("0", color=BLACK)

        zero_label.next_to(axes.c2p(-0.1,0), DOWN*0.6+LEFT*0.1)

        self.add(zero_label)