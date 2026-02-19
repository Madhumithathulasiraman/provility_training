from manim import *

config.frame_width=12
config.frame_height=20
config.pixel_width=2500
config.pixel_height=2500
config.background_color=WHITE

class Balloon(Scene):
    def construct(self):
        #LINE CREATION
        PA=Line([-5,-2,0],[1,-2,0],color="#F527D6").set_z_index(10)
        AB=Line([1,-2,0],[1,0,0],color="#F527D6").set_z_index(10)
        BC=Line([1,0,0],[1,2,0],color="#F527D6")
        PC=Line([-5,-2,0],[1,2,0],color="#F527D6")
        PB=Line([-5,-2,0],[1,0,0],color="#F527D6")
        t_line= Line(start=[1,0,0],end=[1,-2,0],color=BLACK).add_tip(at_start=True).next_to(AB,RIGHT*9).shift(DOWN*-0.1)
        self.add(PA,AB,BC,PC,PB,t_line)
        # LABEL&DOT
        P=Dot(point=[-5,-2,0],color="#2735F5").scale(1)
        label=MathTex("P",color=BLACK).next_to(P,DOWN)
        point_label=Text("Car Parked Point",font_size=20,color="#F58727").next_to(P,DOWN*3)
        self.add(P,label,point_label)

        A=Dot(point=[1,-2,0],color="#2735F5").scale(1)
        label=MathTex("A",color=BLACK).next_to(A,DOWN)      
        point_label=Text("Ground Point",font_size=20,color="#F58727").next_to(A,DOWN*3)
        self.add(A,label,point_label)

        B=Dot(point=[1,0,0],color="#2735F5").scale(1)
        label=MathTex("B",color=BLACK).next_to(B,RIGHT)        
        LineB= DashedLine(start=B.get_center(),end=B.get_center()+LEFT*6,color=BLACK,dash_length=0.2,dashed_ratio=0.7)
        self.add(B,label,LineB)

        C=Dot(point=[1,2,0],color="#2735F5").scale(1)
        label=MathTex("C",color=BLACK).next_to(C,RIGHT)
        self.add(C,label)

        label_PA=MathTex("100m",font_size=30,color=BLACK).shift(DL*2.2)
        label_AB=MathTex("100m",font_size=30,color=BLACK).next_to(B,RIGHT).shift(DOWN)
        label_BC=MathTex("x=?",font_size=30,color=BLACK).next_to(C,RIGHT).shift(DOWN)
        t_label=Tex("t=15s",font_size=58,color=BLACK).next_to(AB,buff=2.7)       
        self.add(label_PA,label_AB,label_BC,t_label)
        K=Dot(point=[-5.2,0,0],color=WHITE).scale(1)
        self.add(K)


        #ANGLE 
        
        BPA=Angle(Line(P.get_center(),B.get_center()),Line(P.get_center(),A.get_center()),radius=1,color=BLACK,other_angle=True)
        KBP=Angle(Line(B.get_center(),K.get_center()),Line(B.get_center(),P.get_center()),radius=1,color=BLACK,other_angle=False)
        tip=Line(start=[0,-0.1,0],end=[0,0.1,0],color=BLACK).add_tip(tip_length=0.2,tip_width=0.3).shift(LEFT*-0)

        BPA_label=MathTex("45^\\circ",font_size=30,color=BLACK).next_to(BPA)
        KBP_label=MathTex("45^\\circ",font_size=30,color=BLACK).next_to(KBP,LEFT)        
        angle=Square(side_length=0.4,color=BLACK).shift(DOWN*1.8,LEFT*-0.8).set_z_index(9)
        self.add(BPA,KBP,tip,BPA_label,KBP_label,angle)
        
        #IMAGE
        image_C=ImageMobject("balloon.png").scale(0.5)
        image_C.scale(0.13).shift(UP*2+RIGHT*2.2)
        image_B=ImageMobject("balloon.png").scale(0.5)
        image_B.scale(0.13).shift(DOWN*-0.1+RIGHT*2.2)
        self.add(image_C,image_B)