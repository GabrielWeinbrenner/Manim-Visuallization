# python C:/Manim/manim/manim.py Linked_List.py Intro -pl
from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        self.question()
        self.bulletPoints()
        self.visual()
    def question(self):
        linkedListQuestion = TextMobject(
            "What is a ", "Linked List", "?"
        )
        linkedListQuestion.set_color_by_tex("Linked List", YELLOW)
        self.play(Write(linkedListQuestion))
        self.wait(2)
        self.play(ApplyMethod(linkedListQuestion.shift, 7*UP))
    def bulletPoints(self):
        self.add_title("Linked Lists")
        self.play(FadeIn(self.title))
        items = VGroup(*list(map(self.createBulletPoint,
        ["are sets of data connected through links",
         "have a head that connects the rest of the nodes",
         "are utilized for their O(1) removal and insertion"]
        )))
        for item in items:
            self.wait()
            self.play(LaggedStartMap(FadeIn, item))
        self.wait(10)
        self.play(FadeOut(items),
        FadeOut(self.title))


    def visual(self):
        linkedListQuestion = TextMobject(
            "What does a ", "Linked List ", "look like?"
        )
        linkedListQuestion.set_color_by_tex("Linked List", YELLOW)
        self.play(Write(linkedListQuestion))
        self.wait(2)
        self.play(ApplyMethod(linkedListQuestion.shift, 3*UP))
        squares = list(map(self.createNode, 
        [6,3,0,-3,-6]))
        vals = ["10", "32", "2", "5", "8"]
        for i in range(0,len(squares)):
            if len(squares) == i:
                break
            value = TextMobject(vals[i]).set_color(BLACK)
            value.move_to(squares[i].get_top()+DOWN)
            self.play(FadeIn(squares[i]), Write(value))
            if i == 0:
                typeOf = TextMobject("Head").set_color(BLACK)
                typeOf.move_to(squares[i].get_top()+DOWN*0.3)
                self.play(Write(typeOf))
            if not(len(squares)-1 == i):
                a = Arrow(squares[i], squares[i+1])
                a.shift(DOWN)
                self.play(FadeIn(a))
            else:
                typeOf = TextMobject("Tail").set_color(BLACK)
                typeOf.move_to(squares[i].get_top()+DOWN*0.3)
                self.play(Write(typeOf))


    def add_title(self,string):
        title = TextMobject(string)
        title.scale(1.5)
        title.to_edge(UP)
        h_line = Line(LEFT, RIGHT).scale(4)
        h_line.next_to(title, DOWN)
        self.h_line = h_line
        self.title = title

    def createBulletPoint(self, item_string):
        item = TextMobject("$\\cdot$ %s" % item_string)
        if not hasattr(self, "items"):
            self.items = VGroup(item)
            self.items.next_to(self.h_line, DOWN, MED_LARGE_BUFF)
        else:
            item.next_to(self.items, DOWN, MED_LARGE_BUFF, LEFT)
            self.items.add(item)
        return item

    def createNode(self,amount):

        square = Square(fill_color=MAROON_B, fill_opacity=1, color=MAROON_B)

        square.shift(amount*LEFT)
        return square




if __name__ == "__main__":
    module_name = 'Linked_List'  # Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module == module_name:
            print(item.name)
            os.system("python -m manim Linked_List.py %s -l" %
                      item.name)  # Does not play files
