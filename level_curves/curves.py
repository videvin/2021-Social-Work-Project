from manim import *

class curve(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[-10,10], y_range=[-10,10], x_length=30, y_length=30, z_length=30)
        self.set_camera_orientation(phi=80 * DEGREES, theta=30 * DEGREES, zoom=0.5)

        negative_curvec2_1 = ParametricFunction(
            lambda u: np.array([
                -2*np.cosh(u),
                2*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        negative_curvec2_2 = ParametricFunction(
            lambda u: np.array([
                2*np.cosh(u),
                -2*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        negative_curvec2_1_copy = np.array(negative_curvec2_1, copy=True)
        negative_curvec2_1_copy.shift(2*LEFT)

        self.add(axes, negative_curvec2_1_copy)
        self.wait(10)