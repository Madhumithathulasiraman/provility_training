from manim import *

config.background_color = WHITE
config.frame_width=15


class ExactGraph(Scene):
    def construct(self):

        axes = Axes(x_range=[-3.9, 3.9, 1],y_range=[-1.9, 5, 1],x_length=11,y_length=8,axis_config={"color": BLACK,"stroke_width": 4,"include_ticks":True,"tick_size": 0.12,},tips=False).set_z_index(10)
        axes.x_axis.add_tip(tip_length=0.35, tip_width=0.35)
        axes.y_axis.add_tip(tip_length=0.35, tip_width=0.35)
        axes.x_axis.tip.set_fill(BLACK)
        axes.y_axis.tip.set_fill(BLACK)
    
        left_line = axes.plot(lambda x: -x - 2,x_range=[-4, -2],color="#9B09C8",stroke_width=4).shift(LEFT*0.1)
        middle_line = axes.plot(lambda x:(4.5/3)*(x + 2),x_range=[-2.17,1],color="#9B09C8",stroke_width=4).shift(LEFT*0.06).scale(0.9)
        right_line = axes.plot(lambda x: (x - 1),x_range=[1, 4],color="#F4930B",stroke_width=4).shift(LEFT*0.2)
        middle_line2 = axes.plot(lambda x: -x + 1,x_range=[-3, 1],color="#F4930B",stroke_width=4).shift(LEFT*0.23)
        dash1 = DashedLine(axes.c2p(-2, 0),axes.c2p(-2,3.6),dash_length=0.15,stroke_width=3,color="#27F5E0").shift(LEFT*0.08)
        dash2 = DashedLine(axes.c2p(1, 0),axes.c2p(1, 4.3),dash_length=0.15,stroke_width=3,color="#27F5E0").shift(LEFT*0.22)

        self.add(axes, left_line, middle_line,middle_line2 ,right_line, dash1, dash2)

        x_labels = VGroup()
        for x in range(-3,4):
            if x != 0:
                label = MathTex(str(x),color=BLACK)
                label.scale(0.6)
                label.next_to(axes.c2p(x,0) ,DOWN, buff=0.15)
                x_labels.add(label)
                self.add(axes, x_labels)
        label1=MathTex("x",color=BLACK)
        label1.next_to(axes.c2p(4.4,0),UP*0.1+LEFT*1)
        label2=MathTex("y",color=BLACK)
        label2.next_to(axes.c2p(0,4),UP*3.5+RIGHT*0.9)
        label3=MathTex("|x+2|",color=BLACK,font_size=30)
        label3.move_to(left_line)
        label3.rotate(16*PI/9).shift(UP*0.3)
        label4=MathTex("|x-1|",color=BLACK,font_size=30)
        label4.move_to(right_line)
        label4.rotate(PI/4).shift(UP*0.3)

        self.add(label1,label2,label3,label4)