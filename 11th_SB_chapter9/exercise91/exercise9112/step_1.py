from manim import *

config.pixel_width = 2500
config.pixel_height = 1800
config.frame_width = 14
config.frame_height = 8
TIP_LEN = 0.4
TIP_WID = 0.8

class ExerciseAnswer9112(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        
        axes=Axes(x_range=[-2.2,8,1],y_range=[-2.5,3,1],x_length=12,y_length=6,axis_config={"color":BLACK,"stroke_width":4,"include_ticks":True})
        labels_right=VGroup(*[MathTex(str(i),font_size=40,color=BLACK).next_to(axes.c2p(i,0),DOWN*0.5+LEFT*0.1)for i in range(1,8)])
        for tick in axes.y_axis.get_tick_marks():
            if tick.get_center()[1]<0:   
                tick.set_opacity(0)
        for tick in axes.y_axis.get_tick_marks():
            if tick.get_center()[0]<2:   
                tick.set_opacity(0)
        for tick in axes.x_axis.get_tick_marks():
            if tick.get_center()[0]<-4:   
                tick.set_opacity(0)

        axes.x_axis.remove(axes.x_axis.tip) if hasattr(axes.x_axis, "tip") else None
        axes.y_axis.remove(axes.y_axis.tip) if hasattr(axes.y_axis, "tip") else None


        axes.x_axis.add_tip(tip_length=TIP_LEN)
        axes.x_axis.add_tip(at_start=True, tip_length=TIP_LEN)

        axes.y_axis.add_tip(tip_length=TIP_LEN)
        axes.y_axis.add_tip(at_start=True, tip_length=TIP_LEN)

        #labels
        axis_label_1=MathTex("x",font_size=55,color=BLACK).next_to(axes.c2p(7.7,0),UP*1.5+RIGHT*1)
        axis_label2=MathTex("x'",font_size=55,color=BLACK).next_to(axes.c2p(-3,0),UP*1.2+RIGHT*2)
        axis_label_2=MathTex("y",font_size=55,color=BLACK).next_to(axes.c2p(0,3),RIGHT*1)
        axis_label=MathTex("y'",font_size=55,color=BLACK).next_to(axes.c2p(0,-3),UP*1.5+RIGHT)
        
        line_1=Line(axes.c2p(5,1.2),axes.c2p(8,1.2),color="#008000",stroke_width=6).scale(0.8)
        line_2=Line(axes.c2p(-2,-1),axes.c2p(5,-1),color="#008000",stroke_width=6).scale(0.5).shift(RIGHT*1.6)
        hole=Circle(radius=0.1,color="#008000",stroke_width=6)
        hole.move_to(axes.c2p(5,0)).shift(DOWN*1+LEFT*0.3)
        hole_2=Circle(radius=0.1,color="#008000",stroke_width=6)
        hole_2.move_to(axes.c2p(5,1)).shift(UP*0.2+RIGHT*0.3)
        hole.set_fill(WHITE,opacity=2)
        hole_2.set_fill(WHITE,opacity=2)
        hole_3=Circle(radius=0.20,color="#FF0000",stroke_width=6)
        hole_3.move_to(axes.c2p(5,0)).shift(DOWN*0.12+RIGHT*0.07)

        self.add(axes,labels_right,axis_label_1,axis_label2,axis_label_2,axis_label,line_1,line_2,hole,hole_2,hole_3)

        dashed_line=DashedLine(start=axes.c2p(5,-2),end=axes.c2p(5,2),color="#834333",stroke_width=6,stroke_opacity=0.6)
        self.add(dashed_line,)
        
        arrow_1=Arrow(LEFT*3,RIGHT*3,color="#800080",stroke_width=4,tip_length=0.25).shift(DOWN*1+LEFT*0.1).scale(0.8)
        arrow_2=Arrow(RIGHT*3,LEFT*3,color="#800080",stroke_width=4,tip_length=0.25).shift(DOWN*1+RIGHT*4.2).scale(0.6)
        arrow_3=Arrow(DOWN*2,UP*3,color="#800080",stroke_width=3,tip_length=0.25).shift(DOWN*2.1+RIGHT*2.4).scale(0.2)
        label_1=MathTex("5^{-}",color=BLACK,font_size=30)
        label_2=MathTex("5^{+}",color=BLACK,font_size=30)

        label_1.next_to(arrow_1.get_end(),LEFT*1.5+DOWN*0.6)
        label_2.next_to(arrow_2.get_end(),RIGHT*1.5+DOWN*0.6)
        self.add(arrow_1,arrow_2,arrow_3,label_1,label_2)

        zero_label = MathTex("0", color=BLACK)

        zero_label.next_to(axes.c2p(0.2,0), DOWN*0.2+LEFT*1.7)
        label=MathTex("y=|x-5|/x-5",font_size=35,color=BLACK).shift(UP*1.3+RIGHT*4)

        self.add(zero_label,label)