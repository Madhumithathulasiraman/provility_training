from manim import *

config.background_color=WHITE

class ExerciseAnswer9515d(Scene):
    def construct(self):

        axes = Axes(x_range=[-3,5,1],y_range=[-1.9,5,1],x_length=8,y_length=5,axis_config={"color":BLACK,"include_ticks":False,"stroke_width":3.5},tips=False)
        axes.x_axis.add_tip()
        axes.y_axis.add_tip()
        axes.x_axis.add_tip(at_start=True)
        axes.y_axis.add_tip(at_start=True)

        x_label = MathTex("x",color=BLACK).next_to(axes.x_axis.get_end(),RIGHT*0.1)
        y_label = MathTex("y",color=BLACK).next_to(axes.y_axis.get_end(),UP*0.1)
        x_label1 = MathTex("x'",color=BLACK).next_to(axes.x_axis.get_start(),LEFT*0.1)
        y_label1 = MathTex("y'",color=BLACK).next_to(axes.y_axis.get_start(),DOWN*0.1)

        zero = MathTex("0",color=BLACK).scale(0.8)
        zero.next_to(axes.c2p(-0.2,0),DOWN+UP*0.5)

        x0 = 2
        x0_label = MathTex("x_0",color=BLACK)
        x0_label.next_to(axes.c2p(x0,0),DOWN)
        left_curve = axes.plot(lambda x: 0.06*(x+2)**2 + 2,x_range=[-2.5,x0],color=PINK)
        right_curve = axes.plot(lambda x: 0.4*(x-x0)**2,x_range=[x0,4],color=BLUE).shift(UP*1.45)
        circle = Circle(radius=0.08,color="#3127F5")
        circle.move_to(axes.c2p(x0,3))
        circle.set_fill(WHITE,opacity=1).set_z_index(10)
        dot = Dot(axes.c2p(x0,2),color=GREEN).set_z_index(10)
        vertical = Line(axes.c2p(x0,0),axes.c2p(x0,2.95),color="#F4360B")
        self.add(axes,x_label,y_label,x_label1,y_label1,zero,x0_label,left_curve,right_curve,circle,dot,vertical)

        x0 = 2
        y1 = 1.8
        y2 = 1
        p1 = axes.c2p(x0, y1)
        p2 = axes.c2p(x0, y2)
        brace = BraceBetweenPoints(p1, p2, direction=RIGHT,color=BLACK).shift(UP*0.8)
        self.add(axes, brace)
        arrow = Arrow(start=LEFT *1,end=RIGHT *1,color=PINK,buff=0,tip_length=0.2).scale(0.5).shift(LEFT*0.1+UP*1)
        arrow2= Arrow(start=RIGHT *1,end=LEFT *1,color=BLUE,buff=0,tip_length=0.2).scale(0.5).shift(RIGHT*1.6+UP*0.1)
        label = MathTex("x_0^{-}", color=BLACK)
        label.next_to(arrow.get_center(),LEFT*0+UP*0.3).scale(0.8)
        label1 = MathTex("x_0^{+}", color=BLACK)
        label1.next_to(arrow2.get_center(),DOWN*0.1).scale(0.8)
        self.add(arrow,arrow2,label, label1)
        eq1 = MathTex(r"\text{There exist a gap between } x_0^{-} \text{ and } x_0^{+}", color=BLACK).scale(0.5)
        eq2 = MathTex(r"(ie)\lim_{x \to x_0^+}=f(x_0)\neq\lim_{x \to x_0^-} f(x)", color=BLACK).scale(0.5)
        
        group = VGroup(eq1,eq2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        box = SurroundingRectangle(group, color=BLACK, buff=0.1,stroke_width=2.5)
        full_box = VGroup(box, group) 
        full_box.scale(0.9)  
        full_box.shift(UP*2.34+ RIGHT*1.5)
        self.add(full_box)
        arrow = Arrow(DOWN,UP,buff=0,color=BLACK,stroke_width=2.5,tip_length=0.15).scale(0.55).shift(RIGHT*1.45+UP*1.25)
        self.add(arrow)