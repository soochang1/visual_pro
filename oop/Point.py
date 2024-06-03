import matplotlib.pyplot as plt #matplotlib을 plt라는 이름으로 가져옵니다. 이 모듈은 그래프를 그리는데 사용됩니다.
from .MObject import MObject #현재 디렉토리의 MObject모듈에서 MObject클래스를 가져옵니다.

class Point(MObject): #MObject 클래스를 상속하는 새로운 클래스 Point를 정의합니다.

    def __init__(self, x, y, _axes=None): #Point 클래스의 생성자를 정의합니다. 이 생성자는 x 좌표, y 좌표, 그리고 선택적으로 _axes를 인자로 받습니다.
        super().__init__(_axes) #부모 클래스 MObject의 생성자를 호출합니다.
        self.x = x #객체의 x와 y 좌표를 설정합니다
        self.y = y
        if _axes != None: #_axes가 None이 아니라면, 객체의 axes를 _axes로 설정합니다.
            self.axes = _axes

    def draw(self): #Point 객체를 그리는 메서드를 정의합니다.
        self.axes.plot(self.x, self.y, marker='o', c='r') #x와 y 좌표에 빨간색 원을 그립니다.
        return self.axes #axes를 반환합니다.


if __name__ == "__main__": #이 스크립트가 직접 실행되는 경우에만 아래의 코드를 실행합니다.
    a = Point(3,3) #x와 y 좌표가 모두 3인 Point 객체 a를 생성합니다.
    a.draw() #a를 그립니다.
    a.show() #그림을 보여줍니다. 이 메서드는 MObject 클래스에 정의되어 있어야 합니다.