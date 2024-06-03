import matplotlib.pyplot as plt #matplotlib.pyplot과 matplotlib.patches를 가져옵니다. 이 모듈들은 그래프를 그리고, 도형을 만드는데 사용됩니다.
import matplotlib.patches
from .Point import Point #현재 디렉토리의 point모듈에서 point클래스를 가져옵니다.

class Circle(Point): #point클래스를 상속하는 새로운 클래스Circle를 정의합니다.

    def __init__(self, x, y, r, _axes=None): #Circle클래스의 생성자를 정의합니다. 이 생성자는 x좌표,y좌표,반지름r,그리고 선택적으로 _axes를 인자로 받습니다.
        super().__init__(x,y,_axes)  #부모클래스 point의 생성자를 호출합니다.
        self.r = r #객체의 반지름을 설정합니다.

    def draw(self): #Circle객체를 그리는 메서드를 정의합니다.
        super().draw() #부모 클래스point의 draw메서드를 호출하여 중심점을 그립니다.
        c = matplotlib.patches.Circle(
            xy = (self.x,self.y),
            radius= self.r,
            fc = 'b',
            ec = 'k', 
        )                   #matplotlib.patches.Circle을 사용하여 원을 생성합니다. 이 원의 중심은 (self.x, self.y), 반지름은 self.r, 채우기 색은 파란색(‘b’), 테두리 색은 검은색(‘k’)입니다.
        self.axes.add_patch(c) #원을 그래프에 추가합니다.
        return self.axes       #axes를 반환합니다.

if __name__ == "__main__":  #이 스크립트가 직접 실행되는 경우에만 아래의 코드를 실행합니다.
    a = Circle(3,3,1)       #x와 y 좌표가 각각 3이고, 반지름이 1인 Circle 객체 a를 생성합니다.
    a.draw()                #a를 그립니다.
    a.show()                #그림을 그려줍니다 이 메서드는 point클래스에 정의되어 있어야 합니다.