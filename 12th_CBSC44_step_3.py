from manim import *
import numpy as np

config.frame_height = 15
config.frame_width = 15
config.pixel_width = 2800
config.pixel_height = 2800

class Step_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        A = LEFT*3+UP*2      
        B = LEFT*3+DOWN*4    
        C = RIGHT*2+UP*2     
        AB = Line(B,A,color=BLUE)   
        AC = Line(A,C,color=BLUE)   
        BC = Line(B,C,color=BLUE)   
        triangle = VGroup(AB, AC, BC).shift(LEFT*2)
        right_angle = RightAngle(AB, AC, length=0.5, color=BLACK, quadrant=(-1, 1))
        tick_h = VGroup(Line(LEFT*0.2, RIGHT*0.2), Line(LEFT*0.2, RIGHT*0.2).shift(DOWN*0.15)).move_to(AB.get_center()).set_color(BLACK).rotate(1*DEGREES)
        tick_r = VGroup(Line(UP*0.2, DOWN*0.2), Line(UP*0.2, DOWN*0.2).shift(RIGHT*0.15)).rotate(-1*DEGREES).move_to(AC.get_center()).set_color(BLACK)

        angle_bottom = Arc(radius=1.0,start_angle=91*DEGREES,angle=-41*DEGREES,arc_center=B,color=GREEN).shift(LEFT*2)
        angle_top = Arc(radius=1.0,start_angle=181*DEGREES,angle=48*DEGREES,arc_center=C,color=PINK).shift(LEFT*2)
        angle_bottom_label = MathTex("45^{\\circ}", color=BLACK).scale(1.2)
        angle_bottom_label.move_to(B + RIGHT*1.3 + UP*0.6).shift(LEFT*2.7+UP*1)
        angle_top_label = MathTex("45^{\\circ}", color=BLACK).scale(1.2)
        angle_top_label.move_to(C + LEFT*1.5 + DOWN*0.4).shift(LEFT*2+DOWN*0.2)

        h_label = MathTex("h", color=BLACK).scale(1.5).next_to(AB, LEFT, buff=0.4)
        r_label = MathTex("r", color=BLACK).scale(1.5).next_to(AC, UP, buff=0.4)
        l_label = MathTex("l", color=BLACK).scale(1.5).next_to(BC.get_center(), DOWN + RIGHT, buff=0.2)
        eq1 = MathTex("h = r", color=BLACK).scale(1.3)
        box1 = SurroundingRectangle(eq1, color=BLACK, buff=0.3)
        formula1 = VGroup(eq1, box1)
        eq2 = MathTex("l = \\sqrt{2} \\cdot h", color=BLACK).scale(1.3)
        box2 = SurroundingRectangle(eq2, color=BLACK, buff=0.3)
        formula2 = VGroup(eq2, box2)
        sep = MathTex(";", color=BLACK).scale(2)
        formulas = VGroup(formula1, sep, formula2).arrange(RIGHT, buff=0.6).move_to(RIGHT*3.5 + DOWN*1)
        self.add(triangle,right_angle,tick_h, tick_r,angle_bottom, angle_top,angle_bottom_label, angle_top_label,h_label, r_label, l_label,formulas)