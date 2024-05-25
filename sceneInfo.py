import json
import math
import socket_config
import sys

data = {'Simdata':
            {'timestamp': 1708269975,
             'queue': [{'timestamp': 1708269969, 'data': '(-1.87,-2.07,0)'}]
             },
        'VehicleControl': {'throttle': 0.0, 'brake': 0.0, 'steering': 0.0, 'handbrake': False,
                           'isManualGear': False, 'gear': 3},
        'Trajectory': {
            'trajectorySize': 20,
            'trajectory':
                [{'P': {'x': -1.88, 'y': -27.07, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -28.06, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -29.06, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -30.05, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -31.05, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -32.06, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -33.04, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -34.04, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -35.04, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -36.04, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -37.06, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -38.04, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -39.05, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -40.05, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -41.04, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -42.06, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -43.03, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -44.03, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -45.03, 'z': 0.0}, 'V': None},
                 {'P': {'x': -1.88, 'y': -51.03, 'z': 0.0}, 'V': None}]},
        'DataGnss':
            {'poseGnss':
                 {'posX': -1.883, 'posY': -27.955, 'posZ': -0.042,
                  'velX': 7.03, 'velY': 0.0, 'velZ': -0.026,
                  'oriX': 0.0, 'oriY': -359.79, 'oriZ': 90.019}
             },
        'DataMainVehilce':
            {'mainVehicleId': 0, 'speed': 7.03, 'gear': 3, 'throttle': 0.0, 'brake': 0.0, 'steering': 0.0,
             'length': 4.814, 'width': 2.18, 'height': 1.908},
        'VehicleSignalLight':
            {'Signal_Light_RightBlinker': 0, 'Signal_Light_LeftBlinker': 0, 'Signal_Light_DoubleFlash': 0,
             'Signal_Light_BrakeLight': 0, 'Signal_Light_FrontLight': 0, 'Signal_Light_HighBeam': 0,
             'Signal_Light_BackDrive': 0},
        'ObstacleEntryList': [
            {'id': -344300, 'viewId': -344300, 'type': 6, 'posX': -1.88, 'posY': -60.0, 'posZ': 0.0, 'oriX': 0.0,
             'oriY': 0.0, 'oriZ': 90.0, 'velX': 0.0, 'velY': 0.0, 'velZ': 0.0, 'length': 4.0, 'width': 1.81,
             'height': 1.53, 'RedundantValue': None}],
        'TrafficLightList': [{"pos":
                                  {"posX":-9.09,"posY":15.49,"posZ":0.0,
                                   "velX":0.0,"velY":0.0,"velZ":0.0,
                                   "oriX":0.0,"oriY":0.0,"oriZ":0.0},
                              "type":2,
                              "Signal_Light_red":0,
                              "Signal_Light_yellow":0,
                              "Signal_Light_green":1}],
        'RoadLineList': [{'Type': 1,
                          'PointPath': [{'x': 7.5, 'y': 65.22, 'z': 0.0},
                                        {'x': 7.5, 'y': 54.35, 'z': 0.0},
                                        {'x': 7.5, 'y': 43.48, 'z': 0.0},
                                        {'x': 7.5, 'y': 32.61, 'z': 0.0},
                                        {'x': 7.5, 'y': 21.74, 'z': 0.0},
                                        {'x': 7.5, 'y': 10.87, 'z': 0.0},
                                        {'x': 7.5, 'y': 0.0, 'z': 0.0},
                                        {'x': 7.49, 'y': -10.87, 'z': 0.0},
                                        {'x': 7.49, 'y': -21.74, 'z': 0.0},
                                        {'x': 7.49, 'y': -32.61, 'z': 0.0},
                                        {'x': 7.49, 'y': -43.48, 'z': 0.0},
                                        {'x': 7.49, 'y': -54.35, 'z': 0.0},
                                        {'x': 7.49, 'y': -65.22, 'z': 0.0},
                                        {'x': 7.49, 'y': -76.09, 'z': 0.0},
                                        {'x': 7.49, 'y': -86.96, 'z': 0.0},
                                        {'x': 7.49, 'y': -97.83, 'z': 0.0},
                                        {'x': 7.49, 'y': -108.7, 'z': 0.0},
                                        {'x': 7.49, 'y': -119.57, 'z': 0.0}]
                          },
                         {'Type': 1,
                          'PointPath': [{'x': -7.49, 'y': 65.22, 'z': 0.0},
                                        {'x': -7.49, 'y': 54.35, 'z': 0.0},
                                        {'x': -7.49, 'y': 43.48, 'z': 0.0},
                                        {'x': -7.49, 'y': 32.61, 'z': 0.0},
                                        {'x': -7.49, 'y': 21.74, 'z': 0.0},
                                        {'x': -7.49, 'y': 10.87, 'z': 0.0},
                                        {'x': -7.5, 'y': 0.0, 'z': 0.0},
                                        {'x': -7.5, 'y': -10.87, 'z': 0.0},
                                        {'x': -7.5, 'y': -21.74, 'z': 0.0},
                                        {'x': -7.5, 'y': -32.61, 'z': 0.0},
                                        {'x': -7.5, 'y': -43.48, 'z': 0.0},
                                        {'x': -7.5, 'y': -54.35, 'z': 0.0},
                                        {'x': -7.5, 'y': -65.22, 'z': 0.0},
                                        {'x': -7.5, 'y': -76.09, 'z': 0.0},
                                        {'x': -7.5, 'y': -86.96, 'z': 0.0},
                                        {'x': -7.5, 'y': -97.83, 'z': 0.0},
                                        {'x': -7.5, 'y': -108.7, 'z': 0.0},
                                        {'x': -7.5, 'y': -119.57, 'z': 0.0}]},
                         {'Type': 0,
                          'PointPath': [{'x': 0.0, 'y': 65.22, 'z': 0.0},
                                        {'x': 0.0, 'y': 54.35, 'z': 0.0},
                                        {'x': 0.0, 'y': 43.48, 'z': 0.0},
                                        {'x': 0.0, 'y': 32.61, 'z': 0.0},
                                        {'x': 0.0, 'y': 21.74, 'z': 0.0},
                                        {'x': 0.0, 'y': 10.87, 'z': 0.0},
                                        {'x': 0.0, 'y': 0.0, 'z': 0.0},
                                        {'x': 0.0, 'y': -10.87, 'z': 0.0},
                                        {'x': 0.0, 'y': -21.74, 'z': 0.0},
                                        {'x': 0.0, 'y': -32.61, 'z': 0.0},
                                        {'x': 0.0, 'y': -43.48, 'z': 0.0},
                                        {'x': 0.0, 'y': -54.35, 'z': 0.0},
                                        {'x': 0.0, 'y': -65.22, 'z': 0.0},
                                        {'x': 0.0, 'y': -76.09, 'z': 0.0},
                                        {'x': 0.0, 'y': -86.96, 'z': 0.0},
                                        {'x': 0.0, 'y': -97.83, 'z': 0.0},
                                        {'x': 0.0, 'y': -108.7, 'z': 0.0},
                                        {'x': 0.0, 'y': -119.57, 'z': 0.0}]}]}

class APIList():
    def __init__(self, data):
        self.__trajList = data['Trajectory']
        self.__VehicleControl = data['VehicleControl']
        self.__DataGnss = data['DataGnss']
        self.__DataMainVehilce = data['DataMainVehilce']
        self.__VehicleSignalLight = data['VehicleSignalLight']
        self.__ObstacleEntryList = data['ObstacleEntryList']
        self.__TrafficLightList = data['TrafficLightList']
        self.__RoadLineList = data['RoadLineList']
        self.__dataflag = data

    def trajListLenAPI(self):
        return self.__trajList['trajectorySize']

    def trajListAPI(self):
        return self.__trajList

    def DataGnssAPI(self):
        return self.__DataGnss['poseGnss']

    def DataMainVehilceAPI(self):
        return self.__DataMainVehilce

    def VehicleSignalLightAPI(self):
        return self.__VehicleSignalLight

    def ObstacleEntryListAPI(self):
        return self.__ObstacleEntryList

    def TrafficLightListAPI(self):
        return self.__TrafficLightList

    def RoadLineListAPI(self):
        return self.__RoadLineList

    def messageState(self):
        if self.__dataflag == None:
            return False
        else:
            return True

    def showAllState(self):
        print(self.DataGnssAPI())
        print(self.DataMainVehilceAPI())
        print(self.ObstacleEntryListAPI())
        print(self.RoadLineListAPI())
        print(self.TrafficLightListAPI())
        print(self.trajListAPI())

class Traj:
    def __init__(self, trajData):
        self.trajLen = trajData['trajectorySize']
        self.__trajList = trajData

    def __trajListInput(self, trajData):
        addLen = len(trajData)
        for i in range(addLen):
            self.__trajList.append(trajData[i])

    def __trajListAppend(self, singleData):
        self.__trajList.append(singleData)

    def __trajClear(self):
        self.__trajList.clear()

    def trajAPI(self):
        return self.__trajList['trajectory']


class Gnss:
    def __init__(self):
        self.GnssLen = 0
        self.GnssList = []

    def __trajListInput(self, GnssData):
        self.GnssLen = len(GnssData)
        for i in range(self.GnssLen):
            self.GnssList.append(GnssData[i])

    def __trajListAppend(self, singleData):
        self.GnssList.append(singleData)

    def __trajClear(self):
        self.GnssList.clear()


class Obstacle:
    def __init__(self):
        self.ObstacleLen = 0
        self.ObstacleList = []

    def __trajListInput(self, ObstacleData):
        self.ObstacleLen = len(ObstacleData)
        for i in range(self.ObstacleLen):
            self.ObstacleList.append(ObstacleData[i])

    def __trajListAppend(self, singleData):
        self.ObstacleList.append(singleData)

    def __trajClear(self):
        self.ObstacleList.clear()


class RoadLine:
    def __init__(self):
        self.RoadLineLen = 0
        self.RoadLineList = []

    def __trajListInput(self, RoadLineData):
        self.ObstacleLen = len(RoadLineData)
        for i in range(self.RoadLineLen):
            self.RoadLineList.append(RoadLineData[i])

    def __trajListAppend(self, singleData):
        self.RoadLineList.append(singleData)

    def __trajClear(self):
        self.RoadLineList.clear()

def dist_calculate(pointAX, pointAY, pointBX, pointBY):
    return math.sqrt(math.pow(pointAX - pointBX, 2) + math.pow(pointAY - pointBY, 2))

def json_decoder(data):
    simdata = data['Simdata']
    queue_sim = simdata['queue']
    # print(queue_sim[0]['timestamp']) # queue -> timestamp data

    VehicleControl = data['VehicleControl']
    # throttle = VehicleControl['throttle']
    # brake = VehicleControl['brake']
    # steering = VehicleControl['steering']
    # handbrake = VehicleControl['handbrake']
    # isManualGear = VehicleControl['isManualGear']
    # gear = VehicleControl['gear']
    # print(VehicleControl)

    # 轨迹
    Trajectory = data['Trajectory']
    traj_size = Trajectory['trajectorySize']
    trajectory = Trajectory['trajectory']
    print("traj:", len(trajectory), trajectory[0]['P'])
    #print("traj:", type(trajectory), len(trajectory), trajectory[0]['P']['x'])

    # 输出自身姿态
    DataGnss = data['DataGnss']
    poseGnss = DataGnss['poseGnss']
    if len(poseGnss) != 0:
        print("pose: ", len(poseGnss), poseGnss)
    # print("pose: ", type(poseGnss), len(poseGnss), poseGnss)

    # 输出主车固有信息
    # DataMainVehilce = data['DataMainVehilce']
    #if len(DataMainVehilce) != 0:
        # print("MainVehicle info: ", len(DataMainVehilce), DataMainVehilce) # 包含车辆尺寸信息

    #输出车灯状态
    # VehicleSignalLight = data['VehicleSignalLight']
    #if len(VehicleSignalLight) != 0:
        # print("SignalLight: ", len(VehicleSignalLight), VehicleSignalLight)

    #输出障碍物列表
    ObstacleEntryList = data['ObstacleEntryList']
    for i in range(len(ObstacleEntryList)) :
        print("obstacle: ", len(ObstacleEntryList), ObstacleEntryList[0])

        print("distance to obstacle: ", dist_calculate(poseGnss['posX'], poseGnss['posY'],
                                                       ObstacleEntryList[i]['posX'], ObstacleEntryList[i]['posY']))
    # print("obstacle: ", len(ObstacleEntryList), ObstacleEntryList[0]['posX'])

    #输出交通信号灯数据
    TrafficLightList = data['TrafficLightList']
    if len(TrafficLightList) != 0:
        print("TrafficLight: ", len(TrafficLightList),
              "Signal_Light_red:",
              TrafficLightList[0]['Signal_Light_red'],
              "Signal_Light_yellow:",
              TrafficLightList[0]['Signal_Light_yellow'],
              "Signal_Light_green:",
              TrafficLightList[0]['Signal_Light_green'])
        print("V2X_TrafficLight: ", len(TrafficLightList),
              "V2X_Signal_Light_red:",
              TrafficLightList[0]['Signal_Light_red'],
              "V2X_Signal_Light_yellow:",
              TrafficLightList[0]['Signal_Light_yellow'],
              "V2X_Signal_Light_green:",
              TrafficLightList[0]['Signal_Light_green'])

    #输出道路参考线
    RoadLineList = data['RoadLineList']
    if len(RoadLineList) != 0:
        print("RoadLineList: ", len(RoadLineList), RoadLineList[0])

if __name__ == "__main__":
    apiList = APIList(data)
    apiList.showAllState()

    #json_decoder(data)