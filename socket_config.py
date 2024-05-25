import socket
import sys
import json
from sceneInfo import APIList
key = "yuandongli202311"

class SocketServer():
    def __init__(self):
        self.__conn = None

    def socket_connect(self):
        # 建立websocket连接
        try:
            x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            x.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            x.bind(("127.0.0.1", 5061))
            x.listen(10)

            self.__conn, address = x.accept()
        except socket.error as msg:
            print(msg)
            sys.exit(1)
        return self.__conn, address

    def socket_launch(self):
        result = self.__conn.recv(4096 * 500)
        dataList = result.split(b"|end")  # 使用|end作为分隔符
        data = dataList[0]
        data_json = json.loads(data)
        apiList = None
        dataState = False
        if data != None:
            dataState = True
            print(data_json)
            if data_json['SimCarMsg'] != None:
                apiList = APIList(data_json['SimCarMsg'])

        return dataState, apiList

    def socket_respond(self):
        self.__conn.send(bytes('{"code":2,"UserInfo":null,"SimCarMsg":null, "messager":""}',
                        encoding="utf-8"))

    def socket_send(self, control_dict_demo):
        self.__conn.send(bytes(control_dict_demo, encoding="utf-8"))