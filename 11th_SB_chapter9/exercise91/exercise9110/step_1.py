from manim import *


config.frame_width=15
config.frame_height=25
config.pixel_width=2500
config.pixel_height=2500

config.background_color=WHITE

class ExerciseAnswer9110(Scene):
    def construct(self):

       axes=Axes(x_range=[-3,6,1],y_range=[-2,4,1],x_length=10,y_length=8,axis_config={"color":BLACK,"stroke_width":4,"include_tip":True})
       for tick in axes.y_axis.get_tick_marks():
            if tick.get_center()[1]<0:   
                tick.set_opacity(0)
       for tick in axes.x_axis.get_tick_marks():
            if tick.get_center()[0]<-4:   
                tick.set_opacity(0)
       axes.x_axis.add_tip(at_start=True)
       axes.y_axis.add_tip(at_start=True)
       axes.x_axis.ticks.shift(LEFT*0.2)
       
       self.add(axes)

       graph = axes.plot(lambda x:x**2+2,x_range=[-1.5,1.5],color="#5321B0").shift(UP*0.1)
       
       self.add(graph)
       end_arrow=Arrow(axes.c2p(1.35,1.35**2+2),axes.c2p(1.5,1.5**2+2),buff=0,stroke_width=2,max_tip_length_to_length_ratio=0.4,color="#5321B0").shift(UP*0.1)
       start_arrow=Arrow(axes.c2p(-1.35,(-1.35)**2+2),axes.c2p(-1.5,(-1.5)**2+2),buff=0,stroke_width=2,max_tip_length_to_length_ratio=0.4,color="#5321B0").shift(UP*0.1)
       self.add(start_arrow,end_arrow)


       labels=axes.get_axis_labels(x_label=MathTex("x",color=BLACK),y_label=MathTex("y", color=BLACK))
       x1_label=MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(),LEFT*0.2+UP*0.2)
       y1_label=MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(),DOWN)
       label_eq=MathTex("y=x^2+2",font_size=45,color=BLACK).move_to(UP*2.5+RIGHT*0.7)
       self.add(labels,x1_label,y1_label,label_eq)


       labels_left=VGroup(MathTex("-2",font_size=40,color=BLACK).next_to(axes.c2p(-2, 0),DOWN*0.7),MathTex("-1",font_size=40,color=BLACK).next_to(axes.c2p(-1, 0),DOWN*0.7),)
     
       labels_right=VGroup(*[MathTex(str(i),font_size=40,color=BLACK).next_to(axes.c2p(i,0),DOWN*0.6)for i in range(1,6)]).shift(DOWN*0.1)
       labels_up=VGroup(*[MathTex(str(i),font_size=40,color=BLACK).next_to(axes.c2p(0,i),LEFT*0.6+UP*0.1)for i in range(1,4)])
       self.add(labels_left,labels_right,labels_up)

       hole=Circle(radius=0.20,color="#B349E4",stroke_width=6)
       hole.move_to(axes.c2p(1,0)).shift(DOWN*0.4)
       hole_2=Circle(radius=0.10,color="#2ED141",stroke_width=6)
       hole_2.move_to(axes.c2p(1,3)).shift(LEFT*0.01)
       hole_2.set_fill(WHITE,opacity=2)
       
       
       
       dashed_line=DashedLine(start=axes.c2p(0,3),end=axes.c2p(1,3),color="#36AEC9",stroke_width=6)
       dashed_line2=DashedLine(start=axes.c2p(1,0),end=axes.c2p(1,3),color="#36AEC9",stroke_width=6)
       self.add(dashed_line,dashed_line2,hole,hole_2)
        
       arrow_1=Arrow(LEFT*3,RIGHT*3,color="#FFBF00",stroke_width=4,tip_length=0.3).shift(DOWN*2.1+LEFT*2.9).scale(0.8)
       arrow_2=Arrow(RIGHT*3,LEFT*3,color="#FFBF00",stroke_width=4,tip_length=0.3).shift(DOWN*2.1+RIGHT*1.9).scale(0.8)
       arrow_3=Arrow(DOWN*2,UP*3,color="#FFBF00",stroke_width=4,tip_length=0.3).shift(DOWN*3.6+LEFT*0.5).scale(0.4)
       label_1=MathTex("1^{-}",color=BLACK,font_size=45)
       label_2=MathTex("1^{+}",color=BLACK,font_size=45)

       label_1.next_to(arrow_1.get_end(),LEFT*1+DOWN*1.5)
       label_2.next_to(arrow_2.get_end(),RIGHT*1+DOWN*1.5)
       self.add(arrow_1,arrow_2,arrow_3,label_1,label_2)

       zero_label = MathTex("0", color=BLACK)

       zero_label.next_to(axes.c2p(0.3,0), DOWN*0.6+LEFT*1.7)

       self.add(zero_label)
       dot = Dot(axes.c2p(1,1),color="#010FCC").scale(1.5).shift(UP*0.1)
       self.add(dot)
       

        