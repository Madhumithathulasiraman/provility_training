from manim import *
config.frame_height=12
config.frame_width=16
config.pixel_width=2500
config.pixel_height=2500
class Axis(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        x_axis=Line(start=LEFT*7,end=RIGHT*7,color=BLACK)
        y_axis=Line(start=UP*7,end=DOWN*7,color=BLACK)
        x_axis.add_tip(),x_axis.add_tip(at_start=True)
        y_axis.add_tip(),y_axis.add_tip(at_start=True)
        self.add(x_axis,y_axis,)
        #line creation x_axis
        tick_1=Line([-1,-0.20,0],[-1,0.20,0],color=BLACK)
        tick_2=Line([-2,-0.20,0],[-2,0.20,0],color=BLACK)
        tick_3=Line([-3,-0.20,0],[-3,0.20,0],color=BLACK)
        tick_4=Line([-4,-0.20,0],[-4,0.20,0],color=BLACK)
        tick_5=Line([-5,-0.20,0],[-5,0.20,0],color=BLACK)
        tick_6=Line([-6,-0.20,0],[-6,0.20,0],color=BLACK)
        tick_7=Line([1,-0.20,0],[1,0.20,0],color=BLACK)
        tick_8=Line([2,-0.20,0],[2,0.20,0],color=BLACK)
        tick_9=Line([3,-0.20,0],[3,0.20,0],color=BLACK)
        tick_10=Line([4,-0.20,0],[4,0.20,0],color=BLACK)
        tick_11=Line([5,-0.20,0],[5,0.20,0],color=BLACK)
        tick_12=Line([6,-0.20,0],[6,0.20,0],color=BLACK)
        self.add(tick_1,tick_2,tick_3,tick_4,tick_5,tick_6,tick_7,tick_8,tick_9,tick_10,tick_11,tick_12)
        #line creation y_axis
        tick_1=Line([-0.20,-1,0],[0.20,-1,0],color=BLACK)
        tick_2=Line([-0.20,-2,0],[0.20,-2,0],color=BLACK)
        tick_3=Line([-0.20,-3,0],[0.20,-3,0],color=BLACK)
        tick_4=Line([-0.20,-4,0],[0.20,-4,0],color=BLACK)
        tick_5=Line([-0.20,-5,0],[0.20,-5,0],color=BLACK)
        tick_6=Line([-0.20,-6,0],[0.20,-6,0],color=BLACK)
        tick_7=Line([0.20,1,0],[-0.20,1,0],color=BLACK)
        tick_8=Line([0.20,2,0],[-0.20,2,0],color=BLACK)
        tick_9=Line([0.20,3,0],[-0.20,3,0],color=BLACK)
        tick_10=Line([0.20,4,0],[-0.20,4,0],color=BLACK)
        tick_11=Line([0.20,5,0],[-0.20,5,0],color=BLACK)
        tick_12=Line([0.20,6,0],[-0.20,6,0],color=BLACK)
        self.add(tick_1,tick_2,tick_3,tick_4,tick_5,tick_6,tick_7,tick_8,tick_9,tick_10,tick_11,tick_12)
        #label
        x_label=MathTex("X",color=BLACK).next_to(RIGHT*6.9)
        x1_label=MathTex("X'",color=BLACK).next_to(LEFT*8)
        y_label=MathTex("Y",color=BLACK).next_to(UP*7)
        y1_label=MathTex("Y'",color=BLACK).next_to(DOWN*7)
        dot=Dot(ORIGIN,color=BLACK).scale(1.5)
        self.add(x_label,x1_label,y_label,y1_label,dot)
        
        
