from pynput.keyboard import Key, Listener


class vehicleControlAPI:
    def __init__(self, throttle, brake, steering):
        self.dirStr_ = None
        self.throttle = throttle
        self.brake = brake
        self.steering = steering
        self.handbrake = False
        self.isManualGear = False
        self.gear = 3
        self.dir_ = None
        self.pathlistx = []
        self.pathlisty = []

    def __throttleSet__(self, throttle, speed = 0, keyboardModel=False):
        if keyboardModel: # throttle表示预期速度 speed表示当前速度
            if throttle >= 0:
                self.throttle = throttle
                self.brake = 0
        else:
            if throttle - speed > 0:
                self.throttle = throttle - speed
                print("throttle: ", self.throttle, speed, throttle)
                self.brake = 0

    def __brakeSet__(self, brake, speed = 0, keyboardModel=False):
        if keyboardModel:
            if brake >= 0:
                self.brake = brake
                self.throttle = 0
        else:
            if brake - speed <= 0:
                self.brake = speed - brake
                print("brake: ", self.brake, speed, brake)
                self.throttle = 0

    def __steeringSet__(self, steering, yaw = 0, keyboardModel=False):
        if keyboardModel:
            self.steering = steering
        else:
            self.steering = steering - yaw
            print("steer: ", self.steering, steering, yaw)

    def __listenerInit__(self, pressState, keyboardModel=False):
        listener = Listener(on_press=pressState)  # 创建监听器
        listener.start()  # 开始监听，每次获取一个键
        listener.join()  # 加入线程

    def __keyboardControl__(self):

        def on_press(key):
            if key == Key.up:
                self.dir_ = "key_up"
                self.__throttleSet__(1, keyboardModel=True)
            elif key == Key.down:
                self.dir_ = "key_down"
                self.__brakeSet__(1, keyboardModel=True)
            elif key == Key.left:
                self.dir_ = "key_left"
                self.__steeringSet__(-0.1, keyboardModel=True)
            elif key == Key.right:
                self.dir_ = "key_right"
                self.__steeringSet__(0.1, keyboardModel=True)
            elif key == Key.enter:
                self.dir_ = "key_right"
                self.__brakeSet__(0, keyboardModel=True)

            return False

        self.__listenerInit__(on_press)
        # print(self.dir_)
        return self.dir_

    def __instructClear__(self):
        self.throttle = 0
        self.brake = 100
        self.steering = 0
        pass

    def __PidControl__(self, trajList):
        # pid算法
        pass

    def __MPCControl__(self, trajList):
        # MPC算法
        pass

# 该文件暴露给外部
def json_encoder(vehicleControlAPI):
    control_dict = {"code": 4,
                    "UserInfo": None,
                    "SimCarMsg": {
                        "Simdata": "null",
                        "VehicleControl": {
                            "throttle": 1.0,
                            "brake": 1.0,
                            "steering": 1.0,
                            "handbrake": False,
                            "isManualGear": False,
                            "gear": 3
                        },
                        "Trajectory": None,
                        "DataGnss": None,
                        "DataMainVehilce": None,
                        "VehicleSignalLight": None,
                        "ObstacleEntryList": [],
                        "TrafficLightList": [],
                        "RoadLineList": [],
                        "DashboardMsg": {
                            "x": [1.0, 2.0, 3.0],
                            "y": [1.0, 2.0, 3.0]
                        }
                    },
                    "messager": ""
                    }
    # throttle, brake, steering, handbrake, isManualGear, gear
    control_dict["SimCarMsg"]["VehicleControl"]["throttle"] = vehicleControlAPI.throttle
    control_dict["SimCarMsg"]["VehicleControl"]["brake"] = vehicleControlAPI.brake
    control_dict["SimCarMsg"]["VehicleControl"]["steering"] = vehicleControlAPI.steering
    control_dict["SimCarMsg"]["VehicleControl"]["handbrake"] = vehicleControlAPI.handbrake
    control_dict["SimCarMsg"]["VehicleControl"]["isManualGear"] = vehicleControlAPI.isManualGear
    control_dict["SimCarMsg"]["VehicleControl"]["gear"] = vehicleControlAPI.gear
    control_dict["SimCarMsg"]["DashboardMsg"]["x"] = vehicleControlAPI.pathlistx
    control_dict["SimCarMsg"]["DashboardMsg"]["y"] = vehicleControlAPI.pathlisty
    return control_dict
