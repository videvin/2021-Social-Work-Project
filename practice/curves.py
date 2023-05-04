from cmath import cosh
from manim import *

class horizontal_hyperbola(Scene):
    def func_1(self,t):
        return np.array((-np.cosh(t), np.sinh(t), 0))
    def func_2(self,t):
        return np.array((np.cosh(t), -np.sinh(t), 0))
    def construct(self):
        func_1 = ParametricFunction(self.func_1, t_range=np.array([-2*PI,2*PI]))
        func_2 = ParametricFunction(self.func_2, t_range=np.array([-2*PI,2*PI]))
        self.add(func_1, func_2)

class vertical_hyperbola(Scene):
    def func_1(self,t):
        return np.array((-np.sinh(t), np.cosh(t), 0))
    def func_2(self,t):
        return np.array((np.sinh(t), -np.cosh(t), 0))
    def construct(self):
        func_1 = ParametricFunction(self.func_1, t_range=np.array([-2*PI,2*PI]))
        func_2 = ParametricFunction(self.func_2, t_range=np.array([-2*PI,2*PI]))
        self.add(func_1, func_2)

class horizontal_hyperbola_3d(ThreeDScene):
    def func_1(self,t):
        return np.array((-np.cosh(t), np.sinh(t), 0))
    def func_2(self,t):
        return np.array((np.cosh(t), -np.sinh(t), 0))
    def construct(self):
        ax = ThreeDAxes
        func_1 = ParametricFunction(self.func_1, t_range=np.array([-2*PI,2*PI]))
        func_2 = ParametricFunction(self.func_2, t_range=np.array([-2*PI,2*PI]))
        self.add(func_1, func_2,ax)

class example(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: np.array([
                np.cosh(u),
                np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        curve2 = ParametricFunction(
            lambda u: np.array([
                -np.cosh(u),
                np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        axes = ThreeDAxes()
        self.add(axes, curve1, curve2)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait(2)