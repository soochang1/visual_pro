import matplotlib.pyplot as plt
import matplotlib
import oop.rectangle #oop패키지에서 Circle 및 Point클래스를 가져옵니다. 이러한 클래스는 점과 원을 나타내며, 그래프를 그릴때 사용됩니다.
import oop.point_rec

def test_external_axes():  #test_external_axes함수를 정의합니다. 이 함수는 외부에서 축을 제공받아 그래프를 그리는 테스트를 수행합니다.
    fig,axes = plt.subplots(figsize=(10,10)) #새로운 figure와 axes를 생성합니다. 이 그래프의 크기는 10*10으로 설정됩니다.
    a = oop.Point.Point(2,2,axes) #oop패키지에서 point클래스를 사용하여(2,2)위치에 점을 생성합니다. 이때 axes를 포함하여 그래프를 생성합니다.
    axes = a.draw() #생성된 점을 그립니다. 그 결과로 변경된 축을 다시 axes변수에 할당합니다.
    b = oop.Circle.Circle(4,4,2,axes) #oop패키지에서 circle클래스를 사용하여 (4,4)를 중심으로 반지름이 2인 원을 생성합니다. 이때 axes를 포함하여 그래프를 생성합니다.
    b.draw() #생성된 원을 그립니다.
    plt.show() #그래프를 화면에 표시합니다.

def test_internal_axes(): #test_internal_axes 함수를 정의합니다. 이 함수는 내부적으로 축을 생성하여 그래프를 그리는 테스트를 수행합니다.
    a = oop.Point.Point(2,2) #oop패키지에서 point클래스 사용하여 (2,2)위치에 점을 생성합니다. 이때 축을 생성하지 않습니다.
    axes = a.draw() #생성된 점을 그립니다. 그 결과로 생성된 축을 axes변수에 할당합니다.
    b = oop.Circle.Circle(4,4,2,axes) #oop 패키지에서 Circle 클래스를 사용하여 (4,4)를 중심으로 반지름이 2인 원을 생성합니다. 이때 앞서 생성된 축을 사용하여 그래프를 생성합니다.
    b.draw() #생성된 원을 그립니다.
    b.show() #그래프를 화면에 표시합니다.

if __name__ == "__main__": #이 코드 블록이 직접 실행될 때 아래의 코드를 실행합니다.
    print(matplotlib.__version__) #matplotlib 라이브러리의 버전을 출력합니다.
    # test_external_axes()
    test_internal_axes() #test_internal_axes 함수를 실행합니다.
