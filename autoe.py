# autoe 模块
# 需要打开服务器
import socket

class Autoe:
	def __init__(self,host='localhost',port=19777):
		try:
			self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			self.s.connect((host,port))
		except:
			print('抱歉,服务器尚未打开,请打开服务器')
	
	# 模拟鼠标点击
	# x			横坐标
	# y			纵坐标
	# click_type	点击类型(0:左键单击  1:左键双击  2:右键单击  3:右键双击)
	def click(self,x,y,click_type=0):
		data = 'click '+ str(x) + " "+ str(y) + " "+str(click_type)
		self.send(data)

	# 模拟键盘敲击
	# one		按键1  可以输入任何单个字母和数字表示按键,也可以填#ctrl 或 #shift 按控制键
	# two		按键2  可选 ,可以输入任何单个字母和数字表示按键,也可以填#ctrl 或 #shift 按控制键
	# three		按键3  可选 ,可以输入任何单个字母和数字表示按键
	def  kbdclick(self,one,two=None,three=None):
		data = "kbdclick "+str(one)
		if two != None:
			data += " " + str(two)
		if three != None:
			data += " " + str(three)
		self.send(data)

	# 发送字节集
	def send(self,data):
		self.s.send(bytes(data,encoding="utf8"))

a = Autoe()
#a.click(1,2)


while True:
	b = input('input:')
	if b=='exit':
		exit()
	a.send(b)