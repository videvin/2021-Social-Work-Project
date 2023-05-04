from manim import *

class ct(Scene):
    def construct(self):

        funny_text = MathTex("f(x) = e^{nx}")
        self.play(Write(funny_text))

        index_labels(funny_text[0])

        funny_copy = funny_text[0][6]
        funny_copy_1 = MathTex("1", font_size=30, color=RED).shift(funny_copy.get_center())
        funny_copy_2 = MathTex("2", font_size=30, color=RED).shift(funny_copy.get_center())
        funny_copy_3 = MathTex("3", font_size=30, color=RED).shift(funny_copy.get_center())
        funny_copy_4 = MathTex("4", font_size=30, color=RED).shift(funny_copy.get_center())
        self.play(FadeToColor(funny_copy, color=RED))
        self.play(FadeTransform(funny_copy, funny_copy_1))
        self.play(FadeTransform(funny_copy_1, funny_copy_2))
        self.play(FadeTransform(funny_copy_2, funny_copy_3))
        self.play(FadeTransform(funny_copy_3, funny_copy_4))        


