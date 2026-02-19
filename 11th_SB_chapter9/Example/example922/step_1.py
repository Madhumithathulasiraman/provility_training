from manim import *
import numpy as np

config.background_color = WHITE

class Example922(Scene):
    def construct(self):

        # Axes
        axes=Axes(x_range=[-3,7,1],x_length=6,y_range=[-7,7,1],y_length=7,axis_config={"color":BLACK,"stroke_width":4},x_axis_config={"include_ticks": False},y_axis_config={"include_ticks": False},tips=False)
        axes.x_axis.add_tip(tip_length=0.2,tip_width=0.2)
        axes.y_axis.add_tip(tip_length=0.2,tip_width=0.2)

        line=DashedLine(axes.c2p(2,-6.8),axes.c2p(2,6.2),color=RED,stroke_width=4,dash_length=0.1).shift(LEFT*0.2)

        f=lambda x:1/((x-2)**3)
        y_top=axes.y_range[1]
        y_bottom=axes.y_range[0]
        x_right_limit=2+np.cbrt(1.2/y_top)
        x_left_limit=2+np.cbrt(1.1/y_bottom)
        left_curve=axes.plot(f,x_range=[axes.x_range[0],x_left_limit],color="#1F2A7C",stroke_width=6,use_smoothing=False).shift(DOWN*0.2)
        right_curve=axes.plot(f,x_range=[x_right_limit,axes.x_range[1]],color="#1F2A7C",stroke_width=6,use_smoothing=False).shift(UP*0.2+LEFT*0.4)

        x_label=MathTex("x",color=BLACK).shift(RIGHT*3.2)
        y_label=MathTex("y",color=BLACK).shift(UP*3.4+LEFT*0.8)

        function_label=MathTex(r"f(x)=\frac{1}{(x-2)^3}",color=BLACK,font_size=25).to_edge(UP*5+RIGHT*10)

        line_label=MathTex("x=2",color=BLACK,font_size=25).next_to(axes.c2p(1.5,-1),RIGHT)
        
        self.add(axes,x_label,y_label,function_label,line,left_curve,right_curve,line_label)
