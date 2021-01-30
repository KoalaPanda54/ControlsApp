from p5 import Vector
from p5 import push_matrix, pop_matrix, translate

class UIObject:
    def __init__(self, pos : Vector, depth : int = 0):
        self.parent = None
        self.depth = depth
        self.children = []
        self.pos = pos

    def render(self):
        pass

    def set_parent(self, parent, keep_world_pos = True):
        parent.add_child(self)
        if keep_world_pos:
            self.pos = self.pos - parent.pos
        

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def remove_child_at_index(self, index):
        self.children.pop(index)

    def mouse_over(self):
        pass

    def mouse_enter(self):
        pass

    def mouse_exit(self):
        pass

    def mouse_click(self):
        pass

    def mouse_up(self):
        pass

    def mouse_down(self):
        pass

def sort_ui(a):
    return a.depth

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.elements = []

    def add_element(self, element : UIObject):
        self.elements.append(element)
        self.elements.sort(key=sort_ui)

    def render(self):
        for element in self.elements:
            new_pos = element.pos
            if element.parent != None:
                new_pos += element.parent.pos

            push_matrix()
            translate(new_pos.x, new_pos.y, element.depth*2)
            element.render()
            pop_matrix()