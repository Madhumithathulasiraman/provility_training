from manim import *

from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class Exercise9571(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        line = NumberLine(x_range=[-5, 5, 1],length=10,include_ticks=False,include_numbers=False,color="#F58E27",stroke_width=4)
        line.add_tip(tip_length=0.35,tip_width=0.25)
        line.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        point1=line.n2p(-1.7)
        point2=line.n2p(1.5)
        label1 = MathTex("-\\infty", color=BLACK).scale(0.9).next_to(line, LEFT).shift(DOWN*0.4+RIGHT*0.7)
        label2 = MathTex("\\infty", color=BLACK).scale(0.9).next_to(line, RIGHT).shift(DOWN*0.4+LEFT*0.7)

       
        label_1=MathTex("0", color=BLACK).scale(0.9).next_to(point1, DOWN)
        label_2=MathTex("2", color=BLACK).scale(0.9).next_to(point2, DOWN).shift(DOWN*0.06)
        tick1= Line(point1+ UP*0.15,point1 + DOWN*0.15, color=BLACK)
        tick2= Line(point2 + UP*0.15,point2 + DOWN*0.15,color=BLACK)
        segment = Line(point1, point2)
       
        brace1 = BraceBetweenPoints(line.n2p(-4.8),line.n2p(-1.8),direction=DOWN,color="#F52795").shift(DOWN*0.4)
        brace2 = BraceBetweenPoints(line.n2p(-1.6),line.n2p(1.4),direction=DOWN,color="#F52795").shift(DOWN*0.4)
        brace3 = BraceBetweenPoints(line.n2p(1.6),line.n2p(4.8),direction=DOWN,color="#F52795").shift(DOWN*0.4)

        #function labels
        f1 = MathTex("f(x)=0", color=BLACK).scale(0.8).next_to(brace1, DOWN)
        f2 = MathTex("f(x)=x^2", color=BLACK).scale(0.8).next_to(brace2, DOWN)
        f3 = MathTex("f(x)=4", color=BLACK).scale(0.8).next_to(brace3, DOWN)
        f4= MathTex("x<0", color=BLACK).scale(0.6).next_to(brace1, UP*0.5)
        f5 = MathTex("0<=x<2", color=BLACK).scale(0.6).next_to(brace2,UP*0.5)
        f6 = MathTex("x>=2", color=BLACK).scale(0.6).next_to(brace3, UP*0.5)

     
        shift_amt = 0.6
        zero_label1 = MathTex("0^{-}", color=BLACK).scale(0.8).move_to(point1 + LEFT*shift_amt + UP*0.6)
        zero_label2= MathTex("0^{+}", color=BLACK).scale(0.8).move_to(point1+ RIGHT*shift_amt + UP*0.6).shift(RIGHT*0.3)
        two_label1= MathTex("2^{-}", color=BLACK).scale(0.8).move_to(point2 + LEFT*shift_amt + UP*0.6)
        two_label2 = MathTex("2^{+}", color=BLACK).scale(0.8).move_to(point2+ RIGHT*shift_amt + UP*0.6).shift(RIGHT*0.3)

        
        height=0.6
        arrow1 = Arrow(start=point1+ LEFT*0.8 + UP*height,end=point1+ LEFT*0.05 + UP*height,buff=0,stroke_width=2,color="#4227F5").shift(DOWN*0.3+LEFT*0.2)
        arrow2 = Arrow(start=point1+ RIGHT*0.8 + UP*height,end=point1+ RIGHT*0.05 + UP*height,buff=0,stroke_width=2,color="#4227F5").shift(DOWN*0.3+RIGHT*0.2)
        arrow3 = Arrow(start=point2+ LEFT*0.8 + UP*height,end=point2 + LEFT*0.05 + UP*height,buff=0,stroke_width=2,color="#4227F5").shift(DOWN*0.3+LEFT*0.2)
        arrow4 = Arrow(start=point2 + RIGHT*0.8 + UP*height,end=point2 + RIGHT*0.05 + UP*height,buff=0,stroke_width=2,color="#4227F5").shift(DOWN*0.3+RIGHT*0.2)

        self.add(line,label1,label2,brace1, brace2, brace3,f1, f2, f3,f4,f5,f6,
                 tick1,tick2,zero_label1,zero_label2,two_label1,two_label2 ,arrow1 ,arrow2,arrow3,arrow4)
