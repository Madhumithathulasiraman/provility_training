from manim import *
import numpy as np
config.background_color = WHITE
config.frame_width =15
config.frame_height =10
config.pixel_width = 3000
config.pixel_height = 3000
class FlowerGraph(Scene):
    def construct(self):

        
        axes = Axes(x_range=[-4, 4, 1],y_range=[-4, 4, 1],axis_config={"include_tip":False,"color":BLACK,"include_ticks":False,"stroke_width":3},)
        axes.x_axis.add_tip(tip_length=0.25,tip_width=0.25)
        axes.x_axis.add_tip(tip_length=0.25,tip_width=0.25,at_start=True)
        axes.y_axis.add_tip(tip_length=0.25,tip_width=0.25)
        axes.y_axis.add_tip(tip_length=0.25,tip_width=0.25,at_start=True)

        x_label = MathTex("x",color=BLACK).next_to(axes.x_axis, RIGHT*0.1)
        y_label = MathTex("y",color=BLACK).next_to(axes.y_axis, UP*0.1)
        x1_label = MathTex("x'",color=BLACK).next_to(axes.x_axis, LEFT*0.1)
        y1_label = MathTex("y'",color=BLACK).next_to(axes.y_axis, DOWN*0.1)
        circles = VGroup()
        for angle in np.linspace(0, 2*PI, 5): 
            r = 1  
            cx = r * np.cos(angle)
            cy = r * np.sin(angle)
            center = axes.c2p(cx, cy)
            radius = np.linalg.norm(axes.c2p(0,0) - center)
            circle = Circle(radius=radius,color=BLUE,stroke_width=4).move_to(center)
            circles.add(circle)
        self.add(axes, circles)
        zero_label = MathTex("0",color=BLACK).scale(0.6)
        zero_label.move_to(axes.c2p(0, 0))
        zero_label.shift(DOWN * 0.25 + LEFT * 0.15)
        self.add(axes, x_label, y_label,x1_label ,y1_label,zero_label)