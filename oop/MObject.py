import matplotlib.pyplot as plt #matplotlib 라이브러리를 사용하여 그래프를 그리는데 필요합니다.

class MObject: #MObject클래스를 정의합니다. 이 클래스는 matplotlib 그래프를 관리하고 그릴 수 있는 기능을 제공합니다.

    def __init__(self,_axes=None): #클래스의 초기화 메서드를 정의합니다. _axes 매개변수를 받으며, 이는 그래프를 그릴 축을 나타냅니다. 기본값은 none입니다.
        self.figure = None #클래스의 인스턴스 변수인 figure와 axes를 초기화합니다.
        self.axes = None #이는 그래프를 그릴 축을 나타냅니다. 기본값은 none입니다.
        if self.axes == None: #기본값이 none이므로 항상 실행됨
            if _axes == None: #_axes가 none인지 확인합니다.
                self.figure, self.axes = plt.subplots(
                    figsize=(5,5)  #그래프의 크기는 (5,5)로 설정됩니다.
                )
                # self.fig = plt.figure(
                #     figsize=(5,5),
                #     facecolor = 'w',
                # )
                # self.axes = self.fig.add_axes(
                #     (0.1,0.1,0.8,0.8),
                # )
            else:
                self.axes = _axes #_axes가 none이지만, 만약에 아닌 경우 _axes를 self.axes로 설정합니다.
        else:
            if _axes == None: #self.axes가 none이 아니고, 주어진 _axes가 none인지 확인합니다. 이 경우 아무 작업도 하지않습니다.
                pass
            else:
                self.axes = _axes #

    def draw(self):
        pass # to be implemented

    def __call__(self): #객체가 함수처럼 호출될 수 있도록 하는 특수 메서드인 call()을 정의합니다.
        return self.draw() #객체가 호출될 때 draw()메서드를 호출하도록 설정합니다.

    def show(self): #그래프를 화면에 표시하는 show()메서드를 정의합니다.
        plt.show() #그래프를 화면에 표시하기 위해 plt.show()함수를 호출합니다