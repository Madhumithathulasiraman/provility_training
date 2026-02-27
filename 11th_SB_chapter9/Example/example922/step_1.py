from manim import *
import numpy as np

config.background_color = WHITE
config.frame_width=15
config.frame_height=8
config.pixel_width=2800
config.pixel_height=2800

class Example922(Scene):
    def construct(self):

        # Axes
        axes=Axes(x_range=[-6,7,1],x_length=6,y_range=[-7,7,1],y_length=7,axis_config={"color":BLACK,"stroke_width":3.5},x_axis_config={"include_ticks": False},y_axis_config={"include_ticks": False},tips=False)
        axes.x_axis.add_tip(tip_length=0.3,tip_width=0.3)
        axes.x_axis.add_tip(at_start=True,tip_length=0.3,tip_width=0.3)
        axes.y_axis.add_tip(tip_length=0.3,tip_width=0.3)
        axes.y_axis.add_tip(at_start=True,tip_length=0.3,tip_width=0.3)

        line=DashedLine(axes.c2p(2,-6.60),axes.c2p(2,6.6),color="#45031C",stroke_width=4,dash_length=0.1).shift(RIGHT*0.1)

        f=lambda x:1/((x-2)**3)
        y_top=axes.y_range[1]
        y_bottom=axes.y_range[0]
        x_right_limit=2+ np.cbrt(1.2/y_top)
        x_left_limit=2+ np.cbrt(1.2/y_bottom)
        left_curve=axes.plot(f,x_range=[axes.x_range[0],x_left_limit],color="#9F27F5",stroke_width=4,use_smoothing=False).shift(DOWN*0.4+RIGHT*0.1)
        right_curve=axes.plot(f,x_range=[x_right_limit,axes.x_range[1]],color="#9F27F5",stroke_width=4,use_smoothing=False).shift(UP*0.4)

        x_label=MathTex("x",color=BLACK).shift(RIGHT*3.2)
        y_label=MathTex("y",color=BLACK).shift(UP*3.5)
        x1_label=MathTex("x'",color=BLACK).shift(LEFT*3.2)
        y1_label=MathTex("y'",color=BLACK).shift(DOWN*3.7+LEFT*0.1)

        two_label = MathTex("2",color=BLACK,font_size=30)
        two_label.next_to(axes.c2p(2, 0),DOWN*0.3+RIGHT*0.1).set_z_index(10)
        zero_label=MathTex("0",color=BLACK,font_size=30)
        zero_label.next_to(axes.c2p(0,0),LEFT*0.3+DOWN*0.2)



        function_label=MathTex(r"f(x)=\frac{1}{(x-2)^3}",color=BLACK,font_size=25).to_edge(UP*4+RIGHT*8.9)

        line_label=MathTex("x=2",color=BLACK,font_size=20).next_to(axes.c2p(2,-1),RIGHT*0.6)
        
        self.add(axes,x_label,y_label,x1_label,y1_label,function_label,zero_label,two_label ,line,left_curve,right_curve,line_label)
        
        
        p_end = right_curve.get_end()
        p_prev = right_curve.point_from_proportion(0.97)

        right_tip = Arrow(p_prev,p_end,buff=0,color="#9F27F5",stroke_width=1,max_tip_length_to_length_ratio=1.5).shift(UP*0.01+RIGHT*0.1)

        self.add(right_tip)

        p_start = left_curve.get_start()
        p_next = left_curve.point_from_proportion(0.03)

        left_tip = Arrow(p_next,p_start,buff=0,color="#9F27F5",stroke_width=1,max_tip_length_to_length_ratio=1.2).shift(DOWN*0.01+LEFT*0.05)


        self.add(left_tip)


        arrow_1=Arrow(UP*3,DOWN*3,color="#09E363",stroke_width=4,tip_length=0.2).shift(DOWN*3.3+RIGHT*0.3).scale(0.1)
        arrow_2=Arrow(DOWN*3,UP*3,color="#09E363",stroke_width=4,tip_length=0.2).shift(UP*3.3+RIGHT*1.2).scale(0.1)
        arrow_3=Arrow(LEFT*3,RIGHT*3,color="#ACE309",stroke_width=4,tip_length=0.25).shift(DOWN*0.3+RIGHT*-0.2).scale(0.3)
        arrow_4=Arrow(RIGHT*3,LEFT*3,color="#ACE309",stroke_width=4,tip_length=0.25).shift(DOWN*0.3+RIGHT*1.8).scale(0.3)
        label_1=MathTex("2^{-}",color=BLACK,font_size=20).shift(DOWN*0.45+RIGHT*0.2)
        label_2=MathTex("2^{+}",color=BLACK,font_size=20).shift(DOWN*0.45+RIGHT*1.8)
        label_3=MathTex(r"Approces\ -\infty",color=BLACK,font_size=20).shift(DOWN*3.6+RIGHT)
        label_4=MathTex(r"Approces\ +\infty",color=BLACK,font_size=20).shift(UP*3.6+RIGHT*2)
        hole=Circle(radius=0.15,color=BLUE,stroke_width=6)
        hole.move_to(axes.c2p(2,0)).shift(DOWN*0.2+RIGHT*0.1)
        self.add(arrow_1,arrow_2,arrow_3,arrow_4,label_1,label_2,label_3,label_4,hole)

        