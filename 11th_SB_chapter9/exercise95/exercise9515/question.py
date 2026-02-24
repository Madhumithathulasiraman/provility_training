from manim import *

config.background_color = WHITE
config.frame_width=20


class FourGraphs(Scene):
    def construct(self):

        # ---------------- GRAPH 1 (Question Image 1) ----------------
        q_image1 = ImageMobject("question1.png").scale(0.6)
        graph1 = Group(q_image1)


        # ---------------- GRAPH 2 ----------------
        axes1 = Axes(
            x_range=[-1, 8, 1],
            y_range=[-1, 6, 1],
            x_length=6,
            y_length=4,
            axis_config={"color":"#057019", "include_ticks": False,"stroke_width":4},
            tips=True        )
        axes1.x_axis.tip.scale(0.7).shift(LEFT*0.2) 
        axes1.y_axis.tip.scale(0.7).shift(DOWN*0.2)
        x_label =MathTex("x", color=BLACK).next_to(axes1.x_axis.get_end(), RIGHT)
        y_label =MathTex("y", color=BLACK).next_to(axes1.y_axis.get_end(), UP)
        zero = MathTex("0", color=BLACK).scale(1)
        zero.next_to(axes1.c2p(0,0),DOWN+LEFT, buff=0.2)
        

        def f(x):
            return 0.15*(x-2.5)**2 + 3

        curve = axes1.plot(f, x_range=[-1,7], color="#0055FF")

        x0 = 5
        v_line = Line(
            axes1.c2p(x0,0.2),
            axes1.c2p(x0,3.4),
            color="#CCCC33"
        )

        open_dot = Circle(radius=0.1, color=RED).set_fill(WHITE,1)
        open_dot.move_to(axes1.c2p(x0,f(x0)))
        dot=Dot(color=PINK).scale(0.5)
        dot.move_to(axes1.c2p(x0,0)).shift(UP*0.04)
        dot2=Dot(color=PINK).scale(0.5)
        dot2.move_to(axes1.c2p(x0,x0)).shift(DOWN*0.77)

        graph2 = VGroup(axes1,x_label,y_label,zero,curve,v_line,open_dot,dot,dot2).scale(0.8)


        # ---------------- GRAPH 3 ----------------
        axes2 = Axes(
            x_range=[-2.2, 5.8, 1],
            y_range=[-3.5,4, 1],
            x_length=9,
            y_length=6,
            axis_config={"color":"#057019", "include_ticks":True,"tick_size": 0.07,"stroke_width":4},
            tips=True
        )
        axes2.x_axis.tip.scale(0.7).shift(LEFT*0.2) 
        axes2.y_axis.tip.scale(0.7).shift(DOWN*0.2)

        def func(x):
            return 1/(x-3)

        left = axes2.plot(func, x_range=[-2.1,2.71], color="#2738F5")
        right = axes2.plot(func, x_range=[3.29,5.5], color="#2738F5")

        line= DashedLine(
            axes2.c2p(3,-3.5),
            axes2.c2p(3,3.5),
            color="#9C2007"
        ).shift(RIGHT*0.1)

        # Proper label grouping
        x_labels = VGroup()
        y_labels = VGroup()

        for x in range(-2,6):
            if x != 0:
                labelx= MathTex(str(x),color=BLACK).scale(0.5)
                labelx.next_to(axes2.c2p(x,0), DOWN, buff=0.1)
                x_labels.add(labelx)

        for y in range(-3,4):
            if y != 0:
                labely= MathTex(str(y), color=BLACK).scale(0.5)
                labely.next_to(axes2.c2p(0,y), LEFT, buff=0.1)
                y_labels.add(labely)
        
        label=MathTex("x = x_0", color=BLACK)
        label.scale(1)
        label.next_to(line, RIGHT,buff=0.2).shift(DOWN*1.5)
        label2=MathTex("x",color=BLACK)
        label2.next_to(axes2.c2p(5.4,0),UP*0.1+RIGHT*1.9)
        label3=MathTex("y",color=BLACK)
        label3.next_to(axes2.c2p(0,4),UP*0.1+RIGHT*0.7)

        graph3 = VGroup(
            axes2, left, right,line,
            x_labels, y_labels,label,label2,label3
        ).scale(0.8)


        # ---------------- GRAPH 4 (Question Image 2) ----------------
        q_image2 = ImageMobject("question4.png").scale(0.6)
        graph4 = Group(q_image2)


        # ---------------- ARRANGE 2×2 ----------------
        all_graphs = Group(graph1, graph2, graph3, graph4)
        all_graphs.arrange_in_grid(rows=2, cols=2, buff=1)
        all_graphs.move_to(ORIGIN)

        self.add(all_graphs)