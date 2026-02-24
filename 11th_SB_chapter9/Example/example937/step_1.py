from manim import *
import numpy as np

config.frame_width=15
config.frame_height=8
config.pixel_width=2500
config.pixel_height=2500

config.background_color =WHITE

class Example937(Scene):
    def construct(self):

        # Axes
        axes=Axes(x_range=[-20, 130, 10],y_range=[-9, 26, 2],y_length=9,axis_config={"color":BLACK, "stroke_width": 4,"tick_size": 0.06},x_axis_config={"include_ticks": False},tips=False)
        axes.x_axis.add_tip(tip_length=0.35, tip_width=0.25)
        axes.y_axis.add_tip(tip_length=0.35, tip_width=0.25)
        labels1=axes.get_axis_labels(MathTex("x",color=BLACK))
        labels2=axes.get_axis_labels(MathTex("y",color=BLACK)).shift(UP*6.3+LEFT*10.3)

        
        f1=lambda x: 0.15 * x
        line_1=axes.plot(f1,x_range=[-20,100],color="#00FF00",stroke_width=4,use_smoothing=False).set_z_index(10)

    
        f2=lambda x: 0.133* x
        line_2=axes.plot(f2,x_range=[100, 130],color="#D100D1",stroke_width=4,use_smoothing=False).set_z_index(10)

        
        dot_line= DashedLine(axes.c2p(-20, 16),axes.c2p(100, 16),color="#0033FF",dash_length=0.15).shift(DOWN*0.22)
        dot_line2=DashedLine(axes.c2p(-20, 14),axes.c2p(100, 14),color="#0033FF",dash_length=0.15).shift(DOWN*0.2)
        dot_line3=DashedLine(axes.c2p(100, 0),axes.c2p(100,13.2),color="#0033FF",dash_length=0.15)             

        self.add(axes,labels1,labels2,line_1,line_2,dot_line,dot_line2,dot_line3)

        tick=axes.x_axis.get_tick(100)
        axes.x_axis.add(tick).set_z_index(10)
        label=MathTex("100",color=BLACK).scale(0.8)
        label.next_to(tick,DOWN,buff=0.1)
        self.add(label)

        for y in range(2, 25, 2):
            num = MathTex(str(y), color=BLACK).scale(0.5)
            num.move_to(axes.c2p(0, y)+LEFT*0.2+DOWN*0.1)
            self.add(num)
        for y in range(-2,-9,-2):
            num_2=MathTex(str(y),color=BLACK).scale(0.5)
            num_2.move_to(axes.c2p(0,y)+LEFT*0.3)
            self.add(num_2)

        eq_label=MathTex("m=.16",color=BLACK).scale(0.8)
        eq_label.rotate(15 * DEGREES).shift(DOWN*0.4)
        eq_label2=MathTex("m=.14",color=BLACK).move_to(line_2).scale(0.8)
        eq_label2.rotate(15 * DEGREES).shift(DOWN*0.4)
        self.add(eq_label,eq_label2)