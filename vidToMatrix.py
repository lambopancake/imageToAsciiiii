import cv2,os


def per(inte, resLen):
	return int((inte/255.0)* 100 * ((resLen-1)*0.01)) 

def printStuff(imageBW, x, y):

	res = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.          "
	res = res[::-1]
	clar = 15
	for i in range(0,x,clar):
		for j in range(0,y,clar):
			#print(i ," ", j)
			try:
				inte = int(imageBW[i,j])
			except:
				print("",end = "")
			print(f"{res[per(inte,len(res))]}", end = " ")
		print("")

vid = cv2.VideoCapture(0)

width  = vid.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`
# or
width  = vid.get(3)  # float `width`
height = vid.get(4)  # float `height`

print('width, height:', width, height)

x = int(width)
y = int(height) 


i = 0
os.system('cls')
while i < 1000:
	
	frame = vid.read()[1]
	blackAndWhite = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#print(blackAndWhite)
	#cv2.imshow("sup", blackAndWhite)
	
	printStuff(blackAndWhite,x, y)
	os.system('clear')
	key = cv2.waitKey(20)
	if key == 27: #hit esc to quit
		break
	i += 1

vid.release()
#cv2.destroyWindow()