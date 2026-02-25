from manim import *

config.background_color=WHITE

config.frame_width=13
config.frame_height=8
config.pixel_width=2800
config.pixel_height=2800


class Exercise957(Scene):
    def construct(self):
        
        axes = Axes(x_range=[-4, 6, 1],y_range=[-4, 6, 1],axis_config={"include_numbers": False,"include_ticks":False,"color":BLACK,"stroke_width":4},tips=True,).set_z_index(10)
        x_label = axes.get_x_axis_label(MathTex("x",color=BLACK))
        y_label = axes.get_y_axis_label(MathTex("y",color=BLACK))
        origin_label = MathTex("0",color=BLACK).next_to(axes.c2p(0, 0), DOWN+LEFT, buff=0.1)

        parabola = axes.plot(lambda x: x**2,x_range=[0,2],color="#2D9966").shift(LEFT*0.15)
        parabola_label = MathTex("y = x^2",color=BLACK).next_to(axes.c2p(1.2, 1.5),RIGHT)
        dot = Dot(axes.c2p(2, 4),color="#FF692A").set_z_index(10).shift(LEFT*0.15)
        horizontal_line = Arrow(start=axes.c2p(2, 4),end=axes.c2p(5.5, 4),buff=0,stroke_width=4,color="#2D9966").shift(LEFT*0.15)
        horizontal_label = MathTex("y = 4",color=BLACK).next_to(axes.c2p(3.5, 4),UP)
        y_zero_label = MathTex("y = 0",color=BLACK).next_to(axes.c2p(-2, 0), DOWN*3)

        
        self.add(axes, x_label, y_label, origin_label,parabola, parabola_label,dot, horizontal_line, horizontal_label,y_zero_label)