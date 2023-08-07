# Name:         Swayam Parekh
# Date:         June. 17, 2022
# Class:        ICS3U1-04
# Description:  This is a shooter game that lets you indefinitely shoot bots until you die, with the difficulty increasing incrementally.


#importing all necessary modules
import pygame 
import math
import random

#setting up all color variables so "global" is not required for functions
darkMode = False
BLACK = (0,0,0)
WHITE = (255,255,255)
MAINUI = (169, 209, 208)
TEXTBOX = (186, 214, 219)
WATER = (94,184,172)
UI1 = (73, 186, 175)
UI2 = (28, 128, 118)
WAVES = (39,115,105)
BOAT = (85,73,117)
SKIN = (217,193,163)
EYE = (224,102,102)
USERPROJ1 = (245,149,66)
USERPROJ2 = (199,116,44)
BOTPROJ1 = (227, 104, 104)
BOTPROJ2 = (166, 75, 75)
GRAY = (87, 99, 94)
WINDOW = (161,198,227)
BOT1 = (85,87,101)
RED = (255,0,0)
GREEN = (0,255,0)
GRAY2 = (104, 106, 115)
GOLD = (212, 175, 55)
GOLDOUTLINE = (130, 108, 35)
SILVER = (170, 169, 173)
SILVEROUTLINE = (103, 102, 107)
BRONZE = (205, 127, 50)
BRONZEOUTLINE = (117, 70, 23)

#sets up all functions
def drawBoat(x):
    #draws the boat when it is not being moved
    pygame.draw.rect(screen, WATER, (0, 0, width, height))        
    pygame.draw.polygon(screen, BOAT, [[x,530], [x+10, 590], [x+50, 590], [x+60,530]]) 
    pygame.draw.ellipse(screen, BOAT, pygame.Rect(x-1, 475, 63, 85))
    pygame.draw.polygon(screen, BOAT, [[x+5,491], [x+30, 465], [x+55,491]])     
    pygame.draw.polygon(screen, GRAY, [[x+8,540], [x+15, 580], [x+45, 580], [x+52,540]]) 
    pygame.draw.line(screen, BLACK, (x+17,540),(x+21,580),1)
    pygame.draw.line(screen, BLACK, (x+26,540),(x+27,580),1)
    pygame.draw.line(screen, BLACK, (x+35,540),(x+33,580),1)
    pygame.draw.line(screen, BLACK, (x+44,540),(x+39,580),1)
    pygame.draw.rect(screen, BLACK, pygame.Rect(x+15,520,30,15))
    
    #draws windshield    
    pygame.draw.polygon(screen, WINDOW, [[x+15,490],[x+25,480],[x+35,480],[x+45,490]])
    pygame.draw.line(screen, WHITE,(x+26,480),(x+22,490),2)
    pygame.draw.line(screen, WHITE,(x+33,480),(x+37,490),2)
    
    #draws face
    pygame.draw.circle(screen, SKIN, (x+30,510),17)
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(x+17, 500, 12, 15))
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(x+31, 500, 12, 15))
    pygame.draw.ellipse(screen, EYE, pygame.Rect(x+19, 503, 10, 13))
    pygame.draw.ellipse(screen, EYE, pygame.Rect(x+33, 503, 10, 13))  
    pygame.draw.circle(screen, WHITE, (x+22,507),3) 
    pygame.draw.circle(screen, WHITE, (x+36,507),3)     
    pygame.draw.circle(screen, WHITE, (x+26,510),1) 
    pygame.draw.circle(screen, WHITE, (x+40,510),1)       
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+16, 499, 14, 17),1)
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+30, 499, 14, 17),1)    
    pygame.draw.line(screen, BLACK, (x+25,520),(x+35,520),2)

def drawBoatLeft(x):
    #draws the boat in its leftwards orientation 
    pygame.draw.rect(screen, WATER, (0, 0, width, height))    
    pygame.draw.polygon(screen, BOAT, [[x,530], [x+10, 590], [x+50, 590], [x+60,530]]) 
    pygame.draw.ellipse(screen, BOAT, pygame.Rect(x-1, 475, 63, 85))
    pygame.draw.polygon(screen, BOAT, [[x+5,491], [x+30, 465], [x+55,491]])     
    pygame.draw.polygon(screen, GRAY, [[x+8,540], [x+15, 580], [x+45, 580], [x+52,540]]) 
    pygame.draw.line(screen, BLACK, (x+17,540),(x+21,580),1)
    pygame.draw.line(screen, BLACK, (x+26,540),(x+27,580),1)
    pygame.draw.line(screen, BLACK, (x+35,540),(x+33,580),1)
    pygame.draw.line(screen, BLACK, (x+44,540),(x+39,580),1)
    pygame.draw.rect(screen, BLACK, pygame.Rect(x+15,520,30,15))
    
    #draws windshield
    pygame.draw.polygon(screen, WINDOW, [[x+15,490],[x+25,480],[x+35,480],[x+45,490]])
    pygame.draw.line(screen, WHITE,(x+26,480),(x+22,490),2)
    pygame.draw.line(screen, WHITE,(x+33,480),(x+37,490),2)
    
    #draws face
    pygame.draw.circle(screen, SKIN, (x+30,510),17)
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(x+17, 500, 12, 15))
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(x+31, 500, 12, 15))
    pygame.draw.ellipse(screen, EYE, pygame.Rect(x+19, 503, 10, 13))
    pygame.draw.ellipse(screen, EYE, pygame.Rect(x+33, 503, 10, 13))  
    pygame.draw.circle(screen, WHITE, (x+22,507),3) 
    pygame.draw.circle(screen, WHITE, (x+36,507),3)     
    pygame.draw.circle(screen, WHITE, (x+26,510),1) 
    pygame.draw.circle(screen, WHITE, (x+40,510),1)       
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+16, 499, 14, 17),1)
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+30, 499, 14, 17),1)    
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+25, 517, 10, 8))       

    #draws the moving waves
    for x in range (random.randint(60,80)):
        wavesX = (x+boatX+50)
        wavesY1 = wavesAmplitude*math.sin((wavesX)/wavesPeriod)+515
        wavesY2 = wavesAmplitude*math.sin((wavesX)/wavesPeriod)+540
        wavesY3 = wavesAmplitude*math.sin((wavesX)/wavesPeriod)+565
        pygame.draw.circle(screen, WAVES,(wavesX,wavesY1),1)
        pygame.draw.circle(screen, WAVES,(wavesX,wavesY2),1)
        pygame.draw.circle(screen, WAVES,(wavesX,wavesY3),1)

def drawBoatRight(x):
    #draws the boat in its rightwards orientation
    pygame.draw.rect(screen, WATER, (0, 0, width, height))        
    pygame.draw.polygon(screen, BOAT, [[x,530], [x+10, 590], [x+50, 590], [x+60,530]]) 
    pygame.draw.ellipse(screen, BOAT, pygame.Rect(x-1, 475, 63, 85))
    pygame.draw.polygon(screen, BOAT, [[x+5,491], [x+30, 465], [x+55,491]])     
    pygame.draw.polygon(screen, GRAY, [[x+8,540], [x+15, 580], [x+45, 580], [x+52,540]]) 
    pygame.draw.line(screen, BLACK, (x+17,540),(x+21,580),1)
    pygame.draw.line(screen, BLACK, (x+26,540),(x+27,580),1)
    pygame.draw.line(screen, BLACK, (x+35,540),(x+33,580),1)
    pygame.draw.line(screen, BLACK, (x+44,540),(x+39,580),1)
    pygame.draw.rect(screen, BLACK, pygame.Rect(x+15,520,30,15))
    
    #draws windshield    
    pygame.draw.polygon(screen, WINDOW, [[x+15,490],[x+25,480],[x+35,480],[x+45,490]])
    pygame.draw.line(screen, WHITE,(x+26,480),(x+22,490),2)
    pygame.draw.line(screen, WHITE,(x+33,480),(x+37,490),2)
    
    #draws face
    pygame.draw.circle(screen, SKIN, (x+30,510),17)
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(x+17, 500, 12, 15))
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(x+31, 500, 12, 15))
    pygame.draw.ellipse(screen, EYE, pygame.Rect(x+19, 503, 10, 13))
    pygame.draw.ellipse(screen, EYE, pygame.Rect(x+33, 503, 10, 13))  
    pygame.draw.circle(screen, WHITE, (x+22,507),3) 
    pygame.draw.circle(screen, WHITE, (x+36,507),3)     
    pygame.draw.circle(screen, WHITE, (x+26,510),1) 
    pygame.draw.circle(screen, WHITE, (x+40,510),1)       
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+16, 499, 14, 17),1)
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+30, 499, 14, 17),1)    
    pygame.draw.arc(screen, BLACK, pygame.Rect(x+25,515,10,8),math.pi,0,10)        
    
    #draws the moving waves    
    for x in range (random.randint(60,80)):
        wavesX = (boatX-x)
        wavesY1 = wavesAmplitude*math.sin(-1*wavesX/wavesPeriod)+515
        wavesY2 = wavesAmplitude*math.sin(-1*wavesX/wavesPeriod)+540
        wavesY3 = wavesAmplitude*math.sin(-1*wavesX/wavesPeriod)+565
        pygame.draw.circle(screen, WAVES,(wavesX,wavesY1),1)
        pygame.draw.circle(screen, WAVES,(wavesX,wavesY2),1)
        pygame.draw.circle(screen, WAVES,(wavesX,wavesY3),1)
       
    
def userProjectile(screen,x,y):
    #draws the user-shot projectile at any coordinate
    pygame.draw.circle(screen, USERPROJ2, (x,y), 10)
    pygame.draw.circle(screen, USERPROJ1, (x,y), 8)
    
def botProjectile(screen,x,y):
    #draws the user-shot projectile at any coordinate
    pygame.draw.circle(screen, BOTPROJ2, (x,y), 10)
    pygame.draw.circle(screen, BOTPROJ1, (x,y), 8)

def drawBot(screen, x, y):
    #draws the bot based on coordinates determined by related lists
    #draws the main body of the bot
    pygame.draw.polygon(screen, BLACK,[[x-1,y+14], [x+9,y+41], [x+31,y+41],[x+41,y+14]])    
    pygame.draw.polygon(screen, BOT1,[[x,y+15], [x+10,y+40], [x+30,y+40],[x+40,y+15]])
    pygame.draw.polygon(screen, RED,[[x+13,y+20], [x+15,y+27], [x+25,y+27],[x+27,y+20]])
    
    #draws the upper body of the bot
    pygame.draw.rect(screen, BLACK, pygame.Rect(x-12,y,62,15))       
    pygame.draw.rect(screen, BOT1, pygame.Rect(x-12,y+2,62,12))   
    pygame.draw.rect(screen, BLACK, pygame.Rect(x-12,y+5,62,3))           
    
    #draws the head of the bot
    pygame.draw.polygon(screen, BOT1,[[x+4,y-25], [x+1,y-30], [x+6,y-40],[x+6,y-30],[x+9,y-25]]) 
    pygame.draw.polygon(screen, BOT1,[[x+36,y-25], [x+39,y-30], [x+34,y-40],[x+34,y-30],[x+31,y-25]])    
    pygame.draw.polygon(screen, BOT1,[[x,y], [x+5,y-25], [x+35,y-25],[x+40,y]])
    pygame.draw.polygon(screen, WHITE,[[x+6,y-4], [x+8,y-12], [x+32,y-12],[x+34,y-4]])   
    pygame.draw.line(screen, BLACK, (x+13,y-4),(x+14,y-12),1)
    pygame.draw.line(screen, BLACK, (x+20,y-4),(x+20,y-12),1)
    pygame.draw.line(screen, BLACK, (x+27,y-4),(x+26,y-12),1)
    pygame.draw.line(screen, RED, (x+12,y-18),(x+17,y-18),3)
    pygame.draw.line(screen, RED, (x+23,y-18),(x+28,y-18),3)
    
    #draws the arms of the bot
    pygame.draw.rect(screen, BOT1, pygame.Rect(x-15,y+5,10,25))   
    pygame.draw.rect(screen, BOT1, pygame.Rect(x+45,y+5,10,25))   
    pygame.draw.rect(screen, BLACK, pygame.Rect(x-23,y+30,25,15))     
    pygame.draw.rect(screen, BLACK, pygame.Rect(x+39,y+30,25,15)) 
    pygame.draw.rect(screen, WINDOW, pygame.Rect(x-20,y+30,19,15))           
    pygame.draw.rect(screen, WINDOW, pygame.Rect(x+42,y+30,19,15)) 
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(x,y+36,1,3))  
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(x+62,y+36,1,3))  
    
    #draws the shoulders of the bot
    pygame.draw.ellipse(screen, BOT1, pygame.Rect(x-20,y,35,20))  
    pygame.draw.ellipse(screen, BOT1, pygame.Rect(x+25,y,35,20))
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x-20,y,35,20),1)  
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+25,y,35,20),1)       
    pygame.draw.circle(screen, BOT1, (x-12,y+10),10) 
    pygame.draw.circle(screen, BOT1, (x+52,y+10),10)  
    pygame.draw.circle(screen, BLACK, (x-12,y+10),10,1) 
    pygame.draw.circle(screen, BLACK, (x+52,y+10),10,1) 

def colourPicker(y): 
    #sets each rgb value to 0
    red = 0
    green = 0
    blue = 0   
    #creates a grayscale gradient that fits within an x range of 50. the constant "grayRange" ensures each value increments by the proper amount.
    for grays in range (50):
        red+=grayRange
        green+=grayRange
        blue+=grayRange
        #all colors are appended so each can be accessed
        grayColours.append((red, green, blue))
        if red > 255:
            red = 255
            green = 255
            blue = 255   
        #gradient is drawn
        pygame.draw.line(screen, (red, green, blue), (grays + width//2-263,y), (grays + width//2-263, y+25))   
    
    #creates a full rgb gradient that loops 6 times for 2 changes each in rgb values. fits within an x range of 410. the constant "colourRange" ensures each value increments by the proper amount.
    red = 255
    green = 0
    blue = 0
    spectrumPortionTracker = 0 #counter that keeps track of all 6 loops  
    for colours in range(410):
        #gradient to yellow | green increases
        if spectrumPortionTracker == 0:
            green += colourRange
            #all colours are appended so each can be accessed
            allColours.append((red, green, blue))
            if green > 255:
                green = 255
                spectrumPortionTracker += 1
                
        #gradient to green | red decreases
        elif spectrumPortionTracker == 1:
            red -= colourRange
            #all colours are appended so each can be accessed            
            allColours.append((red, green, blue))
            if red < 0:
                red = 0
                spectrumPortionTracker += 1
        
        #gradient to cyan | blue increases
        elif spectrumPortionTracker == 2:
            blue += colourRange
            #all colours are appended so each can be accessed            
            allColours.append((red, green, blue))
            if blue > 255:
                blue = 255
                spectrumPortionTracker += 1
                
        #gradient to blue | green decreases
        elif spectrumPortionTracker == 3:
            green -= colourRange
            #all colours are appended so each can be accessed            
            allColours.append((red, green, blue))
            if green < 0:
                green = 0
                spectrumPortionTracker += 1
        
        #gradient to purple | red increases
        elif spectrumPortionTracker == 4:
            red += colourRange
            #all colours are appended so each can be accessed            
            allColours.append((red, green, blue))       
            if red > 255:
                red = 255
                spectrumPortionTracker += 1
                
        #gradient back to red | blue decreases
        elif spectrumPortionTracker == 5:
            blue -= colourRange
            #all colours are appended so each can be accessed            
            allColours.append((red, green, blue))
            if blue < 0:
                blue = 0
                spectrumPortionTracker += 1
        #gradient is drawn
        pygame.draw.line(screen, (red, green, blue), (colours + width//2-213,y), (colours + width//2-213, y+25))   
        
def skinColourPicker(y): 
    #sets each rgb value to 0    
    red = 0
    green = 0
    blue = 0 
    #creates a grayscale gradient that fits within an x range of 50. the constant "grayRange" ensures each value increments by the proper amount.    
    for grays in range (50):
        red+=grayRange
        green+=grayRange
        blue+=grayRange
        #all colours are appended so each can be accessed        
        grayColours.append((red, green, blue))
        if red > 255:
            red = 255
            green = 255
            blue = 255  
        #gradient is drawn
        pygame.draw.line(screen, (red, green, blue), (grays + width//2-263,y), (grays + width//2-263, y+25))      
    
    #sets up the initial rgb values and the end rgb values as well as the variable that stores each color within the gradient
    skinRed = 242
    skinGreen = 227
    skinBlue = 203
    startRed = 242
    startGreen = 227
    startBlue = 203   
    endRed = 51
    endGreen = 33
    endBlue = 6
    
    #creates a gradient that fits within an x range of 50. the variables "redRange, greenRange & blueRange" ensure each value increments by the proper corresponding amount.        
    for skinCol in range (410):  
        redRange = (startRed - endRed)/460
        greenRange = (startGreen - endGreen)/460
        blueRange = (startBlue - endBlue)/460
        skinRed-=redRange
        skinGreen-=greenRange
        skinBlue-=blueRange
        #all skin colours are appended so each can be accessed
        skinColours.append((skinRed, skinGreen, skinBlue))
        
        #gradient is drawn
        pygame.draw.line(screen, (skinRed, skinGreen, skinBlue), (skinCol + width//2-213,y), (skinCol + width//2-213, y+25))   

#initializing the pygame window 
pygame.init()
width = 800
height = 600
SIZE = (width,height)
screen = pygame.display.set_mode(SIZE)
screen.fill(WATER)

#all variables are initialized here 
#imports all necessary fonts
titleFont = pygame.font.SysFont("Impact",100)
bodyFont = pygame.font.SysFont("Tahoma",25)
bodyFont1 = pygame.font.SysFont("Tahoma",30)
bodyFont2 = pygame.font.SysFont("Tahoma",40)
bodyFont3 = pygame.font.SysFont("Tahoma",45)
bodyFont4 = pygame.font.SysFont("Tahoma",20)
miniFont = bodyFont4 = pygame.font.SysFont("Tahoma",15)

#for boat-related movement, health, & projectile shots, preset as constants for consistency
boatX = (width//2)-25
boatY = 465
userBulletPosX = 0
userBulletPosY = 0
botBulletPosX = 0
botBulletPosY = 0
botScale = 0
boatHealth = 4

#generates periods and amplitudes for all the types of waves in the game
wavesPeriod = random.randint(3,6)
wavesAmplitude = random.randint(4,8)
botWavesAmplitude = random.randint(2,5)
botWavesPeriod = random.randint(4,8)
    
#sets up all the Boolean values that act as "switches"
keyLeft = False
keyRight = False
drawBullet = False
drawBotBullet = True
nextShot = True
nextBotShot = False
nextWave = True
menuPage = True
settingsPage = False
playGame = False
gameOver = False
gameOverPg2 = False
pausePage = False
restartPage = False
leaderboardPage = False
rulesPage = False
sorting = True

#variables for colour picker
red = 0
green = 0
blue = 0
spectrumPortionTracker = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
allColours = []
grayColours = []
grayRange = 255/50
colourRange = (255 * 6) / 410

userColour = [0, 0, 0]
skinColours = []

#Remembers the page number for the back button. (for reference: menu = 0, pausePage = 2, gameOver = 3)
pageTracker = 0

#setting up variables related to the user inputting their username
errorNum = 0
playerName = ""

#intializes score variable
score = 0


#setting up related lists that controls the randomized movement of each robot as well as tracking the health
botPosX = [0,0,0,0]
botPosY = [0,0,0,0]
botShiftY1 = random.randint(70,125)
botShiftY2 = random.randint(175,225)
botShiftY = [botShiftY1,botShiftY1,botShiftY2,botShiftY2]
botPeriods = [random.randint(5,15),random.randint(5,15),random.randint(5,15),random.randint(5,15)]
botAmplitudes = [random.randint(5,25),random.randint(5,25),random.randint(5,25),random.randint(5,25)]
botXIncrement = [random.randint(2,5),random.randint(5,8),random.randint(2,5),random.randint(5,8)]
botMoveBack = [False, False, False, False]
botTargPos1 = [random.randint(0,width-100),random.randint(0,width-100),random.randint(0,width-100),random.randint(0,width-100)]
botTargPos2 = [random.randint(0,width-100),random.randint(0,width-100),random.randint(0,width-100),random.randint(0,width-100)]
startingHealth = []
botHealth = []
difficulties = [2,4,6]
gameMode = 0
fullHealth = 0

#sets up lists for files and leaderboard
usernames = []
userscores = []
sortedusernames = []
sorteduserscores = []


#opens files and writes values into a list before the game loop begins
gameUsers = open("gameUsers.txt", "r")
while True:
    #Reading the textfile and removing the new line.
    text = gameUsers.readline()
    text = text.rstrip("\n")
    
    #This is put before so that a blank string doesn't show up at the end of the wordbank.
    if text=="": 
        break 
    #Appends unique words.
    usernames.append(text)
gameUsers.close()

gameScores = open("gameScores.txt", "r")
while True:
    #reading the textfile and removing the new line
    text = gameScores.readline()
    text = text.rstrip("\n")
    
    #this is put before so that a blank string doesn't show up at the end of the wordbank
    if text=="": 
        break 
    #appends unique words
    userscores.append(int(text))
gameScores.close()

#initializes the accumulator variable
scoreSorter = 0 

    
#sets up game loop & clock
myClock = pygame.time.Clock()
running = True
while running:
    #iterates through all game events
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False 
        #these conditionals determine the booleans that enables holding the left/right keys for boat movement
        if evnt.type == pygame.KEYDOWN and playGame:
            if evnt.key == pygame.K_LEFT or evnt.key == pygame.K_a:
                keyLeft = True
            if evnt.key == pygame.K_RIGHT or  evnt.key == pygame.K_d:
                keyRight = True
        if evnt.type == pygame.KEYUP and playGame:
            if evnt.key == pygame.K_LEFT or evnt.key == pygame.K_a:
                keyLeft = False
            if evnt.key == pygame.K_RIGHT or evnt.key == pygame.K_d:
                keyRight = False
        
        #calculates path for user projectile when mouse is clicked
        if nextShot and evnt.type == pygame.MOUSEBUTTONDOWN and playGame: 
            mx, my = pygame.mouse.get_pos()  
            userBulletPosX = boatX+50
            userBulletPosY = boatY              
            drawBullet = True
            nextShot = False
            scale = (mx-userBulletPosX)/(my-userBulletPosY) 
        
        #draws all color pickers for the settings pages        
        if evnt.type == pygame.MOUSEBUTTONDOWN and settingsPage:
            mx, my = pygame.mouse.get_pos()             
            if width//2-213 < mx < width//2+197 and 300 < my < 325:
                BOAT = allColours[(mx-(width//2-213))]            
            elif width//2-263 < mx < width//2-213 and 300 < my < 325:
                BOAT = grayColours[(mx-(width//2-263))]  
                
            if width//2-213 < mx < width//2+197 and 400 < my < 425:
                EYE = allColours[(mx-(width//2-213))]            
            elif width//2-263 < mx < width//2-213 and 400 < my < 425:
                EYE = grayColours[(mx-(width//2-263))]  
                
            if width//2-213 < mx < width//2+197 and 500 < my < 525:
                SKIN = skinColours[(mx-(width//2-213))]        
            elif width//2-263 < mx < width//2-213 and 500 < my < 525:
                SKIN = grayColours[(mx-(width//2-263))]  
                   
        #checks events for textbox input in the gameover page
        keys = pygame.key.get_pressed()  
        if evnt.type == pygame.KEYDOWN and gameOver:
            
            #controls backspace of input
            if (keys[8] or evnt.type == pygame.K_BACKSPACE or evnt.type == pygame.K_DELETE) and playerName != "":
                errorNum = 0
                playerName = playerName[0:len(playerName)-1] 
                
            #ensures there aren't unwanted errors and backspacing stops when playerName is ""
            elif (keys[8] or evnt.type == pygame.K_BACKSPACE or evnt.type == pygame.K_DELETE) and playerName == "":
                errorNum = 0
                playerName = ""
                
            #returns an error when only spaces are entered or nothing is entered
            elif (keys[13] or evnt.type == pygame.K_RETURN) and (playerName == "" or playerName == (str(" "*len(playerName)))):
                errorNum = 1    
            
            #appends playerName to a file along with their score
            elif (keys[13] or evnt.type == pygame.K_RETURN) and (playerName != "" or playerName != (str(" "*len(playerName)))): 
                usernames.append(playerName)
                userscores.append(score)   
                sorteduserscores = []
                sortedusernames = []
                sorting = True
                while sorting:
                    for users in range (len(usernames)):
                        #appends all the least occuring words and then the accumulator increases by one and checks for the next least occuring words
                        if scoreSorter == userscores[users]:
                            sorteduserscores.append(userscores[users])
                            sortedusernames.append(usernames[users])
                        
                    #accumulator used to sort increases by 1        
                    scoreSorter+=1 
                        
                    #breaks the loop and reverses the sorted lists once both lists have been sorted by checking if the same amount of words have been included as in the unsorted list
                    if len(sorteduserscores) == len(userscores):
                        sortedusernames.reverse()
                        sorteduserscores.reverse()
                        
                        #the files are reopened.
                        gameScores = open("gameScores.txt", "w")
                        gameUsers = open("gameUsers.txt", "w")
                        #all the list contents are written into the file for future use
                        for allScores in sorteduserscores:
                            gameScores.write(str(allScores) + "\n")
                        
                        for allUsers in sortedusernames:
                            gameUsers.write(str(allUsers) + "\n")
                            
                        gameScores.close()  
                        gameUsers.close()
                        gameOver = False
                        gameOverPg2 = True
                        sorting = False
               
            #places a character limit   
            elif len(playerName)==15:
                playerName = playerName
                errorNum = 2
            
            #appends the unicode to playerName
            else:
                errorNum = 0
                playerName += evnt.unicode     

    #resets necessary variables when the restartPage boolean is true        
    if restartPage: 
        #for boat-related movement, health, & projectile shots, with preset constants for consistency
        boatX = (width//2)-25
        boatY = 465
        userBulletPosX = 0
        userBulletPosY = 0
        botBulletPosX = 0
        botBulletPosY = 0
        botScale = 0
        boatHealth = 4
        
        #generates periods and amplitudes for all the types of waves in the game
        wavesPeriod = random.randint(3,6)
        wavesAmplitude = random.randint(4,8)
        botWavesAmplitude = random.randint(2,5)
        botWavesPeriod = random.randint(4,8)
        
        #Remembers the page number for the back button. (for reference: menu = 0, rules = 1, settings = 2, leaderboard = 3, playGame = 4,pausePage = 5, gameOverPg2 = 6)
        pageTracker = 0
        
        #intializes score variable
        score = 0
        scoreSorter = 0
        playerName = ""        
        
        #setting up related lists that controls the randomized movement of each robot as well as tracking the health
        botPosX = [0,0,0,0]
        botPosY = [0,0,0,0]
        botShiftY1 = random.randint(70,125)
        botShiftY2 = random.randint(175,225)
        botShiftY = [botShiftY1,botShiftY1,botShiftY2,botShiftY2]
        botPeriods = [random.randint(5,15),random.randint(5,15),random.randint(5,15),random.randint(5,15)]
        botAmplitudes = [random.randint(5,25),random.randint(5,25),random.randint(5,25),random.randint(5,25)]
        botXIncrement = [random.randint(2,5),random.randint(5,8),random.randint(2,5),random.randint(5,8)]
        botMoveBack = [False, False, False, False]
        botTargPos1 = [random.randint(0,width-100),random.randint(0,width-100),random.randint(0,width-100),random.randint(0,width-100)]
        botTargPos2 = [random.randint(0,width-100),random.randint(0,width-100),random.randint(0,width-100),random.randint(0,width-100)]
        difficulties = [2,4,6]
        fullHealth = difficulties[gameMode]
        startingHealth = [fullHealth,fullHealth,fullHealth,fullHealth]
        botHealth = [fullHealth,fullHealth,fullHealth,fullHealth]  
        
        #sets up all the Boolean values that act as "switches"
        keyLeft = False
        keyRight = False
        drawBullet = False
        nextShot = True
        menuPage = False
        settingsPage = False
        drawBotBullet = True
        nextBotShot = False
        nextWave = True
        gameOver = False
        gameOverPg2 = False
        pausePage = False 
        playGame = True
        restartPage = False
        leaderboardPage = False 
        rulesPage = False
    
    #main gameplay boolean; moves good guy, moves bad guy, checks for interactions     
    if playGame:   
        
        #moves boat accordingly (good guy movement)
        if keyLeft == True and boatX != 0 and playGame:
            boatX = boatX - 5
        if keyRight == True and boatX <= width-50 and playGame:
            boatX = boatX + 5
            
        #this set of code handles determining the movement of each individual bot (bad guy movement)
        for eachBot in range(len(botPosX)): 
            if not botMoveBack[eachBot]:
                #generates the fully randomized sine movement of each individual bot
                botPosX[eachBot]+=botXIncrement[eachBot]
                botPosY[eachBot] = botAmplitudes[eachBot]*math.sin(botPosX[eachBot]/botPeriods[eachBot])+botShiftY[eachBot]
                
                #bot moves back when it reaches the end
                if botPosX[eachBot] >= width:
                    botMoveBack[eachBot] = True   
                
            if botMoveBack[eachBot]:
                #generates a second fully randomized sine movement of each individual bot                
                botPosX[eachBot]-=botXIncrement[eachBot]
                botPosY[eachBot] = botAmplitudes[eachBot]*math.sin(botPosX[eachBot]/botPeriods[eachBot])+botShiftY[eachBot]
                
                #bot moves back when it reaches the end                
                if botPosX[eachBot] == 0:
                    botMoveBack[eachBot] = False  
        
        #randomized AI projectile shooting of each bot                 
        for eachBot in range(len(botPosX)):
            
            #1 in 150 chance of the bot shooting a projectile (not actually a lot with continuous iteration)
            if eachBot == random.randint(0,150) and nextBotShot and botHealth[eachBot]>0:
                botBulletPosX = botPosX[eachBot]
                botBulletPosY = botPosY[eachBot]  
                drawBotBullet = True
                nextBotShot = False
                
                #determines the scale based on the target position which is the center of the boat
                botScale = (botBulletPosX-(boatX+31))/(botBulletPosY-(boatY+30))
        
        #when true, the speed (change in position) of the AI projeciles is determined based on the difficulty     
        if drawBotBullet:
            botBulletPosX+=difficulties[gameMode]*1.5*(botScale)
            botBulletPosY+=difficulties[gameMode]*1.5
            if botBulletPosX >= width or botBulletPosX <= 0 or botBulletPosY >= height:
                drawBotBullet = False
                nextBotShot = True #gets ready for the next shot
     
        #projectile shooting of boat                        
        if drawBullet:
            userBulletPosX-=6*(scale)
            userBulletPosY-=6
            if userBulletPosX >= width or userBulletPosX <= 0 or userBulletPosY <= 0:
                drawBullet = False
                nextShot = True #gets ready for the next shot
                userBulletPosX = boatX+25
                userBulletPosY = boatY  
       
        #checks collisions for each bot using related lists  
        for eachCollision in range(len(botPosX)):
            botXCollCoords = [botPosX[eachCollision]-20,botPosX[eachCollision]-10,botPosX[eachCollision],botPosX[eachCollision]+10,botPosX[eachCollision]+20,botPosX[eachCollision]+30,botPosX[eachCollision]+40,botPosX[eachCollision]+47,botPosX[eachCollision]-15,botPosX[eachCollision]-5,botPosX[eachCollision]+5,botPosX[eachCollision]+15,botPosX[eachCollision]+25,botPosX[eachCollision]+35,botPosX[eachCollision]+45,botPosX[eachCollision]-12,botPosX[eachCollision]+52,botPosX[eachCollision],botPosX[eachCollision]+40,botPosX[eachCollision]+5,botPosX[eachCollision]+35,botPosX[eachCollision]+15]
            botYCollCoords = [botPosY[eachCollision]+45,botPosY[eachCollision]+45,botPosY[eachCollision]+45,botPosY[eachCollision]+45,botPosY[eachCollision]+45,botPosY[eachCollision]+45,botPosY[eachCollision]+45,botPosY[eachCollision]+45,botPosY[eachCollision]+30,botPosY[eachCollision]+30,botPosY[eachCollision]+30,botPosY[eachCollision]+30,botPosY[eachCollision]+30,botPosY[eachCollision]+30,botPosY[eachCollision]+30,botPosY[eachCollision]+10,botPosY[eachCollision]+10,botPosY[eachCollision],botPosY[eachCollision],botPosY[eachCollision]-25,botPosY[eachCollision]-25,botPosY[eachCollision]-35]
            
            #checks for collisions based on related lists of all important x/y coordinates mapped out. using a distance formula, if the distance is lower than the radius, the projectile has collided                    
            for allCoords in range(len(botXCollCoords)):
                if (math.sqrt((userBulletPosX - (botXCollCoords[allCoords])) ** 2 + (userBulletPosY - (botYCollCoords[allCoords])) ** 2)) < 10:
                    botHealth[eachCollision]-=1 #subtracts health from the corresponding bot
                    #resets boat projectile coords and booleans
                    drawBullet = False
                    nextShot = True
                    userBulletPosX = boatX+25
                    userBulletPosY = boatY                
        
        #list that contains all collision points of the boat, mapped out               
        boatXCollCoords = [boatX+5,boatX+15,boatX+25,boatX+30,boatX+35,boatX+40,boatX+45,boatX+50,boatX+55,boatX-1,boatX+62,boatX,boatX+61,boatX,boatX+10,boatX+15,boatX+20,boatX+30,boatX+40,boatX+50,boatX+55,boatX+60]
        boatYCollCoords = [491,482,473,465,470,475,480,485,491,517,517,510,510,530,560,590,590,590,590,590,560,530]   
        
        #checks for collisions based on the related lists, using the distance formula
        for eachCollision in range(len(boatXCollCoords)):
            if math.sqrt((botBulletPosX - (boatXCollCoords[eachCollision])) ** 2 + (botBulletPosY - (boatYCollCoords[eachCollision])) ** 2) < 10:  
                boatHealth -=1 #subtracts health from the boat
                #resets bot projectile coords and booleans
                drawBotBullet = False
                nextBotShot = True 
                botBulletPosX = 0
                botBulletPosY = 0
                        
        #handles collision & appropriately updating health bars and scores
        for eachBot in range(len(botPosX)):         
            #after the first collision, the bot is moved out of the pygame window so more collisions are not accidentally counted
            if botHealth[eachBot]<=0:
                botPosX[eachBot] = 1000
                botPosY[eachBot] = 300
            
            #when a bot dies, score increases by 1                             
            if botHealth[eachBot]==0:
                score += 1
                botHealth[eachBot]-=1                               
                        
        #when each wave is completed, the bots pos is reset and health increases by 1. waves make the game more challenging over time. 
        for eachBot in range(len(botPosX)):  
            if botPosX[eachBot] > width and score%4 == 0 and score>0:
                screen.fill(WATER)
                startingHealth[eachBot] = startingHealth[eachBot]+1
                botHealth[eachBot] = startingHealth[eachBot]
                botPosX[eachBot] = 0
                botPosY[eachBot] = 0 
                botMoveBack[eachBot]=False
                                  
        
        #when the boat dies, the game ends and the gameOver boolean becomes true    
        if boatHealth <= 0:
            playGame = False
            gameOver = True
            
        
    
    #draws all elements
    
    #calls the colors again based on the UI look selected
    if darkMode:
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        MAINUI = (24, 24, 24)
        TEXTBOX = (95, 108, 110)
        WATER = (72, 130, 122)
        UI1 = (108, 171, 162)
        UI2 = (21, 99, 89)
        WAVES = (18, 74, 66)
        USERPROJ1 = (245,149,66)
        USERPROJ2 = (199,116,44)
        BOTPROJ1 = (227, 104, 104)
        BOTPROJ2 = (166, 75, 75)        
        WINDOW = (161, 198, 227)
        BOT1 = (85, 87, 101)
        RED = (255,0,0)        
        GRAY = (85,92,105)
        GREEN = (0,255,0)
        GRAY2 = (87, 99, 94)        
    if not darkMode:
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        MAINUI = (169, 209, 208)
        TEXTBOX = (186, 214, 219)        
        WATER = (94, 184, 172)
        UI1 = (73, 186, 175)
        UI2 = (28, 128, 118)
        WAVES = (39, 115, 105)
        USERPROJ1 = (245,149,66)
        USERPROJ2 = (199,116,44)
        BOTPROJ1 = (227, 104, 104)
        BOTPROJ2 = (166, 75, 75)        
        GRAY = (85,92,105)
        WINDOW = (161, 198, 227)
        BOT1 = (85, 87, 101)
        RED = (255,0,0) 
        GREEN = (0,255,0)
        GRAY2 = (87, 99, 94)        
    
    #draws menu page when True    
    if menuPage:   
        
        #pageTracker is used for back buttons
        pageTracker = 0
        screen.fill(MAINUI)
        mx, my = pygame.mouse.get_pos()
        
        #draws all buttons
        easyMode = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,195,100,75))
        mediumMode = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-50,195,100,75))
        hardMode = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)+75,195,100,75))
        rules = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,295,350,75))  
        settings = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,395,350,75)) 
        
        
        #renders and loads all media elements
        titleShadow = titleFont.render("Nautical Assault" , 1, UI2)
        titleMain = titleFont.render("Nautical Assault" , 1, UI1)
        easyText = bodyFont.render("EASY" , 1, UI2)
        mediumText = bodyFont.render("MEDIUM" , 1, UI2)
        hardText = bodyFont.render("HARD" , 1, UI2)
        rulesText = bodyFont2.render("HOW TO PLAY",1,UI2)
        settingsText = bodyFont2.render("SETTINGS",1,UI2)
            
        
        #blits all media elements
        screen.blit(titleShadow, pygame.Rect(70,55,400,100))   
        screen.blit(titleMain, pygame.Rect(75,50,400,100))  
        screen.blit(easyText, pygame.Rect((width//2)-155,220,100,75))   
        screen.blit(mediumText, pygame.Rect((width//2)-47,220,100,75)) 
        screen.blit(hardText, pygame.Rect((width//2)+93,220,100,75))   
        screen.blit(rulesText, pygame.Rect((width//2)-125,308,100,75)) 
        screen.blit(settingsText, pygame.Rect((width//2)-90,408,100,75))          


               
        
        #checks for collisions for all buttons
        if easyMode.collidepoint(mx,my):
            pygame.draw.rect(screen, UI2, pygame.Rect((width//2)-185,185,120,95)) 
            easyText = bodyFont1.render("EASY" , 1, UI1)
            screen.blit(easyText, pygame.Rect((width//2)-160,215,90,95))
            
            #when clicked, the appropriate difficulty values are determined as well as booleans
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                gameMode = 0
                fullHealth = difficulties[gameMode]
                startingHealth = [fullHealth,fullHealth,fullHealth,fullHealth]
                botHealth = [fullHealth,fullHealth,fullHealth,fullHealth]  
                restartPage = True
                playGame = True 
                gameOver = False
                gameOverPg2 = False
                menuPage = False
    
        elif mediumMode.collidepoint(mx,my):
            pygame.draw.rect(screen, UI2, pygame.Rect((width//2)-60,185,120,95)) 
            easyText = bodyFont1.render("MEDIUM" , 1, UI1)
            screen.blit(easyText, pygame.Rect((width//2)-57,215,120,95))
            
            #when clicked, the appropriate difficulty values are determined as well as booleans            
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                gameMode = 1
                fullHealth = difficulties[gameMode]
                startingHealth = [fullHealth,fullHealth,fullHealth,fullHealth]
                botHealth = [fullHealth,fullHealth,fullHealth,fullHealth]  
                restartPage = True
                playGame = True 
                gameOver = False
                gameOverPg2 = False
                menuPage = False
                
        elif hardMode.collidepoint(mx,my):
            pygame.draw.rect(screen, UI2, pygame.Rect((width//2)+65,185,120,95)) 
            easyText = bodyFont1.render("HARD" , 1, UI1)
            screen.blit(easyText, pygame.Rect((width//2)+85,215,120,95)) 
            
            #when clicked, the appropriate difficulty values are determined as well as booleans            
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                gameMode = 2
                fullHealth = difficulties[gameMode]
                startingHealth = [fullHealth,fullHealth,fullHealth,fullHealth]
                botHealth = [fullHealth,fullHealth,fullHealth,fullHealth]    
                restartPage = True
                playGame = True 
                gameOver = False
                gameOverPg2 = False
                menuPage = False          

        elif rules.collidepoint(mx,my):
            pygame.draw.rect(screen,UI2, pygame.Rect((width//2)-185,285,370,95))
            rulesText = bodyFont3.render("HOW TO PLAY" , 1, UI1)
            screen.blit(rulesText, pygame.Rect((width//2)-145,305,370,95))  
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                rulesPage = True
                menuPage = False            

        elif settings.collidepoint(mx,my):
            pygame.draw.rect(screen,UI2, pygame.Rect((width//2)-185,385,370,95))
            settingsText = bodyFont3.render("SETTINGS" , 1, UI1)
            screen.blit(settingsText, pygame.Rect((width//2)-100,405,370,95)) 
            
            #when clicked, the appropriate difficulty values are determined as well as booleans            
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                settingsPage = True
                menuPage = False
                
    if rulesPage:
        mx, my = pygame.mouse.get_pos()        
        
        #shows the correct image file based on UI look
        if not darkMode:
            rulesPic = pygame.image.load("howtoplayLight.png")
            screen.blit(rulesPic,pygame.Rect(0,0,800,600))
        elif darkMode:
            rulesPic = pygame.image.load("howtoplayDark.png")
            screen.blit(rulesPic,pygame.Rect(0,0,800,600)) 
            
        #renders and loads all media elements
        rBack = pygame.draw.rect(screen, UI1,pygame.Rect(10,10,100,40))
        rBackText = (bodyFont1.render("BACK", 1, UI2))
        
        #blits all media elements
        screen.blit(rBackText, pygame.Rect(23,12,100,40))           
            
        if rBack.collidepoint(mx,my):
                    rBack = pygame.draw.rect(screen, UI2,pygame.Rect(10,10,100,40))
                    rBackText = (bodyFont1.render("BACK", 1, UI1))
                    screen.blit(rBackText, pygame.Rect(23,12,100,40))
                    if evnt.type == pygame.MOUSEBUTTONDOWN:
                        if pageTracker == 0:
                            rulesPage = False
                            menuPage = True          
        

    #draws settings page when True            
    if settingsPage:
        screen.fill(MAINUI)
        mx, my = pygame.mouse.get_pos()
        
        #renders and loads all media elements
        sBack = pygame.draw.rect(screen, UI1,pygame.Rect(10,10,100,40))
        settingsShadow = titleFont.render("SETTINGS" , 1, UI2)
        settingsMain = titleFont.render("SETTINGS" , 1, UI1)
        UItext = bodyFont1.render("DARK MODE:", 1, UI2)
        bColourtext = bodyFont1.render("BOAT COLOUR", 1, UI2)
        eColourtext = bodyFont1.render("EYE COLOUR", 1, UI2)
        sColourtext = bodyFont1.render("SKIN COLOUR", 1, UI2)
        sBackText = (bodyFont1.render("BACK", 1, UI2))
        
        #blits all media elements
        screen.blit(settingsShadow, pygame.Rect(210,25,400,100))   
        screen.blit(settingsMain, pygame.Rect(215,20,400,100))
        screen.blit(UItext, pygame.Rect(260,180,400,100))
        screen.blit(bColourtext, pygame.Rect(300,245,400,100))   
        screen.blit(eColourtext, pygame.Rect(312,345,400,100)) 
        screen.blit(sColourtext, pygame.Rect(300,445,400,100))
        screen.blit(sBackText, pygame.Rect(23,12,100,40))   
        
        if sBack.collidepoint(mx,my):
            sBack = pygame.draw.rect(screen, UI2,pygame.Rect(10,10,100,40))
            sBackText = (bodyFont1.render("BACK", 1, UI1))
            screen.blit(sBackText, pygame.Rect(23,12,100,40))
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                if pageTracker == 0:
                    settingsPage = False
                    menuPage = True
                if pageTracker == 2:
                    playGame = True
                    pausePage = True
                    settingsPage = False
                if pageTracker == 3:
                    gameOverPg2 = True
                    settingsPage = False
        

        #calls the colour picker functions and draws a rect that displays the selected colour
        colourPicker(300)
        pygame.draw.rect(screen,BOAT,pygame.Rect(width//2+207,300,50,25))      
        colourPicker(400)
        pygame.draw.rect(screen,EYE,pygame.Rect(width//2+207,400,50,25))    
        skinColourPicker(500)
        pygame.draw.rect(screen,SKIN,pygame.Rect(width//2+207,500,50,25))
        
        #changes the switch design based on the selected UI look
        if darkMode:
            pygame.draw.rect(screen,MAINUI, pygame.Rect((width//2)+45,180,105,50))
            lightButton = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)+45,180,55,40))
            darkButton = pygame.draw.rect(screen, UI2, pygame.Rect((width//2)+100,185,50,30)) 
            lightText = bodyFont.render("ON", 1, UI2)
            darkText = bodyFont4.render("OFF", 1, UI1)  
            screen.blit(lightText, pygame.Rect((width//2)+55,185,55,40))
            screen.blit(darkText, pygame.Rect((width//2)+110,190,50,30))
        elif not darkMode:
            pygame.draw.rect(screen, MAINUI, pygame.Rect((width//2)+45,180,105,50))
            lightButton = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)+50,185,50,30))
            darkButton = pygame.draw.rect(screen, UI2, pygame.Rect((width//2)+95,180,55,40))
            lightText = bodyFont4.render("ON", 1, UI2)
            darkText = bodyFont.render("OFF", 1, UI1)
            screen.blit(lightText, pygame.Rect((width//2)+63,190,55,40))
            screen.blit(darkText, pygame.Rect((width//2)+100,185,50,30))    

        #checks for collision of the UI look switch.
        if lightButton.collidepoint(mx,my):
            pygame.draw.rect(screen, MAINUI, pygame.Rect((width//2)+45,180,105,50))
            lightButton = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)+45,180,55,40))
            darkButton = pygame.draw.rect(screen, UI2, pygame.Rect((width//2)+100,185,50,30))
            lightText = bodyFont.render("ON", 1, UI2)
            darkText = bodyFont4.render("OFF", 1, UI1)
            screen.blit(lightText, pygame.Rect((width//2)+55,185,55,40))
            screen.blit(darkText, pygame.Rect((width//2)+110,190,50,30))
            
            #when clicked, UI changes to dark mode
            if evnt.type == pygame.MOUSEBUTTONDOWN:                          
                darkMode = True    
        elif darkButton.collidepoint(mx,my):
            pygame.draw.rect(screen, MAINUI, pygame.Rect((width//2)+45,180,105,50))
            lightButton = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)+50,185,50,30))
            darkButton = pygame.draw.rect(screen, UI2, pygame.Rect((width//2)+95,180,55,40))
            lightText = bodyFont4.render("ON", 1, UI2)
            darkText = bodyFont.render("OFF", 1, UI1)
            screen.blit(lightText, pygame.Rect((width//2)+63,190,55,40))
            screen.blit(darkText, pygame.Rect((width//2)+100,185,50,30))  
            
            #when clicked, UI changes to light mode
            if evnt.type == pygame.MOUSEBUTTONDOWN:                              
                darkMode = False 
                
        #goes back to the previous page based on the value of pageTracker       
        elif sBack.collidepoint(mx,my):
            sBack = pygame.draw.rect(screen, UI2,pygame.Rect(10,10,100,40))
            sBackText = (bodyFont1.render("BACK", 1, UI1))
            screen.blit(sBackText, pygame.Rect(23,12,100,40))
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                if pageTracker == 0:
                    settingsPage = False
                    menuPage = True
                if pageTracker == 2:
                    playGame = True
                    pausePage = True
                    settingsPage = False
                if pageTracker == 3:
                    gameOverPg2 = True
                    settingsPage = False
                    
    #draws game when True   
    if playGame:
        mx, my = pygame.mouse.get_pos()
        
        #draws different boat designs based on user input
        if keyLeft == True and boatX != 0:
            drawBoatLeft(boatX)
        elif keyRight == True and boatX <= width-50:
            drawBoatRight(boatX)
        else:
            drawBoat(boatX)
        
        #draws health bars of bots          
        for healthBar in range(len(botHealth)):
            pygame.draw.rect(screen,GRAY2,pygame.Rect(botPosX[healthBar]-12,botPosY[healthBar]-62,64,11))  
            pygame.draw.rect(screen,GREEN,pygame.Rect(botPosX[healthBar]-10,botPosY[healthBar]-60,60*botHealth[healthBar]/startingHealth[healthBar],7))
        
        #draws health bar of boat; division by 4 because the boat health stays constant throughout all modes, after testing, I don't plan to change the health, unlike with the bots
        pygame.draw.rect(screen,GRAY2,pygame.Rect(boatX-2,boatY-25,64,11))  
        pygame.draw.rect(screen,GREEN,pygame.Rect(boatX,boatY-23,60*boatHealth/4,7))            
            
        #draws different bot designs based on direction (waves)
        for eachBot in range(len(botPosX)):
            if not botMoveBack[eachBot] and botHealth[eachBot]>0:
                    drawBot(screen,(botPosX[eachBot]),(botPosY[eachBot]))
                    for waves in range (random.randint(40,70)):
                        wavesX = (botPosX[eachBot]-waves)
                        wavesY1 = botWavesAmplitude*math.sin(wavesX/wavesPeriod)+botShiftY[eachBot]+5 
                        pygame.draw.circle(screen, WAVES,(wavesX,wavesY1),1)                
                    
            elif botMoveBack[eachBot] and botHealth[eachBot]>0:
                    drawBot(screen,(botPosX[eachBot]),(botPosY[eachBot]))   
                    for waves in range (random.randint(40,70)):
                        wavesX = (botPosX[eachBot]+30+waves)
                        wavesY1 = botWavesAmplitude*math.sin(wavesX/botWavesPeriod)+botShiftY[eachBot]+5 
                        pygame.draw.circle(screen, WAVES,(wavesX,wavesY1),1)  
                        
        #handles the position and display of the score counter 
        scoreText = (bodyFont2.render(str(score), 1, UI2)) 
        pygame.draw.rect(screen,GRAY2,pygame.Rect(765,15,40,40))
        pygame.draw.polygon(screen,GRAY2,[[610,0],[650,40],[800,40],[800,0]])            
        pygame.draw.circle(screen,GRAY2,(765,25),30)
        if score<10: 
            screen.blit(scoreText, pygame.Rect(760,0,50,30))                 
        elif score>=10:
            screen.blit(scoreText, pygame.Rect(750,0,50,30))     
                
        #draws projectiles
        if drawBullet:
            userProjectile(screen,userBulletPosX,userBulletPosY)    
 
        if drawBotBullet:
            botProjectile(screen,botBulletPosX,botBulletPosY)    
        
        #draws the pause button and checks for collision
        pauseButton = pygame.draw.rect(screen,GRAY2,pygame.Rect(705,7,22,26))          
        pygame.draw.rect(screen,UI2,pygame.Rect(705,7,9,26))
        pygame.draw.rect(screen,UI2,pygame.Rect(718,7,9,26))
        if pauseButton.collidepoint(mx,my):               
            pygame.draw.rect(screen,UI1,pygame.Rect(705,7,9,26))
            pygame.draw.rect(screen,UI1,pygame.Rect(718,7,9,26))
            
            #game is paused, the pause menu appears
            if evnt.type == pygame.MOUSEBUTTONDOWN:    
                playGame = False
                pausePage = True  
        
        #draws the restart button and checks for collision
        restartButton = pygame.draw.rect(screen,GRAY2, pygame.Rect(665,7,22,26))
        pygame.draw.circle(screen,UI2,(676,20),14,7)
        pygame.draw.polygon(screen,GRAY2,[[662,19],[676,15],[662,33]])
        pygame.draw.polygon(screen,UI2,[[660,14],[662,23],[670,19]])
        if restartButton.collidepoint(mx,my):                          
            pygame.draw.circle(screen,UI1,(676,20),14,7)
            pygame.draw.polygon(screen,GRAY2,[[662,19],[676,15],[662,33]])
            pygame.draw.polygon(screen,UI1,[[660,14],[662,23],[670,19]])
            
            #game is reset, restart page becomes True
            if evnt.type == pygame.MOUSEBUTTONDOWN:  
                restartPage = True 
                menuPage = False
                playGame = False 
    
    #draws the pause menu when True            
    if pausePage: 
        #when other buttons are clicked, no matter what, this ensures playGame stays false until it becomes True through collision
        playGame = False
        mx, my = pygame.mouse.get_pos() 
        
        #draws popup menu window
        pygame.draw.circle(screen,MAINUI,(width//2-175,125),30)
        pygame.draw.circle(screen,MAINUI,(width//2-175,500),30)
        pygame.draw.circle(screen,MAINUI,(width//2+175,125),30)
        pygame.draw.circle(screen,MAINUI,(width//2+175,500),30)
        pygame.draw.rect(screen,MAINUI,pygame.Rect(width//2-175,95,350,435))
        pygame.draw.rect(screen,MAINUI,pygame.Rect(width//2-205,125,410,375))
        
        #draws each button
        resume = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,125,350,75))
        restart = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,225,350,75))
        menu = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,325,350,75))        
        settings = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,425,350,75)) 
        
        #renders and loads all media elements
        resumeText = bodyFont2.render("RESUME" , 1, UI2)
        restartText = bodyFont2.render("RESTART" , 1, UI2)
        menuText = bodyFont2.render("MENU",1,UI2)
        settingsText = bodyFont2.render("SETTINGS",1,UI2)
        
        #blits all media elements
        screen.blit(resumeText, pygame.Rect((width//2)-70,138,100,75))   
        screen.blit(restartText, pygame.Rect((width//2)-75,238,100,75)) 
        screen.blit(menuText, pygame.Rect((width//2)-50,338,100,75)) 
        screen.blit(settingsText, pygame.Rect((width//2)-85,438,100,75))          
        
        #checks collision for all buttons
        if resume.collidepoint(mx,my):                          
            pygame.draw.rect(screen, UI2, pygame.Rect((width//2)-175,125,350,75))
            resumeText = bodyFont2.render("RESUME" , 1, UI1)
            screen.blit(resumeText, pygame.Rect((width//2)-70,138,100,75)) 
            
            #game resumes when clicked
            if evnt.type == pygame.MOUSEBUTTONDOWN:  
                pausePage = False
                playGame = True            
                
        elif restart.collidepoint(mx,my):
            pygame.draw.rect(screen, UI2, pygame.Rect((width//2)-175,225,350,75))
            restartText = bodyFont2.render("RESTART" , 1, UI1)
            screen.blit(restartText, pygame.Rect((width//2)-75,238,100,75))  
            
            #game resets when clicked
            if evnt.type == pygame.MOUSEBUTTONDOWN: 
                restartPage = True 
                menuPage = False
                pausePage = False

        elif menu.collidepoint(mx,my):
            pygame.draw.rect(screen, UI2, pygame.Rect((width//2)-175,325,350,75))        
            menuText = bodyFont2.render("MENU",1,UI1)
            screen.blit(menuText, pygame.Rect((width//2)-50,338,100,75)) 
            
            #menu page is drawn when clicked
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                pausePage = False
                menuPage = True               
        
        elif settings.collidepoint(mx,my):
            pygame.draw.rect(screen, UI2, pygame.Rect((width//2)-175,425,350,75)) 
            settingsText = bodyFont2.render("SETTINGS",1,UI1)
            screen.blit(settingsText, pygame.Rect((width//2)-85,438,100,75))   
            
            #settings page is drawn when clicked
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                settingsPage = True
                pausePage = False        
                pageTracker = 2
        
        #playButton = pygame.draw.rect(screen,GRAY,pygame.Rect(705,7,22,26))
        #pygame.draw.polygon(screen,UI2,[[705,20],[727,7],[727,33]])        
        #if playButton.collidepoint(mx,my):
            #pygame.draw.polygon(screen,UI1,[[705,20],[727,7],[727,33]]) 
            #if evnt.type == pygame.MOUSEBUTTONDOWN:
                #pausePage = False
                #playGame = True
                                   
    #draws when the game ends        
    if gameOver:
        mx, my = pygame.mouse.get_pos() 
        screen.fill(MAINUI)
        
        #renders and loads all media elements
        gameOverShadow = titleFont.render("GAME OVER!" , 1, UI2)
        gameOverMain = titleFont.render("GAME OVER!" , 1, UI1) 
        finalScore = bodyFont3.render("YOUR SCORE: "+str(score),1,UI1)
        userPromptText = bodyFont2.render("ENTER USERNAME",1,UI1)  
        userPromptInfoText = miniFont.render("Please Enter 1-15 Characters. Hit Enter when done.",1,UI1)
        
        #blits all media elements
        screen.blit(gameOverShadow, pygame.Rect(157,25,400,100))   
        screen.blit(gameOverMain, pygame.Rect(162,20,400,100))   
        screen.blit(finalScore, pygame.Rect(235,150,400,100))
        screen.blit(userPromptText, pygame.Rect(240,225,400,100))     
        screen.blit(userPromptInfoText, pygame.Rect(238,275,400,100))        
        
        #draws the textbox
        pygame.draw.rect(screen, TEXTBOX, pygame.Rect(220,310,370,50))
        #draws the dispay of user-inputted text
        playerNameDisplay = bodyFont.render(playerName,1,UI2)
        screen.blit(playerNameDisplay,pygame.Rect(240,320,100,100))                
        
        #displays errors for the textbox if needed
        if errorNum == 0:
            errorDisplay = miniFont.render("Characters: "+str(len(playerName))+"/15",1,RED)
            screen.blit(errorDisplay,pygame.Rect(350,370,100,100))                                        
        elif errorNum == 1:
            errorDisplay = miniFont.render("ERROR: Please enter at least ONE character. Do not put all spaces -- it won't work :D.",1,RED)
            screen.blit(errorDisplay,pygame.Rect(125,370,100,100))                            
        elif errorNum == 2:
            errorDisplay = miniFont.render("Max Characters (15) Reached. Anything further is not being registered",1,RED)
            screen.blit(errorDisplay,pygame.Rect(180,370,100,100))                            
            
                
    if gameOverPg2:
        mx, my = pygame.mouse.get_pos() 
        screen.fill(MAINUI)
        replay = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,100,350,75))  
        menu = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,200,350,75))  
        leaderboard = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,300,350,75))  
        settings = pygame.draw.rect(screen, UI1, pygame.Rect((width//2)-175,400,350,75))  
        
        #renders and loads all media elements
        replayText = bodyFont2.render("PLAY AGAIN" , 1, UI2)
        menuText = bodyFont2.render("MENU" , 1, UI2)
        leaderboardText = bodyFont2.render("LEADERBOARD" , 1, UI2)
        settingsText = bodyFont2.render("SETTINGS",1,UI2)

        #blits all media elements
        screen.blit(replayText, pygame.Rect((width//2)-100,113,100,75))   
        screen.blit(menuText, pygame.Rect((width//2)-47,213,100,75)) 
        screen.blit(leaderboardText, pygame.Rect((width//2)-130,313,100,75))   
        screen.blit(settingsText, pygame.Rect((width//2)-95,413,100,75))          
        
        #checks for collision and changes boolean values accordingly 
        if replay.collidepoint(mx,my):
            pygame.draw.rect(screen, UI2, pygame.Rect((width//2)-185,90,370,95))  
            replayText = bodyFont3.render("PLAY AGAIN" , 1, UI1)
            screen.blit(replayText, pygame.Rect((width//2)-120,110,120,95))
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                restartPage = True
                gameOverPg2 = False
    
        elif menu.collidepoint(mx,my):
            pygame.draw.rect(screen, UI2, pygame.Rect((width//2)-185,190,370,95))              
            menuText = bodyFont3.render("MENU" , 1, UI1)
            screen.blit(menuText, pygame.Rect((width//2)-57,210,120,95))
            if evnt.type == pygame.MOUSEBUTTONDOWN: 
                menuPage = True
                playGame = False
                gameOver = False
                gameOverPg2 = False            
                
        elif leaderboard.collidepoint(mx,my):
            pygame.draw.rect(screen,UI2, pygame.Rect((width//2)-185,290,370,95))
            leaderboardText = bodyFont3.render("LEADERBOARD" , 1, UI1)
            screen.blit(leaderboardText, pygame.Rect((width//2)-150,310,370,95))    
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                leaderboardPage = True
                pageTracker = 3
                gameOverPg2 = False                    
        
        elif settings.collidepoint(mx,my):
            pygame.draw.rect(screen,UI2, pygame.Rect((width//2)-185,390,370,95))
            settingsText = bodyFont3.render("SETTINGS" , 1, UI1)
            screen.blit(settingsText, pygame.Rect((width//2)-95,410,370,95)) 
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                settingsPage = True
                pageTracker = 3
                gameOverPg2 = False  
                
    if leaderboardPage:
        mx, my = pygame.mouse.get_pos() 
        screen.fill(MAINUI)
        
        #renders and loads all media
        lbBack = pygame.draw.rect(screen, UI1,pygame.Rect(10,10,100,40))
        lbShadow = titleFont.render("LEADERBOARD" , 1, UI2)
        lbMain = titleFont.render("LEADERBOARD" , 1, UI1) 
        sBackText = (bodyFont1.render("BACK", 1, UI2))        
        #blits all media elements
        screen.blit(lbShadow, pygame.Rect(127,15,400,100))   
        screen.blit(lbMain, pygame.Rect(132,10,400,100)) 
        screen.blit(sBackText, pygame.Rect(23,12,100,40))   
        
        if lbBack.collidepoint(mx,my):
            lbBack = pygame.draw.rect(screen, UI2,pygame.Rect(10,10,100,40))
            lbBackText = (bodyFont1.render("BACK", 1, UI1))
            screen.blit(lbBackText, pygame.Rect(23,12,100,40))
            if evnt.type == pygame.MOUSEBUTTONDOWN:
                if pageTracker == 0:
                    menuPage = True                    
                    leaderboardPage = False
                elif pageTracker == 3:
                    gameOverPg2 = True
                    leaderboardPage = False        
        
        #draws the leaderboard from first to third place
        count = 1  
        for eachusername in range (len(sortedusernames[:3])):
            if count == 1:
                ranklb = bodyFont.render("#"+str(count),1,GOLDOUTLINE)
                pygame.draw.circle(screen,GOLD,(count*width//3-135,150),25)
            elif count == 2:
                ranklb = bodyFont.render("#"+str(count),1,SILVEROUTLINE)   
                pygame.draw.circle(screen,SILVER,(count*width//3-135,150),25)
            elif count == 3:
                ranklb = bodyFont.render("#"+str(count),1,BRONZEOUTLINE)     
                pygame.draw.circle(screen,BRONZE,(count*width//3-135,150),25)
                
            usernamelb = bodyFont2.render(str(sortedusernames[eachusername]),1,UI2)
            userscorelb = miniFont.render("Bots Killed: " + str(sorteduserscores[eachusername]),1,UI2) 
            screen.blit(ranklb, pygame.Rect((count*width//3)-150,133,400,100))              
            pygame.draw.rect(screen,UI1,pygame.Rect(count*width//3-255,180,240,50))
            screen.blit(usernamelb, pygame.Rect((count*width//3)-250,180,400,100))
            screen.blit(userscorelb, pygame.Rect((count*width//3)-180,230,400,100)) 
            count+=1
        
        pygame.draw.circle(screen,TEXTBOX,(190,300),30)
        pygame.draw.circle(screen,TEXTBOX,(650,300),30)
        pygame.draw.circle(screen,TEXTBOX,(190,560),30)
        pygame.draw.circle(screen,TEXTBOX,(650,560),30)
        pygame.draw.rect(screen,TEXTBOX, pygame.Rect(160,290,520,270))
        pygame.draw.rect(screen,TEXTBOX, pygame.Rect(200,270,460,320))    
        
        #draws the leaderboard from place 4-10
        yshift = 0
        count = 4         
        
        if len(sortedusernames)>=4:
            for eachusername in range (3,len(sortedusernames)):
                if eachusername<=10:
                    ranklb = bodyFont.render("#"+str(count),1,UI2)
                    usernamelb = bodyFont.render(str(sortedusernames[eachusername]),1,UI2)
                    userscorelb = bodyFont.render(str(sorteduserscores[eachusername]),1,UI2)
                    screen.blit(ranklb, pygame.Rect(180,295+yshift,400,100))                                    
                    screen.blit(usernamelb, pygame.Rect(255,295+yshift,400,100))
                    screen.blit(userscorelb, pygame.Rect(605,295+yshift,400,100))   
                    yshift += 40
                    count +=1
            
            
        
                    
    pygame.display.flip()
    myClock.tick(60)
    
pygame.quit()     
        
