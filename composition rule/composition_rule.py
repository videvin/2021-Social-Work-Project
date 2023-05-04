from re import S
from manim import *
from matplotlib.pyplot import axis
from numpy import dot

class another_function(Scene):
    def construct(self):

        # First scene: f function

        f_definition = Tex(
            "Let $f(x) = x^2$ be a function defined on $(0,5)$", font_size=30).shift(UP*3.8
            )

        axis_f_original = Axes(
            x_range=[0,5], y_range=[0, 10], x_length = 6.5, y_length = 6.5,
             x_axis_config={"numbers_to_include":np.arange(0,5)},tips=False
            )

        graph1 = axis_f_original.plot(lambda x:x**2, color=RED, x_range=[0,3])

        moving_dot_1 = Dot(axis_f_original.i2gp(graph1.t_min, graph1), color=ORANGE)
        dot_1 = Dot(axis_f_original.i2gp(graph1.t_min, graph1))
        dot_2 = Dot(axis_f_original.i2gp(graph1.t_max, graph1))
        moving_dot_1.add_updater(lambda x: x.move_to(moving_dot_1.get_center()))
        

        question1 = Tex(
            "What happens if we take only pair numbers mutiplying by $2$ $x$ in $(0,5)$?",
         font_size=30).shift(UP*3.8
         )

        self.play(Create(f_definition))
        self.play(GrowFromCenter(axis_f_original))
        self.play(Create(graph1))
        self.add(moving_dot_1, dot_1, dot_2)
        self.play(MoveAlongPath(moving_dot_1, graph1), rate_func=linear)
        self.wait(2)
        self.play(Uncreate(f_definition))
        self.play(Create(question1))
        self.wait(2)
        self.play(Uncreate(question1), Uncreate(axis_f_original), Uncreate(graph1))
        self.remove(dot_1, dot_2, moving_dot_1)
        self.wait()

        #Scene 2: shifting to transformation

        axis_f_resize = Axes(
            x_range=[0,5], y_range=[0, 10], x_length = 4, y_length = 4,
             x_axis_config={"numbers_to_include":np.arange(0,5)},tips=False
            )
        graph1_resize = axis_f_resize.plot(lambda x:x**2, color=RED, x_range=[0,3])
        
        axis_fog = Axes(
            x_range=[0,10], y_range=[0, 10], x_length=4, y_length=4,
             x_axis_config={"numbers_to_include":np.arange(0,5)}, tips=False
        )
        graph2 = axis_fog.plot(lambda x: (2*x)**2, color=GREEN, x_range=[0,5])

        f = VGroup(axis_f_resize, graph1_resize).shift(LEFT*3.9)
        fog = VGroup(graph2, axis_fog).shift(RIGHT*3.9)

        self.play(GrowFromCenter(f), GrowFromCenter(fog))
        self.wait()

        values_3 = Tex("$f(2x) = 2^2$ if $x = 1$", font_size=28).shift(UP*3)
        dot_3 = Dot(axis_fog.i2gp(2.0, graph2))
        values_1 = Tex("$f(2x) = 1^2$ if $x = 1/2$", font_size=28).shift(UP)
        dot_1 = Dot(axis_fog.i2gp(1/2, graph2))
        values_2 = Tex("$f(2x) = (2 \sqrt(2))^2$ if $x = \sqrt(2)$", font_size=28).shift(UP*2)
        dot_2 = Dot(axis_fog.i2gp(np.sqrt(2), graph2))

        self.play(Write((values_1)))
        self.play(Create(dot_1), Flash(dot_1))
        self.wait(3)
        self.play(Write(values_2))
        self.play(Create(dot_2), Flash(dot_2))
        self.wait(3)
        self.play(Write(values_3))
        self.play(Create(dot_3), Flash(dot_3))
        self.wait(5)

        text6 = Tex("And then numbers like $1/3$ or $3/4$ don't belong to the domain of $f(2*x)$", font_size=30).shift(DOWN*3)
        text7 = Tex("$1/3$ is not an even number", font_size=30).shift(DOWN*3)
        text8 = Tex("The new domain is given by multiplying $x$ in $(0,5)$ by $2$", font_size=30).shift(DOWN*3)

        self.play(Create(text6))
        self.wait(3)
        self.play(Unwrite(text6))
        self.play(Create(text7))
        self.wait(3)
        self.play(Uncreate(text7))
        self.play(Create(text8))
        self.wait(3)
        self.play(Uncreate(text8))
        
        text9 = Tex("Lets think differently and define g(x) = 2x", font_size=30).shift(DOWN*3.2)

        axes_3 = Axes(x_range=[0,5], y_range=[0, 10], x_length = 5, y_length = 5, x_axis_config={"numbers_to_include":np.arange(0,5)}, tips=False).shift(LEFT*3.9)
        graph3 = axes_3.plot(lambda x: 2*x, color=BLUE, x_range=[0,5])
        text10 = Tex("We rethink $f(2*x)$ as $f(g(x))$ where $f$ takes $2*x$'s values and $g$ takes $x$'s", font_size=30).shift(DOWN*3.2)

        self.play(Uncreate(f))
        self.remove(values_1, dot_1, values_2, dot_2, values_3, dot_3)
        self.play(Create(axes_3))
        self.play(Create(graph3))
        self.wait(3)
        self.play(Create(text9))
        self.wait(1)
        self.play(Unwrite(text9))
        self.play(Create(text10))
        self.wait(5)


class analytic_calculation(Scene):
    def construct(self):

        title = Tex(r"Analytic Viewpoint", font_size=35).shift(UP*3.5)
        text1 = Tex(r"Let's put the formula for these functions", font_size=30).shift(UP*3)
        formula = Tex(r"$ (f \cdot g)(x) = f(g(x))$", font_size=30).shift(UP*3)

        self.play(Create(title))
        self.wait()
        self.play(Create(text1))
        self.wait(2)
        self.play(Unwrite(text1))
        self.play(Create(formula))
        self.wait(2)
        self.play(Uncreate(title), Uncreate(formula))

        example1 = MathTex(r"h(x) &= 4x^2 \\ &= (2x)^2 \\ &= (f o g)(x)", font_size=28).shift(UP*2)
        example1_box = SurroundingRectangle(example1, color=BLUE, buff=SMALL_BUFF)
        g_example1 = MathTex(r"g(x) = 2x", font_size=28).shift(LEFT*3)
        f_example1 = MathTex(r"f(x) = x^2", font_size=28).shift(RIGHT*3)
        evaluation = Text("Lets evaluate for $x$ some values", font_size=30).shift(DOWN*2)

        self.play(Create(example1), Create(example1_box))
        self.play(Write(g_example1))
        self.play(Write(f_example1))
        self.wait(3)
        self.play(Create(evaluation))
        self.wait(2)
        self.play(Unwrite(example1), Unwrite(g_example1), Unwrite(f_example1), Unwrite(evaluation), Unwrite(example1_box))

        x_text1 = MathTex(r"x = 2 \Rightarrow f(g(2)) &= f(4) \\ &= (2*2)^2 \\ &= 4^2 \\ &= 16", font_size=28).shift(UP*2)
        x_text1_box = SurroundingRectangle(x_text1, color=BLUE, buff=SMALL_BUFF)
        evaluation1 = Tex(r"$f(g(2)) \Rightarrow f(4) \Rightarrow 16$", font_size=30).shift(DOWN)
        evaluation1_box = SurroundingRectangle(evaluation1, color=BLUE, buff=SMALL_BUFF)

        self.play(Create(x_text1))
        self.play(Create(x_text1_box))
        self.wait()
        self.play(Create(evaluation1))
        self.play(Create(evaluation1_box))
        self.wait(5)
        self.play(Unwrite(x_text1), Unwrite(evaluation1), Unwrite(x_text1_box), Unwrite(evaluation1_box))

        example2 = Tex(r"$(f o g)(x) = \sin{1/x}$", font_size=30).shift(UP*2.8)
        example2_box = SurroundingRectangle(example2, color=BLUE, buff=SMALL_BUFF)
        g_example2 = Tex(r"$g(x) = 1/x$", font_size=30).shift(LEFT*3)
        f_example2 = Tex(r"$f(x) = sin(x)$", font_size=30).shift(RIGHT*3)

        self.play(Create(example2), Create(example2_box))
        self.play(Write(g_example2))
        self.play(Write(f_example2))
        self.wait(3)
        self.play(Unwrite(example2), Unwrite(g_example2), Unwrite(f_example2), Unwrite(example2_box))

        x_text2 = MathTex(r"x = 1/\pi \Rightarrow f(g(1/\pi)) &= f(\pi) \\ &= \sin{\pi} \\ = 0", font_size=30).shift(UP*2)
        x_text2_box = SurroundingRectangle(x_text2, color=BLUE, buff=SMALL_BUFF)
        evaluation2 = Tex(r"$f(g(1/\pi)) \Rightarrow f(pi) \Rightarrow 0$", font_size=30).shift(DOWN)
        evaluation2_box = SurroundingRectangle(evaluation2, color=BLUE, buff=SMALL_BUFF)

        self.play(Create(x_text2))
        self.play(Create(x_text2_box))
        self.wait()
        self.play(Create(evaluation2))
        self.play(Create(evaluation2_box))
        self.wait(5)
        self.play(Unwrite(x_text2), Unwrite(evaluation2), Unwrite(x_text2_box), Unwrite(evaluation2_box))

        example3 = Tex(r"$(f o g)(x) = \frac{g(x) + 1}{g(x + 1)} = \frac{x^3 + 1}{(x+1)^3 + x^2}$", font_size=30).shift(UP*2.8)
        example3_box = SurroundingRectangle(example3, color=BLUE, buff=SMALL_BUFF)
        g_example3 = Tex(r"$g(x) = x^3$", font_size=30).shift(LEFT*3)
        f_example3 = Tex(r"$f(x) = \frac{x + 1}{x}$", font_size=30).shift(RIGHT*3)

        self.play(Create(example3), Create(example3_box))
        self.play(Write(g_example3))
        self.play(Write(f_example3))
        self.wait(3)
        self.play(Unwrite(example3), Unwrite(g_example3), Unwrite(f_example3), Unwrite(example3_box))

        x_text3 = MathTex(r"x = 3 \Rightarrow f(g(3)) &= f(27,64) \\ &= \frac{27 + 1}{64} \\ &= 7/16", font_size=30).shift(UP*2)
        x_text3_box = SurroundingRectangle(x_text3, color=BLUE, buff=SMALL_BUFF)
        evaluation3 = Tex(r"$f(g(3)) \Rightarrow f(27,64) \Rightarrow 7/16$", font_size=30).shift(DOWN)
        evaluation3_box = SurroundingRectangle(evaluation3, color=BLUE, buff=SMALL_BUFF)

        self.play(Create(x_text3))
        self.play(Create(x_text3_box))
        self.wait()
        self.play(Create(evaluation3))
        self.play(Create(evaluation3_box))
        self.wait(5)
        self.play(Unwrite(x_text3), Unwrite(evaluation3), Unwrite(x_text3_box), Unwrite(evaluation3_box))
        self.wait(5)

        
