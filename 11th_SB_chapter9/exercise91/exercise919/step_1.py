from manim import *

config.frame_width=15
config.frame_height=20
config.pixel_width=2500
config.pixel_height=2500

config.background_color = WHITE

class Exercise919Answer(Scene):
    def construct(self):

        #Axes
        axes=Axes(x_range=[-3,6,1],y_range=[-2,6,1],x_length=10,y_length=10,axis_config={"color":BLACK,"stroke_width":6},tips=False)
        for tick in axes.y_axis.get_tick_marks():
            if tick.get_center()[1]<0:   
                tick.set_opacity(0)
        for tick in axes.x_axis.get_tick_marks():
            if tick.get_center()[0]<-4:
                tick.set_opacity(0)
        
        axes.x_axis.add_tip()
        axes.x_axis.add_tip(at_start=True)

        axes.y_axis.add_tip()
        axes.y_axis.add_tip(at_start=True)
        
        labels=axes.get_axis_labels(x_label=MathTex("x",color=BLACK),y_label=MathTex("y", color=BLACK))
        x1_label=MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(),LEFT*0.2+UP*0.2)
        y1_label=MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(),DOWN)
        line_1=DoubleArrow(start=axes.c2p(-1, 5),end=axes.c2p(5, -1),buff=0,stroke_width=6,color="#6241C7").shift(DOWN*0.2)
        label_eq=MathTex("y=4-x",font_size=45,color=BLACK).move_to(UP*1.5+RIGHT*0.5)

        labels_left=VGroup(MathTex("-2",font_size=40,color=BLACK).next_to(axes.c2p(-2, 0),DOWN*0.7),MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(-1, 0),DOWN*0.7),)
     
        labels_right=VGroup(*[MathTex(str(i),font_size=40,color=BLACK).next_to(axes.c2p(i,0),DOWN*0.6)for i in range(1,6)]).shift(DOWN*0.1)
        labels_up=VGroup(*[MathTex(str(i),font_size=40,color=BLACK).next_to(axes.c2p(0,i),LEFT*0.6)for i in range(1,6)])
        
        
        hole=Circle(radius=0.15,color="#6241C7",stroke_width=6)
        hole.move_to(axes.c2p(1.9,1.9)).set_z_index(2)
        hole.set_fill(WHITE,opacity=1)

        hole_2=Circle(radius=0.20,color=BLUE,stroke_width=6)
        hole_2.move_to(axes.c2p(2,0)).shift(DOWN*0.4)

        dashed_line=DashedLine(start=axes.c2p(2,2),end=axes.c2p(2,0),color=RED,stroke_width=6)
        dashed_line2=DashedLine(start=axes.c2p(0,2),end=axes.c2p(2,2),color=RED,stroke_width=6)
        self.add(dashed_line,dashed_line2)
        
        arrow_1=Arrow(LEFT*3,RIGHT*3,color=PINK,stroke_width=4,tip_length=0.3).shift(DOWN*3.3+LEFT*1.7).scale(0.8)
        arrow_2=Arrow(RIGHT*3,LEFT*3,color=PINK,stroke_width=4,tip_length=0.3).shift(DOWN*3.3+RIGHT*2.9).scale(0.8)
        arrow_3=Arrow(DOWN*2,UP*3,color=PINK,stroke_width=4,tip_length=0.3).shift(DOWN*4.5+RIGHT*0.6).scale(0.3)
        label_1=MathTex("2^{-}",color=BLACK,font_size=50)
        label_2=MathTex("2^{+}",color=BLACK,font_size=50)

        label_1.next_to(arrow_1.get_end(),LEFT*2+DOWN*1.5)
        label_2.next_to(arrow_2.get_end(),RIGHT*2+DOWN*1.5)
        self.add(arrow_1,arrow_2,arrow_3,label_1,label_2)

        zero_label = MathTex("0", color=BLACK)

        zero_label.next_to(axes.c2p(0.3,0), DOWN*0.6+LEFT*1.7)

        self.add(zero_label)
        self.add(axes,labels,label_eq,labels_left,labels_right,labels_up)
        self.add(line_1,x1_label,y1_label)
        self.add(hole,hole_2)