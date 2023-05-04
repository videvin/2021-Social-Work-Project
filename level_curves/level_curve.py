
from manim import *

class level_curve(ThreeDScene):
    def construct(self):

        graph_surface = Surface(lambda u,v: np.array([u,v,v**2-u**2]), u_range=[-5,5], v_range=[-7,7])

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

        negative_curvec4_1 = ParametricFunction(
            lambda u: np.array([
                -4*np.cosh(u),
                4*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        negative_curvec4_2 = ParametricFunction(
            lambda u: np.array([
                4*np.cosh(u),
                -4*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        negative_curvec6_1 = ParametricFunction(
            lambda u: np.array([
                -6*np.cosh(u),
                6*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        negative_curvec6_2 = ParametricFunction(
            lambda u: np.array([
                6*np.cosh(u),
                -6*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        negative_curvec8_1 = ParametricFunction(
            lambda u: np.array([
                -8*np.cosh(u),
                8*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        negative_curvec8_2 = ParametricFunction(
            lambda u: np.array([
                8*np.cosh(u),
                -8*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        negative_curvec10_1 = ParametricFunction(
            lambda u: np.array([
                -10*np.cosh(u),
                10*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        negative_curvec10_2 = ParametricFunction(
            lambda u: np.array([
                10*np.cosh(u),
                -10*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        negative_curvec12_1 = ParametricFunction(
            lambda u: np.array([
                -12*np.cosh(u),
                12*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        negative_curvec12_2 = ParametricFunction(
            lambda u: np.array([
                12*np.cosh(u),
                -12*np.sinh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )


        # Vertical

        positive_curvec2_1 = ParametricFunction(
            lambda u: np.array([
                -2*np.sinh(u),
                2*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        positive_curvec2_2 = ParametricFunction(
            lambda u: np.array([
                2*np.sinh(u),
                -2*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        positive_curvec4_1 = ParametricFunction(
            lambda u: np.array([
                -4*np.sinh(u),
                4*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        positive_curvec4_2 = ParametricFunction(
            lambda u: np.array([
                4*np.sinh(u),
                -4*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        positive_curvec6_1 = ParametricFunction(
            lambda u: np.array([
                -6*np.sinh(u),
                6*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        positive_curvec6_2 = ParametricFunction(
            lambda u: np.array([
                6*np.sinh(u),
                -6*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        positive_curvec8_1 = ParametricFunction(
            lambda u: np.array([
                -8*np.sinh(u),
                8*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        positive_curvec8_2 = ParametricFunction(
            lambda u: np.array([
                8*np.sinh(u),
                -8*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        positive_curvec10_1 = ParametricFunction(
            lambda u: np.array([
                -10*np.sinh(u),
                10*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        positive_curvec10_2 = ParametricFunction(
            lambda u: np.array([
                10*np.sinh(u),
                -10*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        positive_curvec12_1 = ParametricFunction(
            lambda u: np.array([
                -12*np.sinh(u),
                12*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )
        positive_curvec12_2 = ParametricFunction(
            lambda u: np.array([
                12*np.sinh(u),
                -12*np.cosh(u),
                0
            ]), color=RED, t_range = np.array([-2*PI, 2*PI])
        )

        line_1 = ParametricFunction(
            lambda u: np.array([
                u,
                u,
                0
            ]), color=GREEN, t_range = np.array([-10, 10])
        )
        line_2 = ParametricFunction(
            lambda u: np.array([
                u,
                -u,
                0
            ]), color=GREEN, t_range = np.array([-10, 10])
        )

        axes = ThreeDAxes(x_range=[-10,10], y_range=[-10,10], x_length=30, y_length=30, z_length=30)
        self.set_camera_orientation(phi=80 * DEGREES, theta=30 * DEGREES, zoom=0.5)

        text1 = Text("What surface generates these curves in xy-plane?", font_size=30).shift(UP*3.5)
        title = Tex(r"Level Curves", font_size=35).shift(UP*3.8)
        text2 = Text("The more they get together, the larger the value of z is", font_size=30).shift(UP*3.8)


        self.play(GrowFromCenter(axes))
        self.add_fixed_in_frame_mobjects(title)
        self.play(Create(title))
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Create(text1))


        self.begin_ambient_camera_rotation(0.2)
        self.play(Create(negative_curvec2_1))
        self.play(Create(negative_curvec2_2))
        self.wait()
        self.play(Create(negative_curvec4_1))
        self.play(Create(negative_curvec4_2))
        self.wait()
        self.play(Create(negative_curvec6_1))
        self.play(Create(negative_curvec6_2))
        self.wait() 
        self.play(Create(negative_curvec8_1))
        self.play(Create(negative_curvec8_2))
        self.wait()
        self.play(Create(negative_curvec10_1)) 
        self.play(Create(negative_curvec10_2))
        self.wait()
        self.play(Create(negative_curvec12_1))
        self.play(Create(negative_curvec12_2))

        self.wait(3)

        self.play(Unwrite(title), Unwrite(text1))
        self.wait()
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Create(text2))

        self.play(Create(positive_curvec2_1))
        self.play(Create(positive_curvec2_2))
        self.wait() 
        self.play(Create(positive_curvec4_1))
        self.play(Create(positive_curvec4_2))
        self.wait()
        self.play(Create(positive_curvec6_1))
        self.play(Create(positive_curvec6_2))
        self.wait()
        self.play(Create(positive_curvec8_1))
        self.play(Create(positive_curvec8_2))
        self.wait()
        self.play(Create(positive_curvec10_1))
        self.play(Create(positive_curvec10_2))
        self.wait()
        self.play(Create(positive_curvec12_1))
        self.play(Create(positive_curvec12_2))

        self.wait(3)

        self.play(Create(line_1), Create(line_2))

        self.wait(2)

        self.play(DrawBorderThenFill(graph_surface))

        self.wait(5)

        positive_curvec2_1_surface = ParametricFunction(
            lambda u: np.array([
                -2*np.sinh(u),
                2*np.cosh(u),
                2
            ]), color=PURPLE, t_range = np.array([-2*PI, 2*PI])
        )
        positive_curvec2_2_surface = ParametricFunction(
            lambda u: np.array([
                2*np.sinh(u),
                -2*np.cosh(u),
                2
            ]), color=PURPLE, t_range = np.array([-2*PI, 2*PI])
        )

        negative_curvec2_1_surface = ParametricFunction(
            lambda u: np.array([
                -2*np.cosh(u),
                2*np.sinh(u),
                2
            ]), color=PURPLE, t_range = np.array([-2*PI, 2*PI])
        )
        negative_curvec2_2_surface = ParametricFunction(
            lambda u: np.array([
                2*np.cosh(u),
                -2*np.sinh(u),
                2
            ]), color=PURPLE, t_range = np.array([-2*PI, 2*PI])
        )

        self.play(Transform(positive_curvec2_1, positive_curvec2_1_surface))
        self.play(Transform(positive_curvec2_2, positive_curvec2_2_surface))
        self.play(Transform(negative_curvec2_1, negative_curvec2_1_surface))
        self.play(Transform(negative_curvec2_2, negative_curvec2_2_surface))
        self.wait(5)
        self.stop_ambient_camera_rotation()