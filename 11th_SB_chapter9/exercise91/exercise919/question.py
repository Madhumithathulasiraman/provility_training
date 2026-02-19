from manim import *

config.frame_width=15
config.frame_height=20
config.pixel_width=2500
config.pixel_height=2500

config.background_color = WHITE

class Exercise919(Scene):
    def construct(self):

        #Axes
        axes=Axes(x_range=[-2.3,6,1],y_range=[-1,6,1],x_length=10,y_length=7,axis_config={"color":"#13633B","stroke_width":6},tips=True)
        labels=axes.get_axis_labels(x_label=MathTex("x",color=BLACK),y_label=MathTex("y", color=BLACK))
        line=axes.plot(lambda x:-x+4,color="#25357E",stroke_width=6)
        labels_left=VGroup(MathTex("-2",font_size=40,color=BLACK).next_to(axes.c2p(-2, 0),DOWN*0.5),MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(-1, 0),DOWN*0.5),)
        y_labels=VGroup(MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(0,-1),LEFT*0.6))
        labels_right=VGroup(*[MathTex(str(i),font_size=40,color=BLACK).next_to(axes.c2p(i,0),DOWN*0.5)for i in range(1,6)])
        labels_up=VGroup(*[MathTex(str(i),font_size=40,color=BLACK).next_to(axes.c2p(0,i),LEFT*0.6)for i in range(1,6)])
        dot=Dot(axes.coords_to_point(2,0),color=BLUE)
        
        hole=Circle(radius=0.15,color="#25357E",stroke_width=6)
        hole.move_to(axes.c2p(2,2))
        hole.set_fill(WHITE,opacity=1)

        self.add(axes,labels,labels_left,y_labels,labels_right,labels_up,dot)
        self.add(line)
        self.add(hole)
