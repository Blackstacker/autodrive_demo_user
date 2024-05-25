# 智能车竞赛算法框架

## 1.代码使用方法
启动main后，再运行场景，以下是各文件用法
### main.py 
主文件，场景socket服务对接文件
### sceneInfo.pyd 
场景的原始API信息
### socket_config.pyd 
socket通信对接
### vehicleControl.pyd 
车辆控制信息
### config.py 
调参专用文件
# 2.主要API  
### APIList类（场景数据）
> trajListLenAPI(self):
	return self.__trajList['trajectorySize']  
trajListAPI(self):
	return self.__trajList  
DataGnssAPI(self):
	return self.__DataGnss['poseGnss']  
DataMainVehilceAPI(self):
	return self.__DataMainVehilce  
VehicleSignalLightAPI(self):
	return self.__VehicleSignalLight  
ObstacleEntryListAPI(self):
	return self.__ObstacleEntryList  
TrafficLightListAPI(self):
	return self.__TrafficLightList
RoadLineListAPI(self):
	return self.__RoadLineList
showAllState(self): #输出以上所有状态
### vehicleControlAPI类
>变量   
self.throttle # 油门  
self.brake = brake # 刹车  
self.steering = steering # 方向盘  
self.handbrake = False # 手刹  
self.isManualGear = False # 手动挡  
self.gear = 3 # 挡位  
self.dir_ = None # 方向  
self.pathlistx = []   # eg：[1.0, 2.0, 3.0] # 左上角调试panel界面x轴  
self.pathlisty = []   # eg：[1.0, 2.0, 3.0] # 左上角调试panel界面y轴

> 函数  
`__throttleSet__(self, throttle, speed = 0, keyboardModel=False):
	设定油门`  
`__brakeSet__(self, brake, speed = 0, keyboardModel=False):
	设定刹车`  
`__steeringSet__(self, steering, yaw = 0, keyboardModel=False):
	设定方向盘`  
`__keyboardControl__(self):
	是否为键盘控制`  
`__instructClear__(self):
	所有指令清空`  

