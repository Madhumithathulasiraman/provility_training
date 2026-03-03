from manim import *
import numpy as np

config.frame_width=20
config.frame_height=8
config.pixel_width=2800
config.pixel_height=2800

config.background_color =WHITE

class Example937(Scene):
    def construct(self):

        # Axes
        axes=Axes(x_range=[-20, 159, 10],y_range=[-4, 39, 2],y_length=18,axis_config={"color":BLACK, "stroke_width": 5,"tick_size": 0.06},x_axis_config={"include_ticks":True},tips=False)
        axes.x_axis.add_tip(tip_length=0.4, tip_width=0.4)
        axes.y_axis.add_tip(tip_length=0.4, tip_width=0.4)
        axes.x_axis.add_tip(at_start=True,tip_length=0.4,tip_width=0.4)
        axes.y_axis.add_tip(at_start=True,tip_length=0.4,tip_width=0.4)
        labels1=axes.get_axis_labels(MathTex("x",color=BLACK)).shift(DOWN*3.5)
        labels2=axes.get_axis_labels(MathTex("y",color=BLACK)).shift(UP*12.5+LEFT*10.5)
        labels3=axes.get_axis_labels(MathTex("x'",color=BLACK)).shift(LEFT*12.5+DOWN*3.5)
        labels4=axes.get_axis_labels(MathTex("y'",color=BLACK)).shift(DOWN*5.3+LEFT*10.5)
        f1=lambda x: 0.16 * x
        line_1=axes.plot(f1,x_range=[0,100],color=GREEN,stroke_width=4,use_smoothing=False)

    
        f2=lambda x: 0.140* x
        line_2=axes.plot(f2,x_range=[110, 150],color=RED,stroke_width=4,use_smoothing=False)

        
        dot_line= DashedLine(axes.c2p(-20, 16),axes.c2p(100, 16),color=GREEN,dash_length=0.15)
        dot_line2=DashedLine(axes.c2p(-20, 14),axes.c2p(100, 14),color=RED,dash_length=0.15).shift(UP*0.05)
        dot_line3=DashedLine(axes.c2p(100, 0),axes.c2p(100,16),color=GREEN,dash_length=0.15)             

        self.add(axes,labels1,labels2,labels3,labels4,line_1,line_2,dot_line,dot_line2,dot_line3)


        for y in range(2, 27, 2):
            num = MathTex(str(y), color=BLACK).scale(0.5)
            num.move_to(axes.c2p(0, y)+LEFT*0.2+DOWN*0.1)
            self.add(num)
        
        numbers = VGroup()
        for x in range(10, 160, 10):
            num = MathTex(str(x), color=BLACK).scale(0.5)
            num.move_to(axes.c2p(x, 0) + DOWN * 0.3+LEFT*0.1)
            numbers.add(num)

        self.add(numbers)

        eq_label=MathTex("y=0.16x",color=BLACK).scale(0.5)
        eq_label.rotate(45 * DEGREES).shift(DOWN*3.2)
        eq_label2=MathTex("y=0.14x",color=BLACK).move_to(line_2).scale(0.5)
        eq_label2.rotate(45 * DEGREES).shift(DOWN*0.5)
        self.add(eq_label,eq_label2)

        for tick in axes.x_axis.ticks:
            x_val = axes.x_axis.p2n(tick.get_center())
            if x_val < 0:
                tick.set_opacity(0)
        
        for tick in axes.y_axis.ticks:
            y_val = axes.y_axis.p2n(tick.get_center())
            if y_val < 0:
                tick.set_opacity(0)
        #DOT
        dot=Dot(axes.c2p(0,0),color="#3827F5").scale(0.5)
        circle = Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot.get_center())
        dot1 = Dot(axes.c2p(10, 1.6), color="#3827F5").scale(0.5)
        label1 = MathTex("(10,\,1.6)", color=BLACK,font_size=15).scale(1)
        label1.next_to(dot1,UP*0.8)
        circle1= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot1.get_center())
        dot2= Dot(axes.c2p(20,3.2), color="#3827F5").scale(0.5)
        label2= MathTex("(20,\,3.2)", color=BLACK,font_size=15).scale(1)
        label2.next_to(dot2,UP*0.8)
        circle2= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot2.get_center())
        dot3= Dot(axes.c2p(30,4.8), color="#3827F5").scale(0.5)
        label3 = MathTex("(30,\,4.8)", color=BLACK,font_size=15).scale(1)
        label3.next_to(dot3,UP*0.8)
        circle3= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot3.get_center())
        dot4 = Dot(axes.c2p(40, 6.4), color="#3827F5").scale(0.5)
        label4= MathTex("(40,\,6.4)", color=BLACK,font_size=15).scale(1)
        label4.next_to(dot4,UP*0.8)
        circle4= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot4.get_center())
        dot5= Dot(axes.c2p(50, 8), color="#3827F5").scale(0.5)
        label5= MathTex("(50,\,8)", color=BLACK,font_size=15).scale(1)
        label5.next_to(dot5,UP*0.8)
        circle5= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot5.get_center())
        dot6= Dot(axes.c2p(60, 9.6), color="#3827F5").scale(0.5)
        label6 = MathTex("(60,\,9.6)", color=BLACK,font_size=15).scale(1)
        label6.next_to(dot6,UP*0.8)
        circle6= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot6.get_center())
        dot7 = Dot(axes.c2p(70, 11.2), color="#3827F5").scale(0.5)
        label7 = MathTex("(70,\,11.2)", color=BLACK,font_size=15).scale(1)
        label7.next_to(dot7,UP*0.8)
        circle7= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot7.get_center())
        dot8 = Dot(axes.c2p(80, 12.8), color="#3827F5").scale(0.5)
        label8 = MathTex("(80,\,12.8)", color=BLACK,font_size=15).scale(1)
        label8.next_to(dot8,UP*0.8)
        circle8= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot8.get_center())
        dot9 = Dot(axes.c2p(90, 14.4), color="#3827F5").scale(0.5)
        label9 = MathTex("(90,\,14.4)", color=BLACK,font_size=15).scale(1)
        label9.next_to(dot9,UP*0.8)
        circle9= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot9.get_center())
        dot10 = Dot(axes.c2p(100, 16), color="#3827F5").scale(0.5)
        label10 = MathTex("(100,\,16)", color=BLACK,font_size=15).scale(1)
        label10.next_to(dot10,UP*0.8)
        circle10= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot10.get_center())
        self.add(dot,dot1,circle,circle1,label1,dot2,label2,dot3,label3,dot4,label4,dot5,label5,dot6,label6,dot7,label7,dot8,label8,dot9,label9,dot10,label10,circle2,circle3,circle4,circle5,circle6,circle7,circle8,circle9,circle10)
        
        dot_1=Dot(axes.c2p(100,14),color="#3827F5").scale(0.5).shift(UP*0.05)
        label_1 = MathTex("(100,\,14)", color=BLACK,font_size=15).scale(1)
        label_1.next_to(dot_1,UP*0.8)
        dot_2= Dot(axes.c2p(110,15.4), color="#3827F5").scale(0.5)
        label_2= MathTex("(110,\,15.4)", color=BLACK,font_size=15).scale(1)
        label_2.next_to(dot_2,UP*0.8)
        circle_2= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot_2.get_center())
        dot_3= Dot(axes.c2p(120,16.8), color="#3827F5").scale(0.5)
        label_3= MathTex("(120,\,16.8)", color=BLACK,font_size=15).scale(1)
        label_3.next_to(dot_3,UP*0.8)
        circle_3= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot_3.get_center())
        dot_4= Dot(axes.c2p(130,18.2), color="#3827F5").scale(0.5)
        label_4= MathTex("(130,\,18.2)", color=BLACK,font_size=15).scale(1)
        label_4.next_to(dot_4,UP*0.8)
        circle_4= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot_4.get_center())
        dot_5= Dot(axes.c2p(140,19.6), color="#3827F5").scale(0.5)
        label_5= MathTex("(140,\,19.6)", color=BLACK,font_size=15).scale(1)
        label_5.next_to(dot_5,UP*0.8)
        circle_5= Circle(radius=0.10,color="#F5277D",stroke_width=3).move_to(dot_5.get_center())
       
        self.add(dot_1,label_1,dot_2,label_2,circle_2,dot_3,label_3,circle_3,dot_4,label_4,circle_4,dot_5,label_5,circle_5)

        
        y_label = Text("(cost)",color=BLACK).scale(0.6).shift(UP*6.7+LEFT*5.4)
        y_arrow = Arrow(start=axes.c2p(-10,34),end=axes.c2p(-10, 38),buff=0,color="#27D6F5",stroke_width=4,tip_length=0.3)
        self.add(y_label, y_arrow)
        x_label = Text("(kg)",color=BLACK).scale(0.6).shift(DOWN*8.5+RIGHT*5)
        x_arrow = Arrow(start=axes.c2p(130,-1.8),end=axes.c2p(150, -1.8),buff=0,color="#27D6F5",stroke_width=4,tip_length=0.3)
        self.add(x_label, x_arrow)

        equation1=MathTex("y=0.16x,0<=x<100",color=BLACK).shift(UP*7+RIGHT*2.5).scale(0.9)
        equation2=MathTex("y=0.14x,x>=100",color=BLACK).shift(UP*6.4+RIGHT*2).scale(0.9)
        zero_label=MathTex("0",color=BLACK).scale(0.5)
        zero_label.next_to(axes.c2p(-1, -0.5),LEFT*0.2)
        self.add(equation1,equation2,zero_label)
        