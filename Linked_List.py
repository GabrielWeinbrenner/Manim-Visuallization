# python C:/Manim/manim/manim.py Linked_List.py Intro -pl
from manimlib.imports import *


class Intro(Scene):
    #A few simple shapes
    #Python 2.7 version runs in Python 3.7 without changes
    def construct(self):
        self.question()
        self.visual()
    def question(self):
        question = TextMobject(
            "What is a ", "Linked List", "?"
        )
        question.set_color_by_tex("Linked List", YELLOW)
        self.play(Write(question))
        self.wait(2)
        linked_word = question.get_part_by_tex("Linked List")
        self.play(FadeOut(question))
        self.play(ApplyMethod(linked_word.shift, 3*UP))
    def visual(self):
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)




if __name__ == "__main__":
    module_name = 'Linked_List'  # Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module == module_name:
            print(item.name)
            os.system("python -m manim Linked_List.py %s -l" %
                      item.name)  # Does not play files
