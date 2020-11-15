import sys, pygame, time, random, math

pygame.init()

black = 0,0,0
red = 255,0,0
green = 0,255,0
white = 255,255,255
yellow = 255,255,0
WINSIZE = WIN_WIDTH, WIN_HEIGHT = 800, 600

screen = pygame.display.set_mode((WINSIZE), pygame.RESIZABLE)

font = pygame.font.Font("freesansbold.ttf",13)

x = 400
y = 300

xmove = 0
ymove = 0

boxXCo = 400
boxYCo = 30
boxWIDTH = 30
boxHEIGHT = 30

thickness = 2
line = pygame.draw.rect(screen, white, (0,150,800,3))

class blackBox:
	font = pygame.font.Font("freesansbold.ttf",13)
	screen = pygame.display.set_mode(WINSIZE)
	white = 255,255,255

	def __init__(self,boxwidth,boxheight,x,y):
		self.boxwidth = boxwidth
		self.boxheight = boxheight
		self.x = x
		self.y = y

	def draw(self):
		blackBox = pygame.draw.rect(screen, white, (x,y,self.boxwidth,self.boxheight))

	def show_coords(self):
		coordText = font.render("Co-ordinates:", True,(green))
		screen.blit(coordText, (10,10))
		xCordText = font.render("X: " + str(x), True,(green))
		yCoordText = font.render("Y: " + str(y), True,(green))
		screen.blit(xCordText, (10,40))
		screen.blit(yCoordText, (10,80))

class park:
	thickness = 2

	def __init__(self,screen,color,boxXCo,boxYCo,boxWIDTH,boxHEIGHT):
		self.screen = screen
		self.boxXCo = boxXCo
		self.boxYCo = boxYCo
		self.boxWIDTH = boxWIDTH
		self.boxHEIGHT = boxHEIGHT
		self.color = color
		self.thickness = thickness

	def draw(self):
		line1 = pygame.draw.line(screen, self.color,(boxXCo, boxYCo),( boxXCo + boxWIDTH, boxYCo),thickness)
		line2 = pygame.draw.line(screen, self.color,(boxXCo + boxWIDTH,boxYCo),(boxXCo + boxWIDTH,boxYCo + boxHEIGHT), thickness)
		line3 = pygame.draw.line(screen, self.color,(boxXCo + boxWIDTH,boxYCo + boxHEIGHT),(boxXCo,boxYCo + boxHEIGHT), thickness)
		line4 = pygame.draw.line(screen, self.color,(boxXCo,boxYCo + boxHEIGHT),(boxXCo,boxYCo), thickness)

def collision():
	xCo = 400
	yCo = 30
	width = 30
	height = 30
	thickness = 2
	#distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
	i = 0
	for i in range(0,800):
		distance = math.sqrt((math.pow(i - x,2)) + (math.pow(150 - y,2)))
		if distance < 0.5 or distance < -0.5:
			return True
	return False

def line():
	line = pygame.draw.rect(screen, white, (0,150,800,3))
# rate of movement
sensitivity = 2
def left():
	global x,xmove
	xmove = - sensitivity
	x -= xmove
def right():
	global x,xmove
	xmove = + sensitivity
	x += xmove 
def forward():
	global y,ymove
	ymove = - sensitivity
	y -= ymove
def backward():
	global y,ymove
	ymove = + sensitivity
	y += ymove

running = True
score = 0
time = 0
timeInPark = 0

while running:
	green = 0,255,0
	clock = pygame.time.Clock()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			running = False
			sys.exit()
		if event.type == pygame.RESIZABLE:
			screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				left()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				right()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				xmove = 0			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				forward()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				backward()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				ymove = 0
	x += xmove
	y += ymove
	if x < 0:
		x = 0
	if x > 775:
		x = 775
	if y < 0:
		y = 0
	if y > 575:
		y = 575
	
	screen.fill(black)
	parkx = boxXCo + boxWIDTH/2
	parky = boxYCo + boxHEIGHT/2
	middleX = x + 12.5
	middleY = y + 12.5
	# distance between center of box and park and renders it on screen
	distance = math.sqrt((math.pow(parkx - middleX,2)) + (math.pow(parky - middleY,2)))
	distanceText = font.render("DISTANCE: " + str(distance), True,(green))
	timeText = font.render("Time: " + str(time), True,(green))
	# When box is inside Park screen prints True
	insideParkText = font.render("TRUE",1,(green))
	scoreText = font.render("Score: " + str(score),1,(green))
	# defines width,height,(x,y),xmove,ymove of box
	# Scoring mechanics
	box = blackBox(25,25,x,y)
	if distance < 5:
		timeInPark += 1
		screen.blit(insideParkText, (400,300))
		if timeInPark == 301:
			timeInPark = 0
			score += 100
			box.draw()

	screen.blit(distanceText, (10,500))
	screen.blit(scoreText, (10,400))
	screen.blit(timeText,(10,300))
	line()
	
	box.draw()
	box.show_coords()
	
	parks = park(screen,yellow,boxXCo,boxYCo,boxWIDTH,boxHEIGHT)
	parks.draw()
	time += 1
	clock.tick(60)
	pygame.display.update()