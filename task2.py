from manim import *
config.frame_height=12
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class CreateShape(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        circle=Circle(radius=2,color="#9400D3",stroke_width=4,fill_color="#9400D3",fill_opacity=5)
        to_edge=circle.to_edge(UL)
        circle_label=Text("Circle",color=BLACK).scale(1).next_to(circle,DOWN)
        self.add(circle, circle_label)


        square=Square(side_length=3,color="#00FFFF",fill_color="#00FFFF",fill_opacity=5)
        next_to=square.next_to(circle,buff=1)
        square_label=Text("Square",color=BLACK).scale(1).next_to(square,DOWN,buff=0.8)
        self.add(square, square_label)


        triangle=Triangle(color="#A52A2A",fill_color="#A52A2A",fill_opacity=4).scale(2)
        to_edge=triangle.to_edge(UR,buff=1)
        triangle_label=Text("Triangle",color=BLACK).scale(1).next_to(triangle,DOWN,buff=0.7)
        self.add(triangle, triangle_label)


        rectangle=Rectangle(color="#0000FF",fill_color="#0000FF",fill_opacity=3).scale(1)
        to_edge=rectangle.to_edge(DL)
        rectangle_label=Text("Rectangle",color=BLACK).scale(1).next_to(rectangle,DOWN)
        self.add(rectangle, rectangle_label)


        polygon=Polygon([0.2,-1,0],[2,0,0],[0.8,1,0],color="#008000",fill_color="#008000",fill_opacity=3)
        next_to=polygon.next_to(rectangle,buff=2)
        polygon_label=Text("Polygon",color=BLACK).scale(1).next_to(polygon,DOWN)
        self.add(polygon, polygon_label)



        ellipse=Ellipse(color=BLACK,fill_color=BLACK,fill_opacity=3).scale(2)
        next_to=ellipse.next_to(polygon,buff=2)
        ellipse_label=Text("Ellipse",color=BLACK).scale(1).next_to(ellipse,DOWN)
        self.add(ellipse, ellipse_label)

    