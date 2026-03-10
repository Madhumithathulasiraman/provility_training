from manim import *


config.background_color=WHITE
config.frame_width=10
config.frame_height=4
config.pixel_width=2800
config.pixel_height=2800

class Example121(Scene):
    def construct(self):



        pts = [[-4.3,0,0],[-3.5,1.5,0],[-0.5,3.5,0],[1.9,2.5,0],[3.5,0.5,0],[2,-2.9,0],[-1.7,-2,0],[-3.5,-1.62,0],[-4.3,0,0],]

        curve = VMobject()
        curve.set_points_smoothly(pts)
        curve.set_stroke(BLACK,5)
        line1 = Line(pts[0], pts[4], color=BLACK, stroke_width=4)
        start_point = [-2.1,-2.1,0] + UP*0.2
        line2 = Line(start_point, pts[4], color=BLACK, stroke_width=4)
        tick1 = Line(LEFT*0.12, RIGHT*0.12,color=BLACK).rotate(line2.get_angle()+PI/1.75)
        tick1.move_to(line2.get_start()).set_z_index(10)
        tick2 = Line(LEFT*0.12, RIGHT*0.12,color=BLACK).rotate(line2.get_angle()+PI/2)
        tick2.move_to(line2.get_end()).set_z_index(10)
        self.add(line2, tick1, tick2)
        triA = Polygon(pts[0], pts[4], [-2.5,40,0])
        triB = Polygon(pts[0], pts[4], [1.5,-15,0])
        triC = Polygon([-2.1,-1.9,0], pts[4], [5,-9,0])
        regionA = Intersection(curve, triA).set_fill("#EACFBD", opacity=1).set_stroke(width=0)
        regionB = Intersection(curve, triB).set_fill("#cfe3cf", opacity=1).set_stroke(width=0)
        regionC = Intersection(curve, triC).set_fill("#F0E68C", opacity=1).set_stroke(width=0)
        A = Text("A",color=BLACK).move_to([0,1.2,0])
        B = Text("B",color=BLACK).move_to([-1.7,-0.7,0])
        C = Text("C",color=BLACK).move_to([1,-2,0])
        S = Text("S",color=BLACK).shift(RIGHT*2.1+UP*3)

        self.add(regionA,regionB,regionC)
        self.add(curve,line1,line2)
        self.add(A,B,C,S)

        
        