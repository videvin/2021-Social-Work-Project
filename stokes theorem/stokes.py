from re import X
from tkinter import Y
from manim import *

class stokes(ThreeDScene):

    def construct(self):

        title = Tex(r"Stoke's Theorem", font_size=40).shift(UP*3.8)
        text1 = Text("How do we find the surface area?", font_size=28).shift(UP*3.3)
        axes = ThreeDAxes(x_length=10, y_length=10, z_length=10)
        problem1_surface = Surface(lambda u,v: axes.c2p(u, v, 6 - 2*u - 2*v), v_range=[0,3], u_range=[0,3]).set_fill_by_checkerboard(RED, ORANGE)
        cartesian1 = Surface(lambda u,v: np.array([u, v, 0]), u_range=[-10,10], v_range=[-10,10], fill_opacity=1).set_fill_by_checkerboard(BLACK, PURPLE)
        self.set_camera_orientation(phi=80 * DEGREES, theta=30 * DEGREES)

        # Introduction

        self.play(GrowFromCenter(axes))
        self.add_fixed_in_frame_mobjects(title)
        self.play(Create(title))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Create(text1))
        self.wait()
        self.play(DrawBorderThenFill(problem1_surface), DrawBorderThenFill(cartesian1))
        self.wait(2)
        self.begin_ambient_camera_rotation(0.3)

        # Line Integrals

        Curve1 = Tex(r"$C_1: r_{1}(t) = (3-t) \textbf{i} + t \textbf{j} \text{ , } 0 \leq t \leq 3$", font_size=27)
        Curve2 = Tex(r"$C_2: r_{2}(t) = (6-t) \textbf{j} + (2t-6) \textbf{k} \text{ , } 3 \leq t \leq 6$", font_size=27)
        Curve3 = Tex(r"$C_3: r_{3}(t) = (t-6) \textbf{i} + (18-2t) \textbf{k} \text{ , } 6 \leq t \leq 9$", font_size=27)
        curve_group = VGroup(Curve1,Curve2,Curve3).arrange(DOWN)
        curve_group.shift(2*DOWN)

        self.play(Unwrite(text1), Unwrite(title))
        text2 = Text("We find a parametrization of the curve", font_size=30).shift(UP*3.8)
        self.add_fixed_in_frame_mobjects(text2,curve_group)
        self.play(Create(text2))
        self.add_fixed_in_frame_mobjects(curve_group)
        self.play(Create(curve_group))
        self.wait(2)

        text3 = Text("Our calculation is given by: ", font_size=30).shift(3.8*UP)
        text4 = Text("A simpler way", font_size=30).shift(DOWN*2)
        Calculation_line_integrals = MathTex(r"\int_{c}F \cdot d \textbf{r} &= \int_{c_1}F \cdot r_{1}^{'}(t)dt + \int_{c_2}F \cdot r_{2}^{'}(t)dt + \int_{c_3}F \cdot r_{3}^{'}(t)dt \\ &= \int_{s} \int (\text{curl} \textbf{ F}) \cdot \textbf{N} \textit{d}S", font_size=25).shift(2*DOWN)

        self.play(Uncreate(text2), Uncreate(curve_group))
        self.add_fixed_in_frame_mobjects(text3, Calculation_line_integrals)
        self.play(Create(text3), Create(Calculation_line_integrals))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(text4)
        self.play(Create(text4))
        self.play(Unwrite(text3), Unwrite(Calculation_line_integrals), Unwrite(text4))

        # The general outlook

        text5 = Text("A general way is highlited by Stoke's Theorem", font_size=30).shift(UP*3.7)
        text6 = Text("We consider a general surface", font_size=30).shift(UP*3.4)

        self.add_fixed_in_frame_mobjects(text5)
        self.play(Write(text5))
        self.wait(2)
        self.play(Unwrite(text5))
        self.add_fixed_in_frame_mobjects(text6)
        self.play(Create(text6))
        self.wait(2)

        definition = MathTex(r"\int_{c}F \cdot d \textbf{r} = \int_{s} \int (\text{curl} \textbf{ F}) \cdot \textbf{N} \textit{d}S", font_size=25).shift(DOWN*2)

        general_curve = Surface(lambda u,v: np.array([np.cos(u)*np.sin(v) + 2, 2*np.sin(u)*np.sin(v) + 3, 1.5*np.cos(v) + 1]), v_range=[0,PI/2], u_range=[0,2*PI])

        general_curve_2d = ParametricFunction(lambda u: np.array([np.cos(u) + 2,2*np.sin(u) + 3, 0]), color=RED, t_range = np.array([0, 2*PI]))

        text7 = Text("A piecewise smooth simple closed curve along we integrate", font_size=25).shift(UP*3.5)
        text8 = Text("An oriented surface with a countour given by the curve we are integrating on", font_size=25).shift(UP*3.2)

        self.play(Unwrite(text6), Unwrite(problem1_surface))
        self.play(DrawBorderThenFill(general_curve))
        self.wait()
        self.play(Create(general_curve_2d))
        self.wait()
        self.add_fixed_in_frame_mobjects(definition)
        self.play(Create(definition))
        self.wait()
        self.add_fixed_in_frame_mobjects(text7)
        self.play(Create(text7))
        self.wait(2)
        self.play(Unwrite(text7))
        self.add_fixed_in_frame_mobjects(text8)
        self.play(Create(text8))
        self.wait(5)

        self.stop_ambient_camera_rotation()
        self.wait(2)

