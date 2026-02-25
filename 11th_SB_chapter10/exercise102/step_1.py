from manim import *

config.background_color=WHITE
config.frame_width=10
config.frame_height=4
config.pixel_width=2800
config.pixel_height=2800

class Exercise10220(Scene):
    def construct(self):
        
        axes = Axes(x_range=[-3.9, 3.9, 1],y_range=[-10.9, 11.9, 2],axis_config={"include_tip": True,"color":BLACK,"tick_size": 0.07,"stroke_width":4,"tip_length": 0.2,"tip_width": 0.2},x_length=6,y_length=8,).add_coordinates()
        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = MathTex("f(x)", color=BLACK).next_to(axes.y_axis.get_end(), UP)
        graph = axes.plot(lambda x: 4*x - 5, x_range=[-1.3, 2.3],color="#9434CB")
        points = [axes.c2p(0, -5),axes.c2p(1, -1),axes.c2p(2, 3),axes.c2p(-1, -9)]

        dots = VGroup(*[Dot(point=p, color="#0C6A0C", radius=0.08)for p in points])
        self.add(axes,x_label,y_label,graph,dots)
        
        x_labels = VGroup()
        for x in range(-3, 4):
            if x != 0:
                label = MathTex(str(x), color=BLACK)
                label.scale(0.5)
                label.next_to(axes.c2p(x, 0), DOWN, buff=0.13)
                x_labels.add(label)
        y_labels = VGroup()
        for y in range(-10, 12, 2):
            if y != 0:
               label = MathTex(str(y), color=BLACK)
               label.scale(0.5)
               label.next_to(axes.c2p(0, y), LEFT, buff=0.15)
               y_labels.add(label)

        self.add(x_labels, y_labels)

        