from manim import *
import numpy as np


config.frame_width=15
config.frame_height=20
config.pixel_width=2500
config.pixel_height=2500
config.background_color=WHITE

 

class BoatScene(Scene):
    def construct(self):
        P=Dot(np.array([-5.9,-3,0]),color=PINK,stroke_width=4)
        A=Dot(np.array([0.2,-3,0]),color=PINK,stroke_width=4)
        B=Dot(np.array([3,3,0]),color=PINK,stroke_width=4)
        PA=Line(P,A,color=ORANGE)
        AB=Line(A,B,color=ORANGE)
        PB=DashedVMobject(Line(P.get_center(),B.get_center(),color=ORANGE),num_dashes=75)
        image=ImageMobject("boat.png")
        image.scale(0.2).shift(UR*2.1,+RIGHT*1.9)
        self.add(PA,AB,PB,image,P,A,B)
        P_label=MathTex("P",color=BLACK).next_to(P,DOWN)
        A_label=MathTex("A",color=BLACK).next_to(A,DOWN)
        B_label=MathTex("B",color=BLACK).next_to(B,UP)
        label=Text("Port",color=BLACK,font_size=35).next_to(P,LEFT*2).shift(DOWN*0.5)
        label_1=Text("10km",color=BLACK,font_size=25).next_to(P,RIGHT*10).shift(DOWN*0.3)     
        label_2=Text("8km",color=BLACK,font_size=25).rotate(AB.get_angle()).move_to(AB.get_midpoint()).shift(LEFT*0.3)
        self.add(P_label,A_label,B_label,label,label_1,label_2)
        angle_60=DashedLine(A.get_center(),A.get_center() + RIGHT*2,color=RED)
        angle=Angle(angle_60,AB,radius=0.7,color=PINK)
        angle_label=MathTex("60^\\circ",font_size=34,color=BLACK).next_to(angle,RIGHT*0.5).shift(UP*0.3)
        self.add(angle_60,angle,angle_label)



       

       
        








        

