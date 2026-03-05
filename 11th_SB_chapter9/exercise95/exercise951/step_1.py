from manim import *

config.background_color=WHITE

class Exercise951(Scene):
    def construct(self):

        axes = Axes(x_range=[-4,4,1],y_range=[-6.9,6,1],x_length=8,y_length=6,axis_config={"color": BLACK,"include_ticks":False,"stroke_width": 3.5},tips=False)
        axes.x_axis.add_tip()
        axes.x_axis.add_tip(at_start=True)
        axes.y_axis.add_tip()
        axes.y_axis.add_tip(at_start=True)

        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP)
        x1_label = MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(), LEFT)
        y1_label = MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(),DOWN)
        graph = axes.plot(lambda x: 2*x**2 + 3*x - 5,x_range=[-3,1.8],color=BLUE)

        
        point1 = Dot(axes.c2p(-2.5,0), color="#F527CC")
        point2 = Dot(axes.c2p(1,0), color="#F527CC")
        point3 = Dot(axes.c2p(-0.75,-6.125),color="#F527CC")
        point4 = Dot(axes.c2p(0,-5),color="#F527CC")
        label1 = MathTex("(-2.5,0)", color=BLACK).scale(0.6).next_to(point1, DOWN*0.2+LEFT*0.3)
        label2 = MathTex("(1,0)", color=BLACK).scale(0.6).next_to(point2, DOWN*0.2+RIGHT*0.3)
        label3 = MathTex("(-0.75,-6.125)", color=BLACK).scale(0.6).next_to(point3, DOWN*0.2+LEFT*0.3)
        label4 = MathTex("(0,-5)", color=BLACK).scale(0.6).next_to(point4, DOWN*0.1+RIGHT*0.2)
        func_label = MathTex("f(x)=2x^2+3x-5", color=BLACK).shift(UP*2+RIGHT*1.20).scale(0.6)
        func_label.rotate(PI/2.4)
        text = MathTex(r"\text{Continuous for all } x \in \mathbb{R}",color=BLACK).scale(0.8).shift(UP+RIGHT*3.5)

        self.add(axes, x_label, y_label,x1_label,y1_label,graph,point1, point2, point3, point4,label1, label2,label3,label4,func_label,text)