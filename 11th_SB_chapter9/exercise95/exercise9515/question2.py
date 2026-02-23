from manim import *

config.background_color = WHITE

class Exercise9515b(Scene):
    def construct(self):

        
        axes=Axes(x_range=[-1, 8, 1],y_range=[-1, 6, 1],x_length=10,y_length=6,axis_config={"color":GREEN, "stroke_width":5,"include_ticks":False},tips=False)
        axes.x_axis.add_tip(tip_length=0.25, tip_width=0.25)
        axes.y_axis.add_tip(tip_length=0.25, tip_width=0.25)
        x_label =MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT)
        y_label =MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP)
        zero = MathTex("0", color=BLACK).scale(1)
        zero.next_to(axes.c2p(0,0),DOWN+LEFT, buff=0.2)
        def f(x):
            return 0.15*(x-2.5)**2 +3

        curve=axes.plot(f,x_range=[-1,7],color="#0055FF",stroke_width=4)
        x0=5
        y0=f(x0)

        v_line =Line(axes.c2p(x0,0.1),axes.c2p(x0,3.6),color="#CCCC33",stroke_width=4)
        open_dot = Circle(radius=0.12, color="#FF3333",stroke_width=4)
        open_dot.set_fill(WHITE,opacity=1)
        open_dot.move_to(axes.c2p(x0, y0))
        dot=Dot(color=PINK).scale(0.5)
        dot.move_to(axes.c2p(x0,0))
        dot2=Dot(color=PINK).scale(0.5)
        dot2.move_to(axes.c2p(x0,x0)).shift(DOWN*1.13)

        x0_label = MathTex("x_0", color=BLACK)
        x0_label.next_to(axes.c2p(x0, 0),DOWN,buff=0.2)

        self.add(axes,curve,v_line,open_dot,dot,dot2,x_label,y_label,zero,x0_label)