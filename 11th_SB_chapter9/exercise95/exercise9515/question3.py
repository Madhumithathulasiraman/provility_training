from manim import *
import numpy as np

config.pixel_width =3000
config.pixel_height =3000
config.frame_width = 14
config.frame_height = 8

config.background_color = WHITE

class Exercise9115c(Scene):
    def construct(self):

        
        axes = Axes(x_range=[-2.2, 5.5, 1],y_range=[-3.5,4, 1],x_length=10,y_length=7,axis_config={"color":"#079C1E","stroke_width":4,},tips=True)
        axes.x_axis.tip.scale(0.7).shift(LEFT*0.2) 
        axes.y_axis.tip.scale(0.7).shift(DOWN*0.2)
        axes.x_axis.tip.move_to(axes.x_axis.get_end())
        axes.y_axis.tip.move_to(axes.y_axis.get_end())

    
        def func(x):
            return 1 / (x-3)

        graph_left = axes.plot(func,x_range=[-2,2.72],color="#2738F5",stroke_width=5)

        graph_right = axes.plot(func,x_range=[3.28,5.5],color="#2738F5",stroke_width=5)

        
        line= DashedLine(start=axes.c2p(3,-3.5),end=axes.c2p(3,3.5),color=RED,stroke_width=5,dash_length=0.15).shift(RIGHT*0.050)

        
        label=MathTex("x = x_0", color=BLACK)
        label.scale(1)
        label.next_to(line, RIGHT,buff=0.2).shift(DOWN*1.5)
        label2=MathTex("x",color=BLACK)
        label2.next_to(axes.c2p(5.4,0),UP*0.1+RIGHT*0.9)
        label3=MathTex("y",color=BLACK)
        label3.next_to(axes.c2p(0,4),UP*0.1+RIGHT*0.7)

        self.add(axes, graph_left, graph_right, line, label,label2,label3)

        for x in range(-2,6):
            if x != 0:
                label_x = MathTex(str(x),color=BLACK).scale(0.5)
                label_x.next_to(axes.c2p(x,0),DOWN,buff=0.1)
                self.add(label_x)
        for y in range(-3,4):
            if y!=0:
                label_y=MathTex(str(y),color=BLACK).scale(0.5)
                label_y.next_to(axes.c2p(0,y),LEFT,buff=0.2)
                self.add(label_y)