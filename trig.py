from manim import *

config.background_color=WHITE
config.frame_height=7
config.frame_width=22
config.pixel_width=2500
config.pixel_height=2500
class TrigonoMetric(Scene):
    def construct(self):
        axes=Axes(x_range=[-PI,PI,PI/2],y_range=[-3,3,0.5],x_length=6,y_length=6,tips=False,axis_config={"stroke_color":BLACK,"stroke_width":3}).shift(UL*6.1)
        graph=axes.plot(lambda x:np.sin(x),color=RED)
        x_labels={-PI:MathTex("-\\pi",color=BLACK),-PI/2:MathTex("-\\frac{\\pi}{2}",color=BLACK),PI/2:MathTex("\\frac{\\pi}{2}",color=BLACK),PI:MathTex("\\pi",color=BLACK)}
        axes.add_coordinates(x_labels)
        label=MathTex("y=\\sin x",color=RED).to_edge(UL).scale(2.5).shift(UP*7+RIGHT*3)
        self.add(axes,graph,label)
        axes=Axes(x_range=[-PI,PI,PI/2],y_range=[-2,2,0.5],x_length=6,y_length=6,tips=False,axis_config={"stroke_color":BLACK,"stroke_width":3}).next_to(axes,buff=0.5)
        graph=axes.plot(lambda x:np.cos(x),color=BLUE)
        x_labels={-PI:MathTex("-\\pi",color=BLACK),-PI/2:MathTex("-\\frac{\\pi}{2}",color=BLACK),PI/2:MathTex("\\frac{\\pi}{2}",color=BLACK),PI:MathTex("\\pi",color=BLACK)}
        axes.add_coordinates(x_labels)
        label=MathTex("y=\\cos x",color=RED).to_edge(UL).scale(2.5).shift(UP*7+RIGHT*10)
        self.add(axes, graph,label)
        axes=Axes(x_range=[-PI, PI, PI/2],y_range=[-4, 4,1],x_length=6,y_length=6,tips=False, axis_config={"stroke_color": BLACK,"stroke_width":3}).next_to(axes,buff=0.5)
        graph=axes.plot(lambda x:np.tan(x),x_range=[-1.2,1.2],color=GREEN)
        x_labels={-PI:MathTex("-\\pi",color=BLACK),-PI/2:MathTex("-\\frac{\\pi}{2}",color=BLACK),PI/2:MathTex("\\frac{\\pi}{2}",color=BLACK),PI:MathTex("\\pi",color=BLACK)}
        axes.add_coordinates(x_labels)
        label=MathTex("y=\\tan x",color=RED).to_edge(UL).scale(2.5).shift(UP*7+RIGHT*17)
        self.add(axes, graph,label)
        axes=Axes(x_range=[-PI,PI,PI/2],y_range=[-2,2,1],x_length=6,y_length=6,tips=False,axis_config={"stroke_color":BLACK,"stroke_width":3}).shift(DL*6.1)
        graph=axes.plot(lambda x:1/np.sin(x)-0.7,x_range=[0.4,PI-0.4],color=ORANGE)
        x_labels={-PI:MathTex("-\\pi",color=BLACK),-PI/2:MathTex("-\\frac{\\pi}{2}",color=BLACK),PI/2:MathTex("\\frac{\\pi}{2}",color=BLACK),PI:MathTex("\\pi",color=BLACK)}
        label=MathTex("y=\\csc x",color=RED).to_edge(UL).scale(2.5).shift(DOWN*5+RIGHT*3)
        axes.add_coordinates(x_labels)
        self.add(axes,graph,label)
        axes=Axes(x_range=[-PI,PI,PI/2],y_range=[-4,4,2],x_length=6,y_length=6,tips=False,axis_config={"stroke_color":BLACK,"stroke_width":3}).next_to(axes,buff=0.5)
        graph=axes.plot(lambda x:1/np.cos(x),x_range=[-1.3,PI-1.8],color=PURPLE)
        x_labels={-PI:MathTex("-\\pi",color=BLACK),-PI/2:MathTex("-\\frac{\\pi}{2}",color=BLACK),PI/2:MathTex("\\frac{\\pi}{2}",color=BLACK),PI:MathTex("\\pi",color=BLACK)}
        label=MathTex("y=\\sec x",color=RED).to_edge(UL).scale(2.5).shift(DOWN*5+RIGHT*10)
        axes.add_coordinates(x_labels)
        self.add(axes,graph,label)
        axes=Axes(x_range=[-PI,PI,PI/2],y_range=[-4,4,2],x_length=6,y_length=6,tips=False,axis_config={"stroke_color":BLACK,"stroke_width":3}).next_to(axes,buff=0.5)
        graph=axes.plot(lambda x:1/np.tan(x),x_range=[0.3,PI-0.3],color=PINK)
        x_labels={-PI:MathTex("-\\pi",color=BLACK),-PI/2:MathTex("-\\frac{\\pi}{2}",color=BLACK),PI/2:MathTex("\\frac{\\pi}{2}",color=BLACK),PI:MathTex("\\pi",color=BLACK)}
        axes.add_coordinates(x_labels)
        label=MathTex("y=\\cot x",color=RED).to_edge(UL).scale(2.5).shift(DOWN*5+RIGHT*17)
        self.add(axes,graph,label)




        


        
