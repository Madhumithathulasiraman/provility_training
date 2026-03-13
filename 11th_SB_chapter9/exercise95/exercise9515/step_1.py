from manim import *

config.pixel_width =3000
config.pixel_height =3000
config.frame_width = 14
config.frame_height = 8

class ExerciseAnswer9515a(Scene):
    def construct(self):
        self.camera.background_color = WHITE

       
        axes = Axes(x_range=[-3, 5, 1],y_range=[-3, 10, 1],x_length=8,y_length=6,axis_config={"color":BLACK,"stroke_width":3,"include_ticks":False},tips=False)
        axes.x_axis.add_tip()
        axes.x_axis.add_tip(at_start=True)
        axes.y_axis.add_tip()
        axes.y_axis.add_tip(at_start=True)
        

      
        x0 = 2
        left_curve = axes.plot(lambda x: 3 - 0.1*(x+1)**2,x_range=[-3, x0],color=PINK,stroke_width=5).shift(UP*1.8).set_z_index(10)
        right_curve = axes.plot(lambda x: 1.3*(x-x0)**2 + 2.2,x_range=[x0, 4],color="#0929C8",stroke_width=5)
        open_circle = Circle(radius=0.12, color=BLACK, stroke_width=4)
        open_circle.set_fill(WHITE, opacity=1)
        open_circle.move_to(axes.c2p(x0,2.2))
        filled_dot = Dot(axes.c2p(x0, 6),color=RED).scale(1.2).set_z_index(10)
        v_line = Line(axes.c2p(x0, 0),axes.c2p(x0, 6),color="#8B1A1A",stroke_width=5)

        
        x_label = MathTex("x", color=BLACK).scale(1.2)
        x_label.next_to(axes.x_axis.get_end(), RIGHT*0.1)
        x_label1 = MathTex("x'", color=BLACK).scale(1.2)
        x_label1.next_to(axes.x_axis.get_start(),LEFT*0.1)

        y_label = MathTex("y", color=BLACK).scale(1.2)
        y_label.next_to(axes.y_axis.get_end(), UP*0.1)
        y_label1 = MathTex("y'", color=BLACK).scale(1.2)
        y_label1.next_to(axes.y_axis.get_start(), DOWN*0.1)

        zero_label = MathTex("0", color=BLACK).scale(1.2)
        zero_label.next_to(axes.c2p(0, 0), DOWN+LEFT, buff=0.2)

        x0_label = MathTex("x_0", color=BLACK).scale(1.5)
        x0_label.next_to(axes.c2p(x0, 0), DOWN, buff=0.2)

        self.add(
            axes,
            left_curve,
            right_curve,
            v_line,
            open_circle,
            filled_dot,
            x_label,
            y_label,
            zero_label,
            x0_label,x_label1, y_label1
        )

        x0 = 2
        y1 = 4
        y2 = 1
        p1 = axes.c2p(x0, y1)
        p2 = axes.c2p(x0, y2)
        brace = BraceBetweenPoints(p1, p2, direction=RIGHT,color=BLACK).shift(UP*0.8)
        brace.set_stroke(width=0.01)
        self.add(axes, brace)

        arrow = Arrow(start=LEFT * 2,end=RIGHT * 2,color=PINK,buff=0).scale(0.8).shift(LEFT*1+UP*0.7)
        arrow2= Arrow(start=RIGHT * 2,end=LEFT * 2,color="#0929C8",buff=0).scale(0.65).shift(RIGHT*2.6+DOWN*1)
        label = MathTex("x_0^{-}", color=BLACK)
        label.next_to(arrow.get_center(),RIGHT*1.5+DOWN*0.6).scale(0.8)
        label1 = MathTex("x_0^{+}", color=BLACK)
        label1.next_to(arrow2.get_center(),DOWN*0.1).scale(0.8)
        self.add(arrow,arrow2,label, label1)
        
        eq1 = MathTex(r"\text{There exist a gap between } x_0^{+} \text{ and } x_0^{-}", color=BLACK).scale(0.5)
        eq2 = MathTex(r"(ie)\lim_{x \to x_0^-} f(x) = f(x_0) \neq \lim_{x \to x_0^+} f(x)", color=BLACK).scale(0.5)
        eq3=MathTex(r"\Rightarrow \text{ Not continuous at } x = x_0",color=BLACK).scale(0.5)
        group = VGroup(eq1, eq2,eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        box = SurroundingRectangle(group, color=BLACK, buff=0.1,stroke_width=2.5)
        full_box = VGroup(box, group) 
        full_box.scale(0.9)  
        full_box.shift(UP*0.3+ RIGHT*5)
        self.add(full_box)
        arrow = Arrow(brace.get_right(),full_box.get_left(),buff=0,color=BLACK,stroke_width=2.5,tip_length=0.15)
        self.add(arrow)