# 导入系统级依赖库
import os
import sys

# 导入本地依赖库
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import time
import json
from socket_config import *
from vehicleControl import *
import config
import math
from utils import get_line_error, PID

sceneInfoOutputGap = config.sceneInfoOutputGap

# 设定 转向PID控制器（横向控制）
turn_pid_obj = PID(kp=1.8, motion_kp=2.5, kd=25)
# 设定 速度PID控制器（纵向控制）
speed_pid_obj = PID(kp=0.8, motion_kp=0.4, kd=5)

# 设定 可视化路径点
pathlistx = []
pathlisty = []

# 设定基础速度，速度变小时，需要修改PID参数
base_speed = 10


# 核心算法，此代码仅供参考，供大家快速学习使用，如实际使用，需遵循低耦合，高内聚等代码原则
def algorithm(apiList: APIList, vehicleControl1: vehicleControlAPI):
    # 由于此类参数随循环不断进行更新，因此需要声明全局性的变量
    global turn_pid_obj
    global speed_pid_obj
    global base_speed
    global pathlistx
    global pathlisty

    # 设定车辆停止线阈值
    endflag = False

    # 计算主车速度，由于车辆速度为矢量，分为x、y分量，因此计算速度时需要使用勾股定理计算标量大小
    car_velx = apiList.DataGnssAPI()['velX']  # 读取车辆x速度分量
    car_vely = apiList.DataGnssAPI()['velY']  # 读取车辆y速度分量
    # main_car_speed = pow(car_velx**2+car_vely**2+0.00001, 0.5)
    main_car_speed = math.sqrt(pow(car_velx, 2) + pow(car_vely, 2))  # 计算速度标量

    # 根据道路路径点 计算
    road_line_info = apiList.RoadLineListAPI()
    # print(road_line_info)
    # 获取车辆自身位置
    car_posx = apiList.DataGnssAPI()['posX']  # x位置
    car_posy = apiList.DataGnssAPI()['posY']  # y位置
    print("posx:", car_posx, " posy:", car_posy)  # 输出即时车辆位置
    # 车辆姿态组合成pair
    car_pos = (car_posx, car_posy)
    # 获取车辆当前位置与目标位置的偏差, 入参为车辆当前姿态与当前车辆参考线
    error = get_line_error(car_pos, road_line_info)
    # 转向PID参数更新，PID是基于误差的算法
    steering = turn_pid_obj.update(error)
    # print("steering: ", steering)

    # 根据前方道路障碍物有无计算速度
    ObstacleEntryList = apiList.ObstacleEntryListAPI()

    # 如果存在障碍物
    if len(ObstacleEntryList) >= 0:
        # print(ObstacleEntryList)
        # 计算障碍物与自身距离，同样使用勾股定理
        dis_error = math.sqrt(pow(car_posx - ObstacleEntryList[0]["posX"], 2) +
                              pow(car_posy - ObstacleEntryList[0]["posY"] - 4, 2))
        # 停在距离障碍物一定范围的地方
        if dis_error < 0.6:
            endflag = True

        # print(dis_error)
        # 速度PID控制算法（纵向控制）
        base_speed = speed_pid_obj.update(dis_error) * 0.5
        # print(base_speed)

    # 速度更新
    speed = base_speed

    # 控制转弯时速度，防止翻车
    if abs(steering) >= 0.2:
        speed = base_speed * 0.7

    # 速度控制，0.6等为可调节参数
    if main_car_speed >= speed * 0.6:
        # 限速，防止扣分
        vehicleControl1.brake = 9  # 控制刹车，下同
        vehicleControl1.throttle = 0  # 控制油门
    else:
        if main_car_speed <= 6:
            vehicleControl1.brake = 0
            vehicleControl1.throttle = 1
        # print("main_car_speed:", main_car_speed)

    # 到达停止线附近，防止碰撞进行刹车，并保持刹车在0.1左右，由于相关动力学约束，brake不能过大也不能过小
    if endflag:
        vehicleControl1.brake = 0.1
        vehicleControl1.throttle = 0
    else:
        pathlistx.append(car_posx)  # 将 x轴坐标 送入左上角可视化工具
        pathlisty.append(car_posy)  # 将 y轴坐标 送入左上角可视化工具

    vehicleControl1.pathlistx = pathlisty  # 送入车辆控制器中
    vehicleControl1.pathlisty = pathlistx  #

    vehicleControl1.steering = steering

    # 使用json编码工具将车辆控制数据转化为标准化数据，确保socket正常传输
    control_dict_demo = json_encoder(vehicleControl1)
    control_dict_demo = json.dumps(control_dict_demo)
    # print("speed:",main_car_speed)
    # print("throttle:",vehicleControl1.throttle,"steering:",vehicleControl1.steering)

    # 返回标准化数据
    return control_dict_demo


# 主函数
def main():
    # 循环计数器
    loop_counter = 0

    # 初始化控制API（可适当调整）
    vehicleControl1 = vehicleControlAPI(0, 0, 0)  # 控制初始化

    # 开启socket与仿真场景进行通信（无需修改）
    socketServer = SocketServer()  # 初始化socket对象
    socketServer.socket_connect()  # 建立与场景连接

    # 不断与socket进行通信（该句可进行优化，实际不建议使用死循环）
    while True:
        # 从场景中获取API信息，如自车状态、车辆属性、场景路径、障碍物信息等，API描述详见
        # https://github.com/WendellGong/autoDrive_algorithm_demo
        dataState, apiList = socketServer.socket_launch()

        # 第一次启动场景时进行握手（两次握手），类似TCP
        if dataState and loop_counter == 0:
            socketServer.socket_respond()

        # 后续启动时，进行算法处理以及给场景传送车辆控制信息
        elif dataState and apiList.messageState() and loop_counter != 0:  # 该句用以处理脏数据，防止意外报错
            if (loop_counter >= 2):
                # 核心算法函数，入参为api列表、车辆控制器，出参为json格式信息，传送给场景车辆控制信息
                control_dict_demo = algorithm(apiList, vehicleControl1)

                # socket传输json信息
                socketServer.socket_send(control_dict_demo)

        # 循环计数器累加
        loop_counter += 1


# 主函数入口
if __name__ == "__main__":
    main()

