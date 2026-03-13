from manim import *

config.background_color=WHITE

config.frame_width=13
config.frame_height=8
config.pixel_width=2800
config.pixel_height=2800


class Exercise957(Scene):
    def construct(self):
        
     

        axes = Axes(x_range=[-3.9, 7.9, 1],y_range=[-2.9, 4.9, 1],axis_config={"color": BLACK,"stroke_width":3},tips=False)
        axes.x_axis.add_tip(tip_length=0.3, tip_width=0.3)
        axes.y_axis.add_tip(tip_length=0.3, tip_width=0.3)
        x_numbers=axes.x_axis.add_numbers(range(-3, 8), font_size=25,color=BLACK)
        y_numbers=axes.y_axis.add_numbers(range(-2, 5), font_size=25,color=BLACK)
        
        
        dashed_line = DashedLine(start=axes.c2p(2, 0),end=axes.c2p(2, 4),dash_length=0.1,color=BLACK)
        self.add(dashed_line)
        
        axes.x_axis.add_tip(at_start=True,tip_length=0.3, tip_width=0.3)
        axes.y_axis.add_tip(at_start=True,tip_length=0.3, tip_width=0.3)
        graph1 = axes.plot(lambda x: 0,x_range=[-3, 0],color=GREEN)
        graph1 = Arrow(start=axes.c2p(0, 0),end=axes.c2p(-3.5, 0), buff=0,color=GREEN,stroke_width=4,tip_length=0.3)
        graph2 = axes.plot(lambda x: x**2,x_range=[0, 2],color=RED)
        graph3 = axes.plot(lambda x: 4,x_range=[2, 7],color=BLUE)
        graph3=Arrow(start=axes.c2p(2, 4),end=axes.c2p(7,4), buff=0,color=BLUE,stroke_width=4,tip_length=0.3)
        dot1 = Dot(axes.c2p(0, 0),color="#D627F5")
        dot2 = Dot(axes.c2p(2, 4),color="#D627F5")
        self.add(axes, graph1, graph2, graph3, dot1, dot2)

        arrow1= Arrow(start=axes.c2p(1,-1),end=axes.c2p(1.8, -1),buff=0,color="#3527F5").shift(UP*0.2+RIGHT*0.20)
        label1=MathTex("2^-", color=BLACK).scale(0.5)
        label1.next_to(arrow1.get_center(),DOWN, buff=0.13)
        arrow2= Arrow(start=axes.c2p(3,-1),end=axes.c2p(2.2, -1),buff=0,color="#3527F5").shift(UP*0.2+RIGHT*0.20)
        label2=MathTex("2^+", color=BLACK).scale(0.5)
        label2.next_to(arrow2.get_center(),DOWN+RIGHT*0.15, buff=0.1)

        self.add(arrow1,label1,arrow2,label2)


        arrow_1= Arrow(start=axes.c2p(-1,0.5),end=axes.c2p(-0.2, 0.5),buff=0,color="#3527F5")
        label_1=MathTex("0^-", color=BLACK).scale(0.5)
        label_1.next_to(arrow_1.get_end(),DOWN, buff=0.13)
        arrow_2= Arrow(start=axes.c2p(1,0.5),end=axes.c2p(0.2, 0.5),buff=0,color="#3527F5")
        label_2=MathTex("0^+", color=BLACK).scale(0.5)
        label_2.next_to(arrow_2.get_end(),DOWN, buff=0.1)
        self.add(arrow_1,label_1,arrow_2,label_2)

        parabola_label = MathTex("f(x) = x^2",color=BLACK).next_to(axes.c2p(0.2, 1.5)).scale(0.6).rotate(60 * DEGREES)
        horizontal_label = MathTex("f(x)= 4",color=BLACK).next_to(axes.c2p(3.2,3.7),UP).scale(0.6)
        y_zero_label = MathTex("f(x)= 0",color=BLACK).next_to(axes.c2p(-2, 0),UP*0.2).scale(0.6)

        self.add(parabola_label,horizontal_label,y_zero_label)

        x_label = MathTex("x", color=BLACK)
        x_label.next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        x1_label = MathTex("x'", color=BLACK)
        x1_label.next_to(axes.x_axis.get_start(), LEFT, buff=0)
        y_label = MathTex("y", color=BLACK)
        y_label.next_to(axes.y_axis.get_end(), UP, buff=0.1)
        y1_label = MathTex("y'", color=BLACK)
        y1_label.next_to(axes.y_axis.get_start(), DOWN, buff=0)
        self.add(x_label, x1_label, y_label, y1_label)

       
        infinity1= MathTex("-\\infty", color=BLACK).scale(0.6)
        infinity2= MathTex("\\infty", color=BLACK).scale(0.6)
        infinity1.next_to(axes.x_axis.get_start(), DOWN, buff=0.3)
        infinity2.next_to(axes.x_axis.get_end(), DOWN+RIGHT*0.1, buff=0.3)

        self.add(infinity1,infinity2)