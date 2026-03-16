from manim import *

config.background_color = WHITE
config.frame_width =20
config.frame_height =10
config.pixel_width = 3000
config.pixel_height = 3000


class Exercise10220(Scene):
    def construct(self):

        axes = Axes(x_range=[-3.9, 5.9, 1],y_range=[-15, 8, 1],axis_config={"color": BLACK,"stroke_width": 3,},
        x_axis_config={"include_tip": True,"tick_size": 0.1,"tip_length": 0.2,"tip_width": 0.2,},
        y_axis_config={"include_tip": True,"tick_size": 0.07,"tip_length": 0.2,"tip_width": 0.2,},
        x_length=10,
        y_length=18,)
        axes.x_axis.add_tip(tip_length=0.4,tip_width=0.2,at_start=True)
        axes.y_axis.add_tip(tip_length=0.4,tip_width=0.2,at_start=True)
        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP, buff=0.1)
        x1_label = MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(), LEFT, buff=0.1)
        y1_label = MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(), DOWN, buff=0.1)

        graph = axes.plot(lambda x: 4*x - 5,x_range=[-2.3, 3],color="#D50BF4",stroke_width=5).set_z_index(10)
        start_arrow = Arrow(graph.point_from_proportion(0.1),graph.point_from_proportion(0),buff=0,color="#D50BF4",stroke_width=0).shift(DOWN*0.1+LEFT*0.04)
        end_arrow = Arrow(graph.point_from_proportion(0.9),graph.point_from_proportion(1),buff=0,color="#D50BF4",stroke_width=0).shift(UP*0.1+RIGHT*0.04)
        self.add(graph, start_arrow, end_arrow)
        points = [axes.c2p(0, -5),axes.c2p(1, -1),axes.c2p(2, 3),axes.c2p(-1, -9),axes.c2p(-2,-13),]
        dots = VGroup(*[Dot(point=p, color="#2309C8", radius=0.08)for p in points]).set_z_index(10)
        labels = VGroup(MathTex("(0,-5)", color=BLACK).scale(0.5).next_to(dots[0], RIGHT*0.1+UP*0.1, buff=-1).rotate(PI/2.5),
                        MathTex("(1,-1)", color=BLACK).scale(0.5).next_to(dots[1], RIGHT*0.1+UP*0.1, buff=-1).rotate(PI/2.5),
                        MathTex("(2,3)", color=BLACK).scale(0.5).next_to(dots[2], LEFT*0.65+UP*0, buff=-1).rotate(PI/2.5),
                        MathTex("(-1,-9)", color=BLACK).scale(0.5).next_to(dots[3], LEFT*0.8+UP*0, buff=-1).rotate(PI/2.5),
                        MathTex("(-2,-13)", color=BLACK).scale(0.5).next_to(dots[4],LEFT*0.85+UP*0, buff=-1).rotate(PI/2.5),)
        x_labels = VGroup()
        for x in range(-3,6):
            if x != 0:
                label = MathTex(str(x), color=BLACK).scale(0.5)
                label.next_to(axes.c2p(x, 0), DOWN, buff=0.1)
                x_labels.add(label)
        y_labels = VGroup()
        for y in range(-13, 8):
            if y != 0:
                label = MathTex(str(y), color=BLACK).scale(0.5)
                label.next_to(axes.c2p(0, y), LEFT, buff=0.1)
                y_labels.add(label)
        for tick in axes.y_axis.ticks:
            y_value = axes.y_axis.p2n(tick.get_center())
            tick.shift(DOWN*0.2)
            if abs(round(y_value)) > 13:
             tick.set_opacity(0)
        for tick in axes.x_axis.get_ticks():
            x_value = axes.x_axis.p2n(tick.get_center())
            tick.shift(RIGHT*0.05)
            if abs(x_value - 1) < 0.01:
                tick.set_opacity(0)
        equ=MathTex("f'(x)=4x-5",color=BLACK).scale(0.7).shift(UP*4.5+RIGHT*0.4)
        equ.rotate(PI/2.55)
        zero_label = MathTex("0", color=BLACK).scale(0.5).next_to(axes.c2p(0,0), DOWN+LEFT, buff=0.1)
        self.add(axes, x_label, y_label,dots,labels, x_labels, y_labels,x1_label,y1_label,equ,zero_label)
        

        