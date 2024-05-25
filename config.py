# 调参专用文件
from math import cos, sin, tan, pi
import numpy as np

stateShowBool = True
# 显示动画
show_animation = True
# obstacle信息输出间隔
sceneInfoOutputGap = 2
# traffic light信息开关

# 车辆几何参数
Vehicle_Length = 3.0  # 前后轮距离
Vehicle_Width = 2.0   # 车宽
LF = 3.3  # 后轮到车头距离
LB = 1.0  # 后轮到车尾距离
MAX_STEER = pi/4  # [rad] 最大偏航角

# 地图元素参数
XY_GRID_RESOLUTION = 2.0  # [m]
YAW_GRID_RESOLUTION = np.deg2rad(5.0)  # [rad]

# 动力学参数
N_STEER = 20              # number of steer command
MOTION_RESOLUTION = 0.08  # [m] path interpolate resolution

# 路径规划参数
SB_COST = 100.0          # switch back penalty cost
BACK_COST = 50.0         # backward penalty cost
STEER_CHANGE_COST = 2.0  # steer angle change penalty cost
NON_STRAIGHT_COST = 0.0  # steer angle not zero cost
H_COST = 3.0             # Heuristic cost
M_COST = 3.0             # Cost map coeffient

SB_COST = 100.0          # switch back penalty cost
BACK_COST = 50.0         # backward penalty cost
STEER_CHANGE_COST = 2.0  # steer angle change penalty cost
STEER_COST = 0.0         # steer angle not zero cost
H_COST = 2.5             # Heuristic cost
