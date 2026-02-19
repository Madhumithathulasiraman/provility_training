from manim import *
import numpy as np

config.frame_width=20
config.frame_height=12
config.pixel_width=2500
config.pixel_height=2500
config.background_color=WHITE

class Parabola(Scene):
    def construct(self):

        txt=BLACK

        # X,Y Axis
        x_axis=Line([-5,0,0],[9,0,0],color=BLACK)
        x_axis.add_tip()
        x_label=MathTex("X",color=txt).next_to(x_axis.get_end(),UP)
        x1=MathTex("X'",color=txt).next_to(x_axis.get_start(),UP)
        y_axis=Line([0,6,0],[0,-6,0],color=BLACK)
        y_axis.add_tip(at_start=True)
        y_label=MathTex("Y",color=txt).next_to(y_axis.get_start(),RIGHT)
        y1=MathTex("Y'",color=txt).next_to(y_axis.get_end(),RIGHT)
        self.add(x_axis,y_axis,x_label,x1,y_label,y1)

        # Parabola
        axes=Axes()
        parabola=axes.plot_parametric_curve(
            lambda t: np.array([3*t*t,6*t,0]),
            t_range=[-1.5,1.5],
            color="#1D5DEC",
            stroke_width=8
        )
        self.add(parabola)
        eq=MathTex("y^2=12x",color=txt).move_to([5.2,-4.5,0])
        self.add(eq)
        vertex=Dot([0,0,0],color=RED)
        v_label=MathTex("V(0,0)",color=txt).next_to(vertex,RIGHT,buff=-2).shift(DOWN*0.4)
        focus=Dot([2,0,0],color=RED)
        f_label=Text("Focus",font_size=30,color=txt).next_to(focus,RIGHT).shift(DOWN*0.4)
        f_coord=MathTex("(3,0)",color=txt).next_to(focus,LEFT).shift(DOWN*0.4)
        self.add(vertex,focus,v_label,f_label,f_coord)
        latus=Line([2,-3.1,0],[2,3.1,0],color=GREEN,stroke_width=5)
        self.add(latus)
        top=latus.get_top()
        bottom=latus.get_bottom()
        brace=BraceBetweenPoints(top,bottom,RIGHT,buff=2)
        brace.set_color(BLACK).set_stroke(width=5) 
        brace_text=Text("Length of\nLatus Rectum = 12",
                          font_size=25,
                          color=txt).next_to(brace,RIGHT)
        self.add(brace,brace_text)

        directrix=DashedLine([-3,-3,0],[-3,3,0],color=RED)
        directrix.add_tip()
        directrix.add_tip(at_start=True)
        d_text=MathTex("x=-3",color=txt).next_to(directrix,DOWN)
        self.add(directrix,d_text)

        axis_text=Text("Axis of parabola",font_size=30,color=txt).move_to([8,1,0])
        self.add(axis_text)
