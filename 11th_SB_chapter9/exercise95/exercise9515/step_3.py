from manim import *
import numpy as np

config.pixel_width =3000
config.pixel_height =3000
config.frame_width = 14
config.frame_height = 8

config.background_color = WHITE

class ExerciseAnswer9115c(Scene):
    def construct(self):

        
        axes = Axes(x_range=[-2.2, 5.5, 1],y_range=[-3.5,4, 1],x_length=10,y_length=7,axis_config={"color":BLACK,"stroke_width":3.2,"include_ticks":False},tips=False)
        axes.x_axis.add_tip()
        axes.y_axis.add_tip()
        axes.x_axis.add_tip(at_start=True)
        axes.y_axis.add_tip(at_start=True)
        x_label1=MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(), LEFT*0.1)
        y_label1=MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(), DOWN*0+RIGHT*0.5)

    
        def func(x):
            return 1 / (x-3)

        graph_left = axes.plot(func,x_range=[-1.9,2.68],color="#2738F5",stroke_width=5).shift(DOWN*0.1)
        start_point = graph_left.get_start()
        next_point = graph_left.point_from_proportion(0.2)
        tip_start = Arrow(next_point,start_point,buff=0,stroke_width=5,tip_length=0.2,color="#2738F5",max_tip_length_to_length_ratio=2).shift(LEFT*0.05)
        self.add(tip_start)
        graph_right = axes.plot(func,x_range=[3.28,5.5],color="#2738F5",stroke_width=5)
        end_point = graph_right.get_end()
        prev_point = graph_right.point_from_proportion(0.97)
        tip_right = Arrow(prev_point,end_point,buff=0,stroke_width=5,color="#2738F5",tip_length=0.2,max_tip_length_to_length_ratio=2).shift(RIGHT*0.05)
        self.add(tip_right)
        
        line= DashedLine(start=axes.c2p(3,-3.3),end=axes.c2p(3,3.5),color=RED,stroke_width=5,dash_length=0.15).shift(RIGHT*0.050).set_z_index(10)
        label_dased=MathTex("x_0",color=BLACK)
        label_dased.next_to(line,RIGHT,buff=0).shift(DOWN*0.35+RIGHT*0.1)
        
        label=MathTex("x = x_0", color=BLACK)
        label.scale(1)
        label.next_to(line, RIGHT,buff=0.2).shift(DOWN*1.5)
        label2=MathTex("x",color=BLACK)
        label2.next_to(axes.c2p(5.4,0),DOWN*0+RIGHT*0.9)
        label3=MathTex("y",color=BLACK)
        label3.next_to(axes.c2p(0,3.9),UP*0.1+RIGHT*0.7)

        self.add(axes,x_label1,y_label1,graph_left, graph_right, line, label,label2,label3,label_dased)
        arrow_down = Arrow(UP,DOWN,buff=0,color=PINK,stroke_width=4,tip_length=0.2).scale(0.4).shift(DOWN*2.9+RIGHT*1)
        eq = MathTex(r"\text{Approaches}-\infty",color=BLACK).scale(0.5).shift(DOWN*2.9)
        self.add(arrow_down,eq)
        arrow_UP = Arrow(DOWN,UP,buff=0,color=PINK,stroke_width=4,tip_length=0.2).scale(0.4).shift(UP*2.9+RIGHT*2.5)
        eq1= MathTex(r"\text{Approaches}+\infty",color=BLACK).scale(0.5).shift(UP*2.9+RIGHT*3.5)
        self.add(arrow_UP,eq1)
        arrow = Arrow(start=LEFT * 1,end=RIGHT * 1,color="#C82009",buff=0,tip_length=0.15,stroke_width=2.5).scale(0.6).shift(RIGHT*-1.2+DOWN*0.61)
        arrow2= Arrow(start=RIGHT * 1,end=LEFT * 1,color="#C82009",buff=0,tip_length=0.15,stroke_width=2.5).scale(0.6).shift(RIGHT*3.5+UP*1)
        label = MathTex("x_0^{-}", color=BLACK)
        label.shift(DOWN*0.44+LEFT*1.3).scale(0.7)
        label1 = MathTex("x_0^{+}", color=BLACK)
        label1.next_to(arrow2.get_center(),UP*0.1).scale(0.7)
        self.add(arrow,arrow2,label, label1)
        zero = MathTex("0", color=BLACK).scale(0.7)
        zero.next_to(axes.c2p(0,0),DOWN+LEFT, buff=0.1)

        eq1 = MathTex( r"f(x_0) \text{ does not exist}", color=BLACK).scale(0.5)
        eq2=MathTex(r"\Rightarrow \text{Not continuous at } x = x_0",color=BLACK).scale(0.5)
        group = VGroup(eq1,eq2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        box = SurroundingRectangle(group, color=BLACK, buff=0.1,stroke_width=2.5)
        full_box = VGroup(box, group) 
        full_box.scale(0.8)  
        full_box.shift(UP*1+ RIGHT*5.55)
        self.add(full_box,zero)
        arrow_eq= Arrow(RIGHT,DOWN,buff=0,color=BLACK,stroke_width=2.5,tip_length=0.15).scale(1.85)
        arrow_eq.rotate(155* PI / 180)
        arrow_eq.shift(UP*0.72+RIGHT*2.52)
        self.add(arrow_eq)
        
        

        