from manim import *
import numpy as np

config.background_color = WHITE

class Exercise9113(Scene):
    def construct(self):
        axes = Axes(x_range=[-1.1,2.5,1],y_range=[-1.5,1.5,1],axis_config={"color":"#1B7F3F"},tips=True,x_axis_config={"include_numbers":False},y_axis_config={"include_numbers":False},).set_z_index(1)
        axes.x_axis.set_stroke(width=4)
        axes.y_axis.set_stroke(width=4)

        labels=axes.get_axis_labels(Text("x",color=BLACK),Text("y",color=BLACK))
        labels_left=VGroup(MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(-1, 0), DOWN*0.5),)
        y_labels=VGroup(MathTex("1",font_size=40,color=BLACK).next_to(axes.c2p(0,1),LEFT*0.6),MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(0,-1),LEFT*0.6),)
        labels_right=VGroup(MathTex("1",font_size=40,color=BLACK).next_to(axes.c2p(1, 0), DOWN*0.5),MathTex("2",font_size=40,color=BLACK).next_to(axes.c2p(2, 0), DOWN*0.5),)
        dot=Dot(axes.coords_to_point(1,0),color="#701705").set_z_index(1)
        
        # Curve
        curve = axes.plot(lambda x:np.sin(np.pi * x),x_range=[-1,2.5],color="##701705",stroke_width=4).set_z_index(1)

        self.add(axes,labels,labels_left,y_labels,labels_right,dot,curve)
        

