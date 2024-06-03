import matplotlib.pyplot as plt
import matplotlib
import oop_rectangle.rectangle
import oop_rectangle.point_rec

def test_external_axes():
    fig,axes = plt.subplots(figsize=(10,10))
    a = oop_rectangle.point_rec.Point(2,2,axes)
    axes = a.draw()
    b = oop_rectangle.rectangle.rectangle(4,4,4,2,axes)
    b.draw()
    plt.show()

def test_internal_axes():
    a = oop_rectangle.point_rec.Point(2,2)
    axes = a.draw()
    b = oop_rectangle.rectangle.rectangle(4,4,4,2,axes)
    b.draw()
    b.show()

if __name__ == "__main__":
    print(matplotlib.__version__)
    # test_external_axes()
    test_internal_axes()