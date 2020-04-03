import matplotlib.pyplot as plt
import numpy as np

'''read file 
fin=open("para.txt")
a=[]
for i in fin:
  a.append(float(i.strip()))
a=np.array(a)
a=a.reshape(9,3)
'''
a = np.random.random((9, 3)) * 2  # 随机生成y

print(a)
print(type(a))
y1 = a[0:, 0]
print(y1)
y2 = a[0:, 1]
print(y2)
y3 = a[0:, 2]
print(y3)

x = np.arange(1, 10)
print(x)
print(type(x))
ax = plt.subplot(224)
width = 10
hight = 3

ax.arrow(0, 0, 0, hight, width=0.01, head_width=0.1, head_length=0.3, length_includes_head=True, fc='k', ec='k')
ax.arrow(0, 0, width, 0, width=0.01, head_width=0.1, head_length=0.3, length_includes_head=True, fc='k', ec='k')

ax.axes.set_xlim(-0.5, width + 0.2)
ax.axes.set_ylim(-0.5, hight + 0.2)

plotdict = {'dx': x, 'dy': y1}
ax.plot('dx', 'dy', 'bD-', data=plotdict)

ax.plot(x, y2, 'r^-')
ax.plot(x, y3, color='#900302', marker='*', linestyle='-')

plt.show()
