from manim import *

class particular_sequence(Scene):
    def construct(self):
        line1 = NumberLine(
            x_range=[0,10], length = 10, include_numbers=True
        ).shift(UP*2)

        self.play(GrowFromCenter(line1))

        self.wait(1)

        line2 = NumberLine(
            x_range=[0,1,0.1], length = 10, include_numbers=True).shift(DOWN*2
        )

        function_text = MathTex(
            r"f(x) = \frac{1}{n^2}", font_size = 40
        ).shift(UP)

        self.play(FadeIn(function_text))

        function_text1 = MathTex(
            r"a_1(1) = \frac{1}{1^2} = 1}", font_size = 35
        )

        function_text2 = MathTex(
            r"a_2(2) = \frac{1}{2^2} = \frac{1}{4}", font_size = 35
        )

        function_text3 = MathTex(
            r"a_3(3) = \frac{1}{3^2} = \frac{1}{9}", font_size = 35
        )

        function_text4 = MathTex(
            r"a_4(4) = \frac{1}{4^2} = \frac{1}{16}", font_size = 35
        )

        examples = VGroup(  # It lays out the equations in descending order
            function_text1, function_text2, function_text3,
         function_text4).arrange(DOWN
        ) 

        examples.next_to(function_text, RIGHT)

        self.play(ReplacementTransform(line1,line2))
        self.play(ScaleInPlace(function_text, scale_factor=2))

        self.play(function_text.animate.shift(LEFT*2))

        self.play(Create(examples))

        dot1 = Dot(point=line2.n2p(1), color=RED)       # It takes the point from the number line
        dot2 = Dot(point=line2.n2p(0.25), color=RED)
        dot3 = Dot(point=line2.n2p(0.11), color=RED)
        dot4 = Dot(point=line2.n2p(0.06), color=RED)

        self.play(FadeToColor(dot1, color=RED))
        self.play(FadeToColor(dot2, color=RED))
        self.play(FadeToColor(dot3, color=RED))
        self.play(FadeToColor(dot4, color=RED))
        self.wait(4)


class distance_definition(Scene):
    def construct(self):

        text1 = Tex(r"These are all numbers in $(a,b)$", font_size=36).shift(UP*3)
        text1_box = SurroundingRectangle(text1, color=BLUE, buff=SMALL_BUFF)
        distance =  MathTex(r"|a-b|", font_size=40).shift(UP)
        a =  MathTex(r"a", font_size=15).shift(LEFT*5, UP*1.5, DOWN)
        b =  MathTex(r"b", font_size=15).shift(RIGHT*5, UP*1.5, DOWN)


        number_line1 = NumberLine(x_range=[0,1], length = 10)

        self.play(GrowFromCenter(number_line1))
        self.wait(0.5)
        self.play(ScaleInPlace(a, scale_factor=2))
        self.play(FadeToColor(a, color=RED))
        self.play(ScaleInPlace(b, scale_factor=2))
        self.play(FadeToColor(b, color=RED))
        self.wait(0.5)
        self.play(Create(distance), Create(text1), Create(text1_box))
        self.wait(2)
        self.play(FadeOut(distance),FadeOut(text1), FadeOut(text1_box))
        self.play(FadeOut(a), FadeOut(b))
        self.play(FadeOut(number_line1))
        self.wait()
        
        number_line2 = NumberLine(x_range=[0,1,0.5], length = 10)

        text2 = Tex(r"These are all numbers in $(a,b)$ less than a number $\epsilon$", font_size=36).shift(UP*3)
        text2_box = SurroundingRectangle(text2, color=BLUE, buff=SMALL_BUFF)

        a_minus =  MathTex(r"a-\epsilon", font_size=20).shift(LEFT*5, UP*1.5, DOWN)
        a_new =  MathTex(r"a", font_size=20).shift(UP)
        a_plus =  MathTex(r"a+\epsilon", font_size=20).shift(RIGHT*5, UP*1.5, DOWN)

        distance_epsilon = MathTex(r"|x-a| < \epsilon", font_size=35).shift(UP*2)

        text3 = Tex(r"Another way to see this", font_size=36).shift(UP*3)
        text4 = MathTex(r"a-\epsilon < a < a+\epsilon", font_size=36).shift(UP*3)
        text4_box = SurroundingRectangle(text4, color=BLUE, buff=SMALL_BUFF)

        self.play(FadeIn(number_line2))
        self.play(ScaleInPlace(a_new, scale_factor=2), ScaleInPlace(a_minus, scale_factor=2), ScaleInPlace(a_plus, scale_factor=2))
        self.play(Create(distance_epsilon), Create(text2), Create(text2_box))
        self.wait(2)
        self.play(FadeOut(distance_epsilon),FadeOut(text2), FadeOut(text2_box))
        self.play(Create(text3))
        self.wait()
        self.play(Unwrite(text3))
        self.play(Create(text4), Create(text4_box))
        self.wait()
        self.play(FadeOut(a_new), FadeOut(a_minus), FadeOut(a_plus))
        self.play(FadeOut(number_line2))
        self.wait(2)
        


class sequence_process(Scene):
    def construct(self):
        line_points1 = NumberLine(
            x_range = [0,2], length = 10, include_numbers = True).shift(DOWN*2
        )
        line_points2 = NumberLine(
            x_range = [0,2, 0.5], length = 10, include_numbers = True).shift(DOWN*2
        )
        line_points3 = NumberLine(
            x_range = [0,2, 0.5], length = 10, include_numbers = True).shift(DOWN*2
        )
        line_points4 = NumberLine(
            x_range = [0,2, 0.5], length = 10, include_numbers = True).shift(DOWN*2
        )
        line_points5 = NumberLine(
            x_range = [0,2, 0.5], length = 10, include_numbers = True).shift(DOWN*2
        )

        sequence_formula = MathTex(
            r"a_n(n) = \frac{n+1}{n} \rightarrow 1", font_size=33).shift(LEFT*5,UP*3
        )
        sequence_formula1 = MathTex(
            r"a_n(1) = \frac{1+1}{1} = 2", font_size=30).next_to(sequence_formula, DOWN).shift(RIGHT*(1/2))
        sequence_formula2 = MathTex(
            r"a_n(2) = \frac{2+1}{2} = 1.5", font_size=28).next_to(sequence_formula1, DOWN).shift(RIGHT*(1/2))
        sequence_formula3 = MathTex(
            r"a_n(5) = \frac{5+1}{5} = 1.25", font_size=26).next_to(sequence_formula2,DOWN).shift(RIGHT*(1/2))
        sequence_formula4 = MathTex(
            r"a_n(50) = \frac{50+1}{50} = 1.02", font_size=24).next_to(sequence_formula3,DOWN).shift(RIGHT*(1/2))
        sequence_formula5 = MathTex(
            r"a_n(100) = \frac{100+1}{100} = 1.01", font_size=22).next_to(sequence_formula4,DOWN).shift(RIGHT*(1/2))

        dot_sequence1 = Dot(point=line_points1.n2p(2), color=BLUE)
        dot_sequence2 = Dot(point=line_points1.n2p(1.5), color=BLUE)
        dot_sequence3 = Dot(point=line_points1.n2p(1.25), color=BLUE)
        dot_sequence4 = Dot(point=line_points1.n2p(1.02), color=BLUE)
        dot_sequence5 = Dot(point=line_points1.n2p(1.01), color=BLUE)

        limit = MathTex(r"a = 1", font_size=40, color=RED).shift(DOWN*3)

        self.play(GrowFromCenter(line_points1))
        self.wait(0.5)
        self.play(Create(sequence_formula, lag_ratio=0.5))
        self.wait(0.5)
        self.play(Create(sequence_formula1, lag_ratio=0.5))
        self.wait()
        self.play(FadeToColor(dot_sequence1, color=RED), Broadcast(limit, n_mobs=1, remover=False, final_opacity=1, run_time=2))
        self.wait(3)

        l1 = Line(dot_sequence1, dot_sequence2.get_center()).set_color(PURPLE)
        l2 = VMobject()
        l2.add_updater(lambda x:x.become(Line(dot_sequence1, dot_sequence1.get_center())))
        self.play(MoveAlongPath(dot_sequence1,l1), rate_func=linear)
        self.play(Create(sequence_formula2, lag_ratio=0.5))
        self.wait()

        self.play(FadeTransform(line_points1, line_points2))

        self.wait(0.5)
        self.play(FadeToColor(dot_sequence2, color=GREEN))
        self.wait(1)

        l3 = Line(dot_sequence2, dot_sequence3.get_center()).set_color(PURPLE)
        l4 = VMobject()
        l4.add_updater(lambda x:x.become(Line(dot_sequence2, dot_sequence2.get_center())))
        self.play(MoveAlongPath(dot_sequence2,l3), rate_func=linear)
        self.play(Create(sequence_formula3, lag_ratio=0.5))
        self.wait(1)

        self.play(FadeTransform(line_points2, line_points3))

        self.wait(0.5)
        self.play(FadeToColor(dot_sequence3, color=YELLOW))
        self.wait(1)

        l5 = Line(dot_sequence3, dot_sequence4.get_center()).set_color(PURPLE)
        l6 = VMobject()
        l6.add_updater(lambda x:x.become(Line(dot_sequence3, dot_sequence3.get_center())))
        self.play(MoveAlongPath(dot_sequence3,l5), rate_func=linear)
        self.play(Create(sequence_formula4, lag_ratio=0.5))
        self.wait(1)

        self.play(FadeTransform(line_points3,line_points4))

        self.wait(0.5)
        self.play(FadeToColor(dot_sequence4, color=BLUE))
        self.wait(1)

        l7 = Line(dot_sequence4, dot_sequence5.get_center()).set_color(PURPLE)
        l8 = VMobject()
        l8.add_updater(lambda x:x.become(Line(dot_sequence4, dot_sequence4.get_center())))
        self.play(MoveAlongPath(dot_sequence4,l7), rate_func=linear)
        self.play(Create(sequence_formula5, lag_ratio=0.5))
        self.wait(1)

        self.play(FadeTransform(line_points4, line_points5))
        self.wait(0.5)
        self.play(FadeToColor(dot_sequence5, color=PURPLE))
        self.wait(1)



class formal_definition(Scene):
    def construct(self):
        informal_def = Tex(
            r"$a_n = \frac{n+1}{n}$ approaches the number $1$ as $x$ gets larger and larger",
             font_size = 30).shift(UP*2.5)
        text1 = Tex("Values approaches no matter how small these numbers can be", font_size=28).shift(UP*2.5)
        text2 = Tex("We want the numbers inside the distance $|a_n - 1| < b$", font_size=28).shift(UP*2)
        
        convergence_interval = NumberLine(x_range=[0,2, 0.09], length = 13)

        l_limit_general = MathTex(r"limit", font_size=30, color=RED_B).move_to(UP*0.5)

        self.play(GrowFromCenter(convergence_interval))
        self.play(Create(informal_def))
        self.play(Write(l_limit_general))
        self.wait(2)
        self.play(Unwrite(informal_def))
        self.play(Write(text1))
        self.wait(2)
        self.play(Unwrite(text1))
        self.play(Create(text2))
        self.wait(2)
        self.play(Unwrite(text2))
        self.play(Unwrite(l_limit_general))
        self.wait(1)

         # Points for convergence_interval

        dot_text1 = MathTex(r"\frac{2}{\Downarrow}", color=WHITE, font_size=28).shift(RIGHT*6.5, UP)
        dot_sequence1 = Dot(point=convergence_interval.n2p(2), color=BLUE)

        dot_text2 = MathTex(r"\frac{1.5}{\Downarrow}", color=WHITE, font_size=28).shift(RIGHT*3.2, UP)
        dot_sequence2 = Dot(point=convergence_interval.n2p(1.5), color=BLUE)

        dot_text3 = MathTex(r"\frac{1.25}{\Downarrow}", color=WHITE, font_size=28).shift(RIGHT*1.6, UP)
        dot_sequence3 = Dot(point=convergence_interval.n2p(1.25), color=BLUE)

        dot_text4 = MathTex(r"\frac{\Uparrow}{1.02}", color=WHITE, font_size=28).shift(RIGHT*.1, DOWN)
        dot_sequence4 = Dot(point=convergence_interval.n2p(1.02), color=BLUE)

        dot_text5 = MathTex(r"\frac{}{1.01}", color=WHITE, font_size=28).shift(RIGHT*.1, DOWN*1.5)
        dot_sequence5 = Dot(point=convergence_interval.n2p(1.01), color=BLUE)

        l_limit = MathTex(r"1", font_size=30, color=RED).move_to(UP*0.5)


        # First epsilon = 8/5 = 0.6

        text3 = Tex(r"In this case $b = 8/5 = 0.6$", font_size=30).shift(UP*2.5)

        text_number1 = Tex(r"Number $2$ is left out", font_size=28).next_to(text3, DOWN*2)

        l_minus_1 =  MathTex(r"1-0.6", font_size=30, color=RED).shift(LEFT*3.8, DOWN*1.5, UP)
        dot_leftextreme_1 = Dot(point=convergence_interval.n2p(0.4), color=RED)

        l_plus_1 =  MathTex(r"1+0.6", font_size=30, color=RED).shift(RIGHT*3.8, DOWN*1.5, UP)
        dot_rightextreme_1 = Dot(point=convergence_interval.n2p(1.6), color=RED)

        self.play(Create(text3), GrowFromCenter(convergence_interval))
        self.play(Create(dot_leftextreme_1), Flash(dot_leftextreme_1))
        self.play(Create(dot_rightextreme_1), Flash(dot_rightextreme_1))
        self.play(Create(l_minus_1), Create(l_plus_1), Create(l_limit))
        self.wait(1)

        l1 = Line(dot_sequence1, dot_sequence2.get_center()).set_color(PURPLE)
        l2 = VMobject()
        l2.add_updater(lambda x:x.become(Line(dot_sequence1, dot_sequence1.get_center())))
        self.play(MoveAlongPath(dot_sequence1,l1), rate_func=linear)
        self.play(GrowFromCenter(dot_text1))
        self.play(Create(dot_sequence1), Flash(dot_sequence1))
        self.wait(1)
        self.play(FadeToColor(dot_sequence2, color=GREEN))
        self.wait(1)

        l3 = Line(dot_sequence2, dot_sequence3.get_center()).set_color(PURPLE)
        l4 = VMobject()
        l4.add_updater(lambda x:x.become(Line(dot_sequence2, dot_sequence2.get_center())))
        self.play(MoveAlongPath(dot_sequence2,l3), rate_func=linear)
        self.play(GrowFromCenter(dot_text2))
        self.wait(1)
        self.play(FadeToColor(dot_sequence3, color=GREEN))
        self.wait(1)

        l5 = Line(dot_sequence3, dot_sequence4.get_center()).set_color(PURPLE)
        l6 = VMobject()
        l6.add_updater(lambda x:x.become(Line(dot_sequence3, dot_sequence3.get_center())))
        self.play(MoveAlongPath(dot_sequence3,l5), rate_func=linear)
        self.play(GrowFromCenter(dot_text3))
        self.wait(1)
        self.play(FadeToColor(dot_sequence4, color=GREEN))
        self.wait(1)

        l7 = Line(dot_sequence4, dot_sequence5.get_center()).set_color(PURPLE)
        l8 = VMobject()
        l8.add_updater(lambda x:x.become(Line(dot_sequence4, dot_sequence4.get_center())))
        self.play(MoveAlongPath(dot_sequence4,l7), rate_func=linear)
        self.play(GrowFromCenter(dot_text4))
        self.play(GrowFromCenter(dot_text5))
        self.wait(1)
        self.play(FadeToColor(dot_sequence5, color=GREEN))
        self.wait(1)

        self.play(FadeOut(text3))
        self.play(Create(text_number1))
        self.wait(2)
        self.play(FadeOut(text3), FadeOut(l_minus_1), FadeOut(l_plus_1), FadeOut(text_number1), FadeOut(dot_leftextreme_1), FadeOut(dot_rightextreme_1))
        self.wait(1)


        # Second epsilon = 1/3 = 0.33


        text4 = Tex(r"Lets check out with $b = 1/3 = 0.3$", font_size=30).shift(UP*2.5)

        text_number2 = Tex(r"Numbers $1.5$ and $2$ are now excluded", font_size=28).shift(UP*2)

        l_minus_2 =  MathTex(r"1-0.3", font_size=30, color=RED).shift(LEFT*1.9, DOWN*1.5, UP)
        dot_leftextreme_2 = Dot(point=convergence_interval.n2p(0.7), color=RED)
        l_plus_2 =  MathTex(r"1+0.3", font_size=30, color=RED).shift(RIGHT*1.9, DOWN*1.5, UP)
        dot_rightextreme_2 = Dot(point=convergence_interval.n2p(1.3), color=RED)

        self.play(Create(text4)) 
        self.play(Create(l_minus_2))
        self.play(Create(l_plus_2))
        self.play(Create(dot_leftextreme_2), Flash(dot_leftextreme_2))
        self.play(Create(dot_rightextreme_2), Flash(dot_rightextreme_2))
        self.wait(1)
        self.play(Create(text_number2))
        self.wait(1)
        self.play(FadeOut(dot_leftextreme_1), FadeOut(dot_rightextreme_1), FadeOut(dot_sequence1), FadeOut(dot_sequence2),
         FadeOut(dot_sequence3), FadeOut(dot_sequence4), FadeOut(dot_sequence5))
        self.remove(l1,l2,l3,l4,l5,l6,l7,l8)
        self.play(FadeOut(dot_text1), FadeOut(dot_text2), FadeOut(dot_text3), FadeOut(dot_text4), FadeOut(dot_text5))
        convergence_interval_2 = NumberLine(x_range=[0,2,.5], length = 13) # New number line for smaller epsilon
        self.play(FadeTransform(convergence_interval, convergence_interval_2))
        self.play(Unwrite(text4), Unwrite(l_minus_2), Unwrite(l_plus_2))
        self.remove(dot_leftextreme_2, dot_rightextreme_2, text_number2)
        self.wait(1)


        # Points updated to convergence_interval_2

        
        dot_text4_new = MathTex(r"\frac{1.02}{\Downarrow}", color=WHITE, font_size=28).shift(RIGHT*4.5, UP*1.5, DOWN)
        dot_sequence4_new = Dot(point=convergence_interval_2.n2p(1.7), color=BLUE)
        dot_text5_new = MathTex(r"\frac{1.01}{\Downarrow}", color=WHITE, font_size=28).shift(RIGHT*2, UP*1.5, DOWN) 
        dot_sequence5_new = Dot(point=convergence_interval_2.n2p(1.30), color=BLUE)
        dot_text6_new = MathTex(r"\frac{\Uparrow}{1.001}", color=WHITE, font_size=28).shift(np.array([.3,0,0]), DOWN*1.5, UP)
        dot_sequence6_new = Dot(point=convergence_interval_2.n2p(1.05), color=BLUE)

        # Third epsilon = 5/100 = 0.005

        text7 = Tex(r"Finally, for $b = 5/100 = 0.005$", font_size=30).shift(UP*2.5)

        text_number3 = Tex(r"This time, the number $1.02$ is out", font_size=28).shift(UP*2.5)

        text8 = Tex(r"We add the term $a_{(1000)} = 1.001$", font_size=30).shift(UP*2)

        a_minus_3 =  MathTex(r"1-0.005", font_size=30, color=RED).shift(LEFT*3, DOWN*1.5, UP)
        dot_leftextreme_3 = Dot(point=convergence_interval.n2p(0.5), color=RED)
        a_plus_3 =  MathTex(r"1+0.005", font_size=30, color=RED).shift(RIGHT*3, DOWN*1.5, UP)
        dot_rightextreme_3 = Dot(point=convergence_interval.n2p(1.5), color=RED)

        self.play(GrowFromCenter(convergence_interval_2))
        self.play(Create(text7))
        self.play(Create(dot_leftextreme_3), Flash(dot_leftextreme_3))
        self.play(Create(dot_rightextreme_3), Flash(dot_rightextreme_3))
        self.play(Create(a_minus_3), Create(a_plus_3))


        self.add(dot_sequence4_new, dot_sequence5_new, dot_sequence6_new)

        l1 = Line(dot_sequence4_new, dot_sequence5_new.get_center()).set_color(PURPLE)
        l2 = VMobject()
        l2.add_updater(lambda x:x.become(Line(dot_sequence4_new, dot_sequence4_new.get_center())))
        self.play(MoveAlongPath(dot_sequence4_new,l1), rate_func=linear)
        self.play(GrowFromCenter(dot_text4_new))
        self.play(Create(dot_sequence4_new), Flash(dot_sequence4_new))
        self.wait(1)
        self.play(FadeToColor(dot_sequence4_new, color=GREEN))
        self.wait(1)

        l3 = Line(dot_sequence5_new, dot_sequence6_new.get_center()).set_color(PURPLE)
        l4 = VMobject()
        l4.add_updater(lambda x:x.become(Line(dot_sequence5_new, dot_sequence5_new.get_center())))
        self.play(MoveAlongPath(dot_sequence5_new,l1), rate_func=linear)
        self.play(GrowFromCenter(dot_text5_new))
        self.wait(1)
        self.play(FadeToColor(dot_sequence5_new, color=GREEN))
        self.play(GrowFromCenter(dot_text6_new))
        self.wait(1)
        self.play(Unwrite(text7))
        self.play(Create(text_number3))
        self.play(Create(text8))
        self.wait(1)
        self.play(Uncreate(text_number3))
        self.play(Uncreate(text8))
        self.wait(1)

        # Our formal definition


        text9 = Tex(r"We may repeat this process without an end changing $b$ every time", font_size=30).shift(UP*2.5)
        text10 = Tex(r"For any set surrounding the limit, we can find numbers of the sequence at some point", font_size=28).shift(UP*2)
        text11 = Tex(r"Lets call this number $\epsilon$ and express mathematically the idea", font_size=30).shift(UP*2.5)

        text13 = Tex(r"We say $l$ is the limit of $a_n$ for any $\epsilon >0$ if we can find a term for which $a_N$ is in $(l- \epsilon, l + \epsilon)$", font_size=30).shift(UP*2.5)
        text14 = Tex(r"Equivalently, $l$ is the limit of $a_n$ if for any $\epsilon >0$, there is an N such that if $n \geq N$, then $|a_n-l| < \epsilon$", font_size=30).shift(UP*2.5)

        self.play(Create(text9), Create(text10))
        self.wait(2)
        self.play(Unwrite(text9))
        self.play(Unwrite(text10))
        self.play(Create(text11))
        self.wait(2)
        self.play(Unwrite(text11))
        self.wait(2)
        self.play(Create(text13))
        self.wait(3)
        self.play(Unwrite(text13))
        self.play(Create(text14))
        self.wait(5)

