import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


widths = []
heights = []
distances = []
volumes = []
colors = []

f = open("volume_result_info_10.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    parts = line.split(",")
    widths.append(parts[0])
    heights.append(parts[1])
    distances.append(parts[2])
    # distances.append(0)
    volumes.append(parts[3].strip())
    colors.append("red")
f.close()

# for volume in volumes:
#     if volume == "10L":
#         colors.append("red")
#     else:
#         colors.append("blue")


f = open("volume_result_info_20.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    parts = line.split(",")
    widths.append(parts[0])
    heights.append(parts[1])
    distances.append(parts[2])
    # distances.append(0)
    volumes.append(parts[3].strip())
    colors.append("blue")
f.close()


# 3D 플롯을 위한 준비
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# X, Y, Z 축에 해당하는 데이터
x = [float(i) for i in widths]
y = [float(i) for i in heights]
z = [float(i) for i in distances]

# 3D 산점도 그리기
scatter = ax.scatter(x, y, z, c=colors, cmap="viridis")

# 컬러바 추가
color_bar = fig.colorbar(scatter, ax=ax, label="Volume Value")

# 레이블 추가
ax.set_xlabel("Width")
ax.set_ylabel("Height")
ax.set_zlabel("Distance")

# 플롯 보여주기
plt.show()
