from manim import *

from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class Exercise9571(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        line = NumberLine(x_range=[-5, 5, 1],length=10,include_ticks=False,include_numbers=False,color="#97079C",stroke_width=4)
        line.add_tip(tip_length=0.35,tip_width=0.25)
        line.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        point1=line.n2p(-1.7)
        point2=line.n2p(1.5)
        label1 = MathTex("-\\infty", color=BLACK).scale(0.9).next_to(line, LEFT).shift(DOWN*0.4+RIGHT*0.7)
        label2 = MathTex("\\infty", color=BLACK).scale(0.9).next_to(line, RIGHT).shift(DOWN*0.4+LEFT*0.7)

       
        label_1=MathTex("-2", color=BLACK).scale(0.9).next_to(point1, DOWN)
        label_2=MathTex("1", color=BLACK).scale(0.9).next_to(point2, DOWN).shift(DOWN*0.06)
        tick1= Line(point1+ UP*0.15,point1 + DOWN*0.15, color=BLACK)
        tick2= Line(point2 + UP*0.15,point2 + DOWN*0.15,color=BLACK)
        segment = Line(point1, point2)
       
        brace1 = BraceBetweenPoints(line.n2p(-4.8),line.n2p(-1.8),direction=DOWN,color="#2754F5").shift(DOWN*0.4)
        brace2 = BraceBetweenPoints(line.n2p(-1.6),line.n2p(1.4),direction=DOWN,color="#2754F5").shift(DOWN*0.4)
        brace3 = BraceBetweenPoints(line.n2p(1.6),line.n2p(4.8),direction=DOWN,color="#2754F5").shift(DOWN*0.4)

        #function labels
        f1 = MathTex("f(x)=-(x+2)-(x-2)", color=BLACK).scale(0.5).next_to(brace1, DOWN*0.5)
        f2 = MathTex("f(x)=(x+2)-(x-1)", color=BLACK).scale(0.5).next_to(brace2, DOWN*0.5)
        f3 = MathTex("f(x)=+(x+2)+(x-1)", color=BLACK).scale(0.5).next_to(brace3, DOWN*0.5)
        f4= MathTex("x<-2", color=BLACK).scale(0.6).next_to(brace1, UP*3.5)
        f5 = MathTex("-2<=x<1", color=BLACK).scale(0.6).next_to(brace2,UP*3.5)
        f6 = MathTex("x>=1", color=BLACK).scale(0.6).next_to(brace3, UP*3.5)

     
        

        
       

        self.add(line,label1,label2,brace1, brace2, brace3,f1, f2, f3,f4,f5,f6,
                 tick1,tick2,label_1,label_2)
