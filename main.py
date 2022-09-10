import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D, art3d
from stl import mesh
from mpl_toolkits import mplot3d
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

#load cut data from file and show it
x, y, z = [],[],[]

#only for visualization
xn, yn, zn = [],[],[]

LaserPointX = []
LaserPointY = []
LaserPointZ = []

#initial point of laser
LaserPointXInit = 0.0
LaserPointYInit = -20.0
LaserPointZInit = 30.0

lines = [line.rstrip() for line in open('line.txt')]
for line in lines:
    if line:
        axisdata = line.split(' ')
        if float(axisdata[2]) < 0:
            xn.append(float(axisdata[0]))
            yn.append(float(axisdata[1]))
            zn.append(float(axisdata[2]))
        else:
            # Show line to cut
            x.append(float(axisdata[0]))
            y.append(float(axisdata[1]))
            z.append(float(axisdata[2]))

            # Rotate aligner
            print(axisdata[1])
            # FIRST poinT of laser
            LaserPointX.append(float(LaserPointXInit))
            LaserPointY.append(float(LaserPointYInit))
            LaserPointZ.append(float(LaserPointZInit))
            #Rotate aligner

            # END point or laser vesibular
            LaserPointX.append(float(axisdata[0]))
            LaserPointY.append(float(axisdata[1]))
            LaserPointZ.append(float(axisdata[2]))
            # END point or laser lingual

# Точки разворота стола п
print(*sorted(y)[:2])

ax.plot(x, y, z, color='green')  # Plot positive contour curves
ax.plot(xn, yn, zn, color='red')  # Plot negative contour curves
ax.plot(LaserPointX, LaserPointY, LaserPointZ, color='blue')


#show aligner model

# aligner_stl = mesh.Mesh.from_file('stlfile.stl')
# ax.add_collection3d(mplot3d.art3d.Poly3DCollection(aligner_stl.vectors))
# scale = aligner_stl.points.flatten()
# ax.auto_scale_xyz(scale, scale, scale)


ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.set_zlabel("Z label")

plt.show()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
