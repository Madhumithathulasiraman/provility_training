from manim import *

config.pixel_width = 2500
config.pixel_height = 2500
config.frame_width = 14
config.frame_height = 8

class Example91(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        #Axes 
        x_axis=Arrow(start=LEFT*5,end=RIGHT*5,buff=0,color=BLACK,stroke_width=6,)
        y_axis = Arrow(start=DOWN*3,end=UP*3,buff=0,color=BLACK,stroke_width=6,)

        #Lines
        right_line=Line(ORIGIN,UR*2.2,color=PINK,stroke_width=6)
        left_line=Line(ORIGIN,UL*2.2,color=PINK,stroke_width=6)
        self.add(x_axis,y_axis,right_line,left_line)

        # Labels
        x_label=MathTex("x",font_size=25,color=BLACK).next_to(x_axis.get_end()).scale(2)
        y_label=MathTex("y",font_size=25,color=BLACK).next_to(y_axis.get_end(),UP).scale(2)
        self.add(x_label, y_label)
        
        eq_1=MathTex("y=x",font_size=50,color=BLACK).next_to(right_line.get_end(),UP*0.4+RIGHT*0.4)
        eq_2=MathTex("y=-x",font_size=50,color=BLACK).next_to(left_line.get_end(),UP*0.4+LEFT*0.4)
        self.add(eq_1,eq_2)
        
        pos_1=MathTex("x>0",font_size=35,color=BLACK).move_to(RIGHT*1.2+UP*0.3)
        pos_2=MathTex("x<0",font_size=35,color=BLACK).move_to(LEFT*1.2+UP*0.3)
        point=MathTex("0",font_size=50,color=BLACK).next_to(ORIGIN,DOWN*0.6+LEFT)
        self.add(pos_1,pos_2,point)
        

        

        
