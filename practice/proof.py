from manim import *

class proof(Scene):
    def construct(self):
        words = MathTex(r"Hallo!", font_size=32, color=GREEN_B)
        self.add(words)
        self.wait(2)
        self.remove(words)
        self.play(Create(words))
        self.wait(2)
        self.remove(words)
        self.play(Write(words))
        self.wait(2)

class move(Scene):
    def construct(self):

        line_points1 = NumberLine(
            x_range = [0,2, 0.5], length = 5, include_numbers = True).shift(DOWN*2
        )

        dot_sequence2 = Dot(point=line_points1.n2p(1.5), color=BLUE)

        dot1 = Dot(point=line_points1.n2p(2), color=BLUE)
        
        self.play(Create(dot1), Flash(dot1))
        l1 = Line(dot1, dot_sequence2.get_center()).set_color(PURPLE)
        l2 = VMobject()
        self.add(dot1,l1,l2, line_points1)
        l2.add_updater(lambda x:x.become(Line(dot_sequence2, dot1).set_color(PURPLE)))
        self.play(MoveAlongPath(dot1,l1), rate_func=linear)
        self.wait(5)


class Movealong(Scene):
    def construct(self):

        d1 = Dot().set_color(ORANGE)
        l1 = Line(RIGHT, LEFT)
        l2 = VMobject()
        self.add(d1, l1, l2)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(d1, l1), rate_func=linear)
        self.wait(3)

class more(Scene):
    def construct(self):

        line_points1 = NumberLine(
            x_range = [0,2], length = 10, include_numbers = True).shift(DOWN*2
        )

        dot_2 = Dot(point=line_points1.n2p(1.5), color=BLUE)
        dot_1 = Dot(point=line_points1.n2p(2), color=BLUE)
        line2 = Line(dot_1, dot_2)
        self.add(line2)
        self.wait(2)
        self.remove(line2)
        line3 = Line(dot_2, dot_1)
        self.add(line3)
        self.wait(2)

class tryone(Scene):
    def construct(self):

        convergence_interval = NumberLine(x_range=[0,2, 0.09], length = 13)

        convergence_interval_2 = NumberLine(x_range=[0,2,.5], length = 13) # New number line for smaller epsilon

        convergence_interval = NumberLine(x_range=[0,2, 0.09], length = 13)




        a_minus_3 =  MathTex(r"1-0.005", font_size=30, color=RED).shift(LEFT*3, DOWN*1.5, UP)
        dot_leftextreme_3 = Dot(point=convergence_interval.n2p(1.005), color=RED)
        a_plus_3 =  MathTex(r"1+0.005", font_size=30, color=RED).shift(RIGHT*3, DOWN*1.5, UP)
        dot_rightextreme_3 = Dot(point=convergence_interval.n2p(0.995), color=RED)

        self.add(convergence_interval_2, dot_leftextreme_3, dot_rightextreme_3)
        self.wait(4)


class move_function(Scene):
    def construct(self):

        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False}, x_axis_config={"numbers_to_include": np.arange(0,10)}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)

        def func(x):
            return 3*(x-2) ** 2
        graph = ax.plot(func, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()

        self.add(ax, labels, graph, dot)
        self.play(t.animate.set_value(x_space[minimum_index]))
        self.wait()

class function(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False}, x_axis_config={"numbers_to_include": np.arange(0,10)}
        )

        x_space_1 = np.linspace(*ax.x_range[:1],100)
        x_space_2 = np.linspace(*ax.x_range[:3],200)
        print(x_space_2)
        #minimum_index = func(x_space).argmin()


class alternative(Scene):
    def construct(self):
        ax = Axes(x_range=[-1, 10], y_range=[-1, ])
        graph = ax.plot(lambda x: x**2, color=BLUE, x_range=[0, 10])
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        moving_dot.add_updater(lambda x: x.move_to(moving_dot.get_center()))
        
        #def update_curve(mob):
        #    mob.move_to(moving_dot.get_center())

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))


class para_plane(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_length=10, y_length=10, z_length=5)
        problem1_surface = Surface(lambda u,v: axes.c2p(u, v, 6 - 2*u - 2*v), v_range=[0,3], u_range=[0,3]).set_fill_by_checkerboard(RED, ORANGE)
        cartesian1 = Surface(lambda u,v: np.array([u, v, 0]), u_range=[-10,10], v_range=[-10,10], fill_opacity=1).set_fill_by_checkerboard(BLACK, BLACK)
        cartesian2 = Surface(lambda u,v: np.array([0, v, u]), u_range=[-10,10],
         v_range=[-10,10], fill_opacity=0.1).set_fill_by_checkerboard(GRAY, GREEN)
        cartesian3 = Surface(lambda u,v: np.array([u, 0, v]), u_range=[-10,10], v_range=[-10,10], fill_opacity=0.1).set_fill_by_checkerboard(GRAY, PURPLE)
        self.set_camera_orientation(phi=80 * DEGREES, theta=30 * DEGREES, zoom=0.9)
        self.add(problem1_surface,axes, cartesian1)
        #self.add(cartesian1, axes)
        #self.add(cartesian2)
        #self.add(cartesian3)
        self.wait(5)