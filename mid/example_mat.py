import matplotlib.pyplot as plt
import matplotlib.patches as patches

pnt_x=5
pnt_y=3

fig, axes = plt.subplots(1,1,figsize=(5,5))

plt.plot(pnt_x, pnt_y, marker='o')

r=2

cir=patches.Circle((pnt_x, pnt_y), r)
axes.add_patch(cir)

plt.show()

#클래스로 생성해보기