from manim import *

config.background_color = WHITE
config.frame_width=15


class ExerciseAnswer952(Scene):
    def construct(self):

        axes = Axes(x_range=[-3.9, 3.9, 1],y_range=[-1.9, 5, 1],x_length=11,y_length=8,axis_config={"color": BLACK,"stroke_width":3.5,"include_ticks":False,"tick_size": 0.12,},tips=False).set_z_index(10)
        axes.x_axis.add_tip(tip_length=0.35, tip_width=0.35)
        axes.y_axis.add_tip(tip_length=0.35, tip_width=0.35)
        axes.x_axis.add_tip(at_start=True,tip_length=0.35, tip_width=0.35)
        axes.y_axis.add_tip(at_start=True,tip_length=0.35, tip_width=0.35)
        

        axes.x_axis.tip.set_fill(BLACK)
        axes.y_axis.tip.set_fill(BLACK)
    
        left_line = axes.plot(lambda x: -x - 2,x_range=[-4, -2],color="#9B09C8",stroke_width=4).shift(LEFT*0.1)
        start = axes.c2p(-4, -(-4) - 2)
        end = axes.c2p(-2.05, -(-2) - 2)

        left_line = Arrow(end,start,buff=0,color="#9B09C8",stroke_width=4,tip_length=0.25)

        self.add(left_line)
        middle_line = axes.plot(lambda x:(4.5/3)*(x + 2),x_range=[-2.17,1],color="#9B09C8",stroke_width=4).shift(LEFT*0.06).scale(0.9)
        start = axes.c2p(-2.19, (4.5/3)*(-2.17 + 2))
        end = axes.c2p(1, (4.5/3)*(1 + 2))

        middle_line = Arrow(start,end,buff=0,color="#9B09C8",stroke_width=4,tip_length=0.25).shift(LEFT * 0.06).scale(0.9)

        self.add(middle_line)
        right_line = axes.plot(lambda x: (x - 1),x_range=[1, 4],color="#F4930B",stroke_width=4).shift(LEFT*0.2)
        start = axes.c2p(1, (1 - 1))     
        end = axes.c2p(4, (4 - 1))    

        right_line = Arrow(start,end,buff=0,color="#F4930B",stroke_width=4,tip_length=0.25).shift(LEFT * 0.2)

        self.add(right_line)
        middle_line2 = axes.plot(lambda x: -x + 1,x_range=[-3, 1],color="#F4930B",stroke_width=4).shift(LEFT*0.23)
        start = axes.c2p(-3, -(-3) + 1)   
        end = axes.c2p(1, -(1) + 1)       

        middle_line2 = Arrow(end,start,buff=0,color="#F4930B",stroke_width=4,tip_length=0.25).shift(LEFT * 0.23)

        self.add(middle_line2)
        dash1 = DashedLine(axes.c2p(-2, 0),axes.c2p(-2,3.6),dash_length=0.15,stroke_width=3,color="#27F5E0").shift(LEFT*0.08)
        dash2 = DashedLine(axes.c2p(1, 0),axes.c2p(1, 4.3),dash_length=0.15,stroke_width=3,color="#27F5E0").shift(LEFT*0.22)

        self.add(axes, left_line, middle_line,middle_line2 ,right_line, dash1, dash2)

        x_labels = VGroup()
        x_ticks = VGroup()
        for x in range(-2, 3):
            if x != 0:
                label = MathTex(str(x), color=BLACK)
                label.scale(0.6)
                label.next_to(axes.c2p(x,0), DOWN, buff=0.15)
                x_labels.add(label)
                tick = Line(axes.c2p(x, -0.08), axes.c2p(x, 0.08),color=BLACK,stroke_width=2)
                x_ticks.add(tick)
                if x == 1:
                    tick.shift(LEFT*0.22)
                    x_ticks.add(tick)
                if x == -2:
                    tick.shift(LEFT*0.08)
                    x_ticks.add(tick)

        self.add(axes, x_ticks, x_labels)
        label1=MathTex("x",color=BLACK)
        label1.next_to(axes.c2p(4.4,0),UP*0.1+LEFT*1)
        label2=MathTex("y",color=BLACK)
        label2.next_to(axes.c2p(0,4),UP*3.5+RIGHT*0.9)
        label3=MathTex("f(x)=|x+2|",color=BLACK,font_size=25)
        label3.move_to(left_line).shift(LEFT*1.2)
        label4=MathTex("f(x)=|x-1|",color=BLACK,font_size=25)
        label4.move_to(dash2).shift(DOWN*1)
        label5=MathTex("x'",color=BLACK)
        label5.next_to(axes.c2p(-4.2,0),UP*0.1)
        label6=MathTex("y'",color=BLACK)
        label6.next_to(axes.c2p(0,-1.8),RIGHT*0.9)
        zero_label = MathTex("0", color=BLACK).scale(0.6)
        zero_label.next_to(axes.c2p(0, 0),DOWN+LEFT,buff=0.1)

        

        self.add(label1,label2,label3,label4,label5,label6,zero_label)

              