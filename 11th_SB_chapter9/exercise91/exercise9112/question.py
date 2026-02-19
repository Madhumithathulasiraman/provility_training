from manim import *

config.pixel_width = 2500
config.pixel_height = 1800
config.frame_width = 14
config.frame_height = 8

class Exercise9112(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Axes
        axes=Axes(x_range=[-2.2, 8, 1],y_range=[-2.5,3,1],x_length=12,y_length=6,axis_config={"color":"##116422","stroke_width":9,"include_ticks":True,"tick_size":0.09,})
        labels_left=VGroup(MathTex("-2",font_size=40,color=BLACK).next_to(axes.c2p(-2, 0), DOWN*0.5),MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(-1, 0),DOWN*0.5),)
        y_labels=VGroup(MathTex("-2",font_size=40,color=BLACK).next_to(axes.c2p(0,-2),LEFT*0.6),MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(0,-1),LEFT*0.6),MathTex("1",font_size=40,color=BLACK).next_to(axes.c2p(0,1),LEFT*0.5),MathTex("2",font_size=40,color=BLACK).next_to(axes.c2p(0,2), LEFT*0.5),)
        labels_right=VGroup(*[MathTex(str(i),font_size=40,color=BLACK).next_to(axes.c2p(i,0),DOWN*0.5)for i in range(1,8)])

        #labels
        axis_label_1=MathTex("x",font_size=70,color=BLACK).next_to(axes.c2p(7.7,0),UP*1.2)
        axis_label_2=MathTex("y",font_size=70,color=BLACK).next_to(axes.c2p(0,3),RIGHT*1.4)

        
        line_1=Line(axes.c2p(5,1.2),axes.c2p(8,1.2),color="#11194D",stroke_width=8)
        line_2=Line(axes.c2p(-2,-1),axes.c2p(5,-1),color="#11194D",stroke_width=8)
        zero_1=MathTex("0",font_size=45,color=BLACK).next_to(line_1.get_start(),LEFT*0.3)
        zero_2=MathTex("0",font_size=45,color=BLACK).next_to(line_2.get_end(),RIGHT*0.2)

        self.add(axes,labels_left,labels_right,y_labels,axis_label_1,axis_label_2,line_1,line_2,zero_1,zero_2)

    
