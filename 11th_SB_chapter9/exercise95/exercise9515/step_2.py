from manim import *

config.pixel_width =3000
config.pixel_height =3000
config.frame_width = 14
config.frame_height = 8

config.background_color = WHITE

class ExerciseAnswer9515b(Scene):
    def construct(self):

        
        axes=Axes(x_range=[-1.5, 8, 1],y_range=[-1.9, 6, 1],x_length=10,y_length=6,axis_config={"color":BLACK, "stroke_width":3,"include_ticks":False},tips=False)
        axes.x_axis.add_tip(tip_length=0.25, tip_width=0.25)
        axes.x_axis.set_z_index(10)
        axes.x_axis.add_tip(at_start=True,tip_length=0.25, tip_width=0.25)
        axes.y_axis.add_tip(tip_length=0.25, tip_width=0.25)
        axes.y_axis.add_tip(at_start=True,tip_length=0.25, tip_width=0.25)
        x_label =MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT*0.1)
        y_label =MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP*0.1)
        x_label1=MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(), LEFT*0.1)
        y_label1=MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(), DOWN*0.1)
        zero = MathTex("0", color=BLACK).scale(1)
        zero.next_to(axes.c2p(0,0),DOWN+LEFT, buff=0.2)
        def f(x):
            return 0.15*(x-2.5)**2 +3

        curve=axes.plot(f,x_range=[-1,7],color="#0055FF",stroke_width=4)
        x0=5
        y0=f(x0)

        v_line =Line(axes.c2p(x0,0),axes.c2p(x0,4),color="#CCCC33",stroke_width=4)
        open_dot = Circle(radius=0.12, color=ORANGE,stroke_width=4)
        open_dot.set_fill(WHITE,opacity=1)
        open_dot.move_to(axes.c2p(x0, y0))
        

        x0_label = MathTex("x_0", color=BLACK)
        x0_label.next_to(axes.c2p(x0, 0),DOWN,buff=0.2)

        self.add(axes, x_label1, y_label1,curve,v_line,open_dot,x_label,y_label,zero,x0_label)

        arrow = Arrow(start=LEFT * 1,end=RIGHT * 1,color=RED,buff=0,tip_length=0.2).scale(0.5).shift(RIGHT*1+UP*1.5)
        arrow2= Arrow(start=RIGHT * 1,end=LEFT * 1,color=RED,buff=0,tip_length=0.2).scale(0.5).shift(RIGHT*2.6+UP*1.5)
        label = MathTex("x_0^{+}", color=BLACK)
        label.next_to(arrow.get_center(),LEFT*0.1+UP*0.1).scale(0.8)
        label1 = MathTex("x_0^{-}", color=BLACK)
        label1.next_to(arrow2.get_center(),UP*0.01+RIGHT*0.1).scale(0.8)
        self.add(arrow,arrow2,label, label1)
        eq1 = MathTex( r"f(x) \neq f(x_0)", color=BLACK).scale(0.5)
        eq2 = MathTex( r"\text{But} \lim_{x \to x_0^{+}} f(x) \neq \lim_{x \to x_0^{-}} f(x)", color=BLACK).scale(0.5)
        eq3=MathTex(r"\text{Not continuous at } x = x_0",color=BLACK).scale(0.5)
        group = VGroup(eq1, eq2,eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        box = SurroundingRectangle(group, color=BLACK, buff=0.1,stroke_width=2.5)
        full_box = VGroup(box, group) 
        full_box.scale(0.9)  
        full_box.shift(UP*3+ RIGHT*1)
        self.add(full_box)
        arrow_up = Arrow(DOWN,UP,buff=0,color=BLACK,stroke_width=2,tip_length=0.15).scale(0.37).shift(UP*1.9+RIGHT*1.85)
        self.add(arrow_up)