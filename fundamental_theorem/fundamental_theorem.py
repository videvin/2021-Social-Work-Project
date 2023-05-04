from tkinter import Y
from manim import *
from matplotlib.pyplot import axes

class fundamental_theorem(Scene):
    def construct(self):

        axes_1 = Axes(y_range=[0,10], x_range=[0,5], tips=False)

        function_1 = axes_1.plot(lambda x:1/x, x_range=[0.1,5], color=PURPLE)

        area_1 = axes_1.get_riemann_rectangles(function_1, x_range=[0,2], dx=0.05, color=BLUE_B)

        self.play(GrowFromCenter(axes_1))
        self.wait()
        self.play(Create(function_1, lag_ratio=0.3))
        self.wait()
        self.play(Create(area_1, lag_ratio=0.2))

        Group_1 = VGroup(area_1, function_1, axes_1)

        self.play(Group_1.animate.shift(LEFT*3))

        axes_2 = Axes(y_range=[-4,5], x_range=[0,10], tips=False).shift(RIGHT*3, UP)

        self.wait()

        self.play(GrowFromCenter(axes_2))

        function_2 = axes_2.plot(lambda x:np.log(x), x_range=[0.1,10], color=PURPLE)

        self.play(Create(function_2, lag_ratio=0.3))

        self.wait(2)
