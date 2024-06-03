import matplotlib.pyplot as plt
import matplotlib.patches
from .point_rec import Point

class rectangle(Point):

    def __init__(self, x, y, width, height, _axes=None):
        super().__init__(x,y,_axes)
        self.width= width
        self.height= height

    def draw(self):
        super().draw()
        r = matplotlib.patches.Rectangle(
            xy = (self.x,self.y),
            width= self.width,
            height= self.height,
            fc = 'b',
            ec = 'k', 
        )
        self.axes.add_patch(r)
        return self.axes

if __name__ == "__main__":
    a = rectangle(3,3,1)
    a.draw()
    a.show()