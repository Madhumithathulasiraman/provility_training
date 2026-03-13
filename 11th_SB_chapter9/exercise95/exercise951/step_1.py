from manim import *

config.background_color=WHITE
config.pixel_width =3000
config.pixel_height =3000
config.frame_width = 14
config.frame_height = 8

class Exercise951(Scene):
    def construct(self):

        axes = Axes(x_range=[-4.4,4.4,1],y_range=[-7,7.5,1],x_length=8,y_length=6,axis_config={"color": BLACK,"include_ticks":False,"stroke_width": 3},tips=False)
        axes.x_axis.add_tip(tip_length=0.3,tip_width=0.3)
        axes.x_axis.add_tip(tip_length=0.3,tip_width=0.3,at_start=True)
        axes.y_axis.add_tip(tip_length=0.3,tip_width=0.3)
        axes.y_axis.add_tip(tip_length=0.3,tip_width=0.3,at_start=True)
        x_axis = DoubleArrow(start=LEFT*3.5,end=RIGHT*3.5,buff=0,stroke_width=4,color=BLUE,tip_length=0.2).shift(DOWN*0.10).set_z_index(10)
        self.add(x_axis)

        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT*0.1)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP*0.1)
        x1_label = MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(), LEFT*0.1)
        y1_label = MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(),DOWN*0.1)
        graph = axes.plot(lambda x: 2*x**2 + 3*x - 5,x_range=[-3.2,1.70],color=BLUE).set_z_index(10)
        end_tip = Arrow(graph.point_from_proportion(0.93),graph.point_from_proportion(1),buff=0,color=BLUE,stroke_width=0).shift(UP*0.05+RIGHT*0.01)
        start_tip = Arrow(graph.point_from_proportion(0.07),graph.point_from_proportion(0),buff=0,color=BLUE,stroke_width=0).shift(UP*0.05+LEFT*0.01)
        self.add(graph, start_tip, end_tip)
        
        point1 = Dot(axes.c2p(-2.5,0), color="#F527CC").set_z_index(10)
        point2 = Dot(axes.c2p(1,0), color="#F527CC").set_z_index(10)
        
        label1 = MathTex("(-2.5,0)", color=BLACK).scale(0.6).next_to(point1, UP*0.2+LEFT*0.5)
        label2 = MathTex("(1,0)", color=BLACK).scale(0.6).next_to(point2, UP*0.2+RIGHT*0.5)
        
        func_label = MathTex("f(x)=2x^2+3x-5", color=BLACK).shift(UP*1.2+RIGHT*1).scale(0.5)
        func_label.rotate(PI/2.4)
        text = MathTex(r"\text{Continuous for all } x \in \mathbb{R}",color=BLACK).scale(0.5).shift(DOWN*0.4+RIGHT*2.3)

        self.add(axes, x_label, y_label,x1_label,y1_label,graph,point1, point2,label1, label2,func_label,text)