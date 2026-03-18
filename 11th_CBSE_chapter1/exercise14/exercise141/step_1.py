from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 15
config.pixel_width = 2800
config.pixel_height = 2800


class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        rectangle = Rectangle(width=9.5, height=6.5,stroke_color="#2E27F5",fill_color="#C4BEA9",fill_opacity=0.3,stroke_width=3)
        u_label = Text("U", color=BLACK, font_size=45).move_to(UR+RIGHT*3+UP*1.8)
        r = 2.2
        c1 = np.array([-1.3, 0, 0])
        c2 = np.array([1.3, 0, 0])
        circle_1 = Circle(radius=r, stroke_color="#CF27F5", stroke_width=3).move_to(c1)
        circle_2 = Circle(radius=r, stroke_color="#CF27F5", stroke_width=3).move_to(c2)
        hatch = VGroup()
        spacing = 0.4
        angle = PI/4
        direction = np.array([np.cos(angle), np.sin(angle), 0])
        normal = np.array([-direction[1], direction[0], 0])
        for t in np.arange(-6, 6, spacing):
            base = t * normal
            segments = []
            for center in [c1, c2]:
                diff = base - center
                a = np.dot(direction, direction)
                b = 2 * np.dot(diff, direction)
                c = np.dot(diff, diff) - r**2
                disc = b*b - 4*a*c
                if disc >= 0:
                    s1 = (-b - np.sqrt(disc)) / (2*a)
                    s2 = (-b + np.sqrt(disc)) / (2*a)
                    segments.append((s1, s2))
            if not segments:
                continue
            segments.sort()
            merged = [segments[0]]
            for seg in segments[1:]:
                last = merged[-1]
                if seg[0] <= last[1]:
                    merged[-1] = (last[0], max(last[1], seg[1]))
                else:
                    merged.append(seg)

           
            for s1, s2 in merged:
                eps = 0.01
                start = base + (s1 + eps) * direction
                end   = base + (s2 - eps) * direction
                line = Line(start, end,stroke_color="#0BF4EC",stroke_opacity=1,stroke_width=2.5)
                hatch.add(line)
        label1 = Text("X", color=BLACK, font_size=40).move_to(circle_1).shift(UP*2.7)
        label2 = Text("Y", color=BLACK, font_size=40).move_to(circle_2).shift(UP*2.7)
        left_value = MathTex("5", color=BLACK).move_to(circle_1.get_center() + LEFT*0.5) 
        middle_value = MathTex("3", color=BLACK).shift(LEFT*0.1) 
        right_value = MathTex("2", color=BLACK).move_to(circle_2.get_center() + RIGHT*0.5)
        outline1 = circle_1.copy().set_fill(opacity=0)
        outline2 = circle_2.copy().set_fill(opacity=0)

        self.add(rectangle,u_label,hatch,outline1, outline2,label1, label2,left_value,middle_value,right_value)