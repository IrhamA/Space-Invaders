from tkinter import *
from math import *  
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=1000, height=1000, background="black")


def setInitialValues():
        global score, xStation, yStation, xPlayer, yPlayer, xSpeed, ySpeed, playerImage
        global xMouse, yMouse, xSpeed, ySpeed, playerDrawing, playerImageFiles, missileSpeed
        global mouseAngle,  missile, xMissile, yMissile
        global xMissileSpeed, yMissileSpeed, alien1ImageFiles, alien2ImageFiles, alien3ImageFiles 
        global xEnemy1, yEnemy1, xEnemy2, yEnemy2, xEnemy3, yEnemy3, alien1Drawing, alien2Drawing
        global alien3Drawing, whichAlien, xEnemy4, yEnemy4, alien4Drawing, alien4ImageFiles, speedEnemy, numEnemiesPerFrame
        global  alien1Alive, alien2Alive, alien3Alive, alien4Alive
        global hits, fire, fireTimer

        fire = []
        fireTimer = []

        hits = 0 
        for r in range (300):
                starX = randint(0,1000)
                starY = randint(0,1000)
                size = randint (0,4)
                colourChoice = choice(["white", "#FF004F", "yellow", "orange", "white"])
                screen.create_oval(starX,starY,starX+size,starY+size, fill = colourChoice)

        screen.create_oval(620,500,1410,1500, fill = "#f46b42")


                
        score = 0
        xStation = 500
        yStation = 500
        xPlayer = 500
        yPlayer = 500
        xSpeed = 0
        ySpeed = 0
        playerDrawing = 0
        mouseAngle = 0
        xMouse = 0
        yMouse = 0
        playerImage = playerImageFiles[0]

        if difficulty == "EASY":
                speedEnemy = 7
                numEnemiesPerFrame = 65

        elif difficulty == "NORMAL":
                speedEnemy = 14
                numEnemiesPerFrame = 30

        elif difficulty == "HARD":
                speedEnemy = 21
                numEnemiesPerFrame = 9
        
        whichAlien = 1
        
        xEnemy1 = []
        yEnemy1 = []
        xEnemy2 = []
        yEnemy2 = []
        xEnemy3 = []
        yEnemy3 = []
        xEnemy4 = []
        yEnemy4 = []


        alien1Drawing = []
        alien2Drawing = []
        alien3Drawing = []
        alien4Drawing = []

        alien1Alive = []
        alien2Alive = []
        alien3Alive = []
        alien4Alive = []
            

        getAlienCoords()
        
        missile = []
        xMissile = []
        yMissile = []
        xMissileSpeed = []
        yMissileSpeed = []
        missileSpeed = 30

def getDistanceBetweenPoints(x1,y1,x2,y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)



def startMenu():
        global titleText, Play, playText, Rules, rulesText, Quit, quitText, playerImageFiles, startImage, enemyImage1, enemyImage2, enemyImage3, enemyImage4, station, stationDrawing
        global sI, E1, E2, E3, E4,alien1ImageFiles,alien2ImageFiles,alien3ImageFiles,alien4ImageFiles

        
        screen.create_rectangle(0,0,1000,1000, fill = "black")

        station = PhotoImage( file = "stationHit0.gif" )
        stationDrawing = screen.create_image( 140, 150, image = station, anchor=CENTER )

        sI = PhotoImage( file = "playerImages/playerCopy110.gif")
        startImage = screen.create_image(270, 450, image = sI, anchor=CENTER)
        E1 = PhotoImage( file = "alien1Images/alien1Copy44.gif")
        enemyImage1 = screen.create_image(400, 870, image = E1, anchor=CENTER)
        E2 = PhotoImage( file = "alien2Images/alien2Copy60.gif")
        enemyImage2 = screen.create_image(800, 200, image = E2, anchor=CENTER)
        E3 = PhotoImage( file = "alien3Images/alien3Copy55.gif")
        enemyImage3 = screen.create_image(900, 430, image = E3, anchor=CENTER)
        E4 = PhotoImage( file = "alien4Images/alien4Copy49.gif")
        enemyImage4 = screen.create_image(783, 680, image = E4, anchor=CENTER)
        
        for r in range (400):
                starX = randint(0,1000)
                starY = randint(0,1000)
                size = randint (0,4)
                colourChoice = choice(["white", "#FF004F", "yellow", "orange", "white"])
                screen.create_oval(starX,starY,starX+size,starY+size, fill = colourChoice)

        Play = screen.create_rectangle(400,375,600,475,fill="#FF004F")
        playText = screen.create_text(500,425,text="Start", font = "impact 30", fill = "black")
        Rules = screen.create_rectangle(400,525,600,625,fill="#FF004F")
        rulesText = screen.create_text(500,575, text="Rules", font="impact 30", fill="black")
        Quit = screen.create_rectangle(400,675,600,775,fill="#FF004F")
        quitText = screen.create_text(500,725, text="Quit", font="impact 30", fill="black")
        titleText = screen.create_text(500,225, text="SPACE DEFENCE", font="impact 54", fill="#FF004F")        
        screen.update()
        screen.bind( "<Button-1>", startMouseClickHandler )
        
def callStartMenu():
        global alien1ImageFiles,alien2ImageFiles,alien3ImageFiles,alien4ImageFiles,playerImageFiles, fireImage
        playerImageFiles = []
        alien1ImageFiles = []
        alien2ImageFiles = []
        alien3ImageFiles = []
        alien4ImageFiles = []
        
         
        for i in range(1,122):
                pImage = PhotoImage( file = "playerImages/playerCopy" + str(i) + ".gif" )
                playerImageFiles.append( pImage )
                
                a1Image = PhotoImage( file = "alien1Images/alien1Copy" + str(i) + ".gif" )
                alien1ImageFiles.append( a1Image )

                a2Image = PhotoImage( file = "alien2Images/alien2Copy" + str(i) + ".gif" )
                alien2ImageFiles.append( a2Image )
                
                a3Image = PhotoImage( file = "alien3Images/alien3Copy" + str(i) + ".gif" )
                alien3ImageFiles.append( a3Image )

                a4Image = PhotoImage( file = "alien4Images/alien4Copy" + str(i) + ".gif" )
                alien4ImageFiles.append( a4Image )
        fireImage = PhotoImage( file = "fire.gif" )
        
        startMenu()
        
def startMouseClickHandler(event):
    global Play, playText, Rules, rulesText, Quit, quitText, titleText


    xMouse = event.x
    yMouse = event.y

    if 400 < xMouse < 600 and 375 < yMouse < 475:
            screen.delete(Play, playText, Rules, rulesText, Quit, quitText, titleText)#, startImage, enemyImage1, enemyImage2, enemyImage3, enemyImage4, station)
            difficultyScreen()

    elif 400 < xMouse < 600 and 525 < yMouse < 625:
            screen.delete(Play, playText, Rules, rulesText, Quit, quitText, titleText)
            ruleScreen()

    elif 400 < xMouse < 600 and 675 < yMouse < 775:
            root.destroy()

def difficultyScreen():
        global Easy, easyText, Normal, normalText, Hard, hardText

        Easy = screen.create_rectangle(400,375,600,475,fill="#FF004F")
        easyText = screen.create_text(500,425,text="EASY", font = "impact 30", fill = "black")
        Normal = screen.create_rectangle(400,525,600,625,fill="#FF004F")
        normalText = screen.create_text(500,575, text="NORMAL", font="impact 30", fill="black")
        Hard = screen.create_rectangle(400,675,600,775,fill="#FF004F")
        hardText = screen.create_text(500,725, text="HARD", font="impact 30", fill="black")

        screen.bind( "<Button-1>", difficultyMouseClickHandler )
     

def difficultyMouseClickHandler( event ):
        global Play, playText, Rules, rulesText, Quit, quitText, titleText, numEnemiesPerFrame, speedEnemy, difficulty, startImage, enemyImage1, enemyImage2, enemyImage3, enemyImage4, station
        global n
        xMouse = event.x
        yMouse = event.y
        screen.delete('all')

        if 400 < xMouse < 600 and 375 < yMouse < 475:
                screen.delete(Easy, easyText, Normal, normalText, Hard, hardText)#, startImage, enemyImage1, enemyImage2, enemyImage3, enemyImage4, station)
                n = screen.create_text(500,500, text = "3", font="impact 60", fill="#FF004F")
                screen.update()
                sleep(1)
                screen.delete(n)
                n = screen.create_text(500,500, text = "2", font="impact 60", fill="#FF004F")
                screen.update()
                sleep(1)
                screen.delete(n)
                n = screen.create_text(500,500, text = "1", font="impact 60", fill="#FF004F")
                screen.update()
                sleep(1)
                screen.delete(n)
                difficulty = "EASY"
                runGame()

        elif 400 < xMouse < 600 and 525 < yMouse < 625:
                screen.delete(Easy, easyText, Normal, normalText, Hard, hardText)#, startImage, enemyImage1, enemyImage2, enemyImage3, enemyImage4, station)
                n = screen.create_text(500,500, text = "3", font="impact 60", fill="#FF004F")
                screen.update()
                sleep(1)
                screen.delete(n)
                n = screen.create_text(500,500, text = "2", font="impact 60", fill="#FF004F")
                screen.update()
                sleep(1)
                screen.delete(n)
                n = screen.create_text(500,500, text = "1", font="impact 60", fill="#FF004F")
                screen.update()
                sleep(1)
                screen.delete(n)
                difficulty = "NORMAL"
                runGame()

        elif 400 < xMouse < 600 and 675 < yMouse < 775:
                screen.delete(Easy, easyText, Normal, normalText, Hard, hardText)#, startImage, enemyImage1, enemyImage2, enemyImage3, enemyImage4, station)
                n = screen.create_text(500,500, text = "3", font="impact 60", fill="#FF004F")
                screen.update()
                sleep(1)
                screen.delete(n)
                n = screen.create_text(500,500, text = "2", font="impact 60", fill="#FF004F")
                screen.update()
                sleep(1)
                screen.delete(n)
                n = screen.create_text(500,500, text = "1", font="impact 60", fill="#FF004F")
                screen.update()
                sleep(1)
                screen.delete(n)
                difficulty = "HARD"
                runGame()

def ruleScreen():
        global rule1, rule2, rule3, rule4, rule5, rule6, instructions1, instructions2, instructions3, BACK, backText

        rule1 = screen.create_text(500,300, text = "You are commanding a spaceship and your goal is to protect", font="impact 24", fill="#FF004F")
        rule2 = screen.create_text(500,350, text = "the space station from alien invaders. The spacestation has a ", font="impact 24", fill="#FF004F")
        rule3 = screen.create_text(500,400, text = "limited amount of health before it is beyond repair, there are ", font="impact 24", fill="#FF004F")
        rule4 = screen.create_text(500,450, text = "self-destructing robot aliens coming from all over the the map", font = "impact 24", fill = "#FF004F")
        rule5 = screen.create_text(500,500, text = "      to destroy the ship. If three ships crash into the station,      ", font = "impact 24", fill = "#FF004F")
        rule6 = screen.create_text(500,550, text = "                                   it's game over.                                         ", font = "impact 24", fill = "#FF004F")

        instructions1 =  screen.create_text(500, 650, text = " Use WASD to move and your mouse to aim the spaceship. ", font = "impact 24", fill = "green")
        instructions2 =  screen.create_text(500, 700, text = "Click the left button on your mouse to shoot where you aim.", font = "impact 24", fill = "green")
        instructions3 =  screen.create_text(500, 750, text = "        Good luck, the fate of humanity is in your hands.         ",  font = "impact 24", fill = "green")
        
        BACK = screen.create_rectangle(50,50,250,150,fill="#FF004F")
        backText = screen.create_text(150,100,text="Back",font="impact 30",fill="white")

        screen.bind( "<Button-1>", ruleMouseClickHandler )

def ruleMouseClickHandler(event):
        global rule1, rule2, rule3, rule4, rule5, rule6, instructions1, instructions2, instructions3, BACK, backText
    
        xMouse = event.x
        yMouse = event.y

        if 50 < xMouse < 250 and 50 < yMouse < 150:
                screen.delete(rule1, rule2, rule3, rule4, rule5, instructions1, instructions2, instructions3, BACK, backText)
                startMenu()
         
def getAlienCoords(): #figures out random coords for aliens 
        global xEnemy1, yEnemy1, xEnemy2, yEnemy2, xEnemy3, yEnemy3, xEnemy4, yEnemy4, whichAlien

        z = randint(1,4)
        
        if z == 1:
                X = randint(-200,0)
                Y = randint(0, 1000)


        elif z == 2:
                X = randint(1000,1200)
                Y = randint(0, 1000)

        elif z == 3:
                X = randint(0, 1000)
                Y = randint(-200, 0)


        elif z == 4:
                X = randint(0, 1000)
                Y = randint(1000,1200)

                
        if whichAlien == 1:
                 xEnemy1.append(X)
                 yEnemy1.append(Y)

        elif whichAlien == 2:
                 xEnemy2.append(X)
                 yEnemy2.append(Y)

        elif whichAlien == 3:
                 xEnemy3.append(X)
                 yEnemy3.append(Y)

        elif whichAlien == 4:
                 xEnemy4.append(X)
                 yEnemy4.append(Y)

        createAlien()


def createAlien(): #adds an empty index to the drawing alien arrays
        global alien1Drawing, alien2Drawing, alien3Drawing, whichAlien

        if whichAlien == 1:
                 alien1Drawing.append(0)
                 alien1Alive.append(True)

        elif whichAlien == 2:
                 alien2Drawing.append(0)
                 alien2Alive.append(True)
                
        elif whichAlien == 3:
                alien3Drawing.append(0)
                alien3Alive.append(True)
                
        elif whichAlien == 4:
                alien4Drawing.append(0)
                alien4Alive.append(True)

def alienUpdatingandDrawing(): #goes through each alien array and updates positions then draws them
        global xEnemy1, yEnemy1, xEnemy2, yEnemy2, xEnemy3, yEnemy3, xEnemy4, yEnemy4, alien1Drawing, alien2Drawing, alien3Drawing, alien4Drawing, whichAlien, numEnemiesPerFrame, speedEnemy, alien1Alive, alien2Alive, alien3Alive, alien4Alive


        if len(alien1Drawing) > 0:
                
                for i in range(len(alien1Drawing)):


                        distanceX = xEnemy1[i] - xStation
                        distanceY = yEnemy1[i] - yStation
                        angle = atan2(distanceY, distanceX)
                        Angle = degrees(angle)
                        f = int(-1*(Angle/3))
                        f = f - 60
                ##        print(xEnemy, yEnemy)
                ##        print(i)
                        hyp = sqrt(((distanceX)**2)+(distanceY)**2)
                        distanceX = distanceX / hyp
                        distanceY = distanceY / hyp
                        xEnemy1[i] = xEnemy1[i] -speedEnemy*distanceX
                        yEnemy1[i] = yEnemy1[i] -speedEnemy*distanceY

                        alien1Image = alien1ImageFiles[f]
                            
                        alien1Drawing[i] = screen.create_image( xEnemy1[i], yEnemy1[i], image = alien1Image, anchor=CENTER )


        if len(alien2Drawing) > 0:
                
                for i in range(len(alien2Drawing)):
                        
     
                        distanceX = xEnemy2[i] - xStation
                        distanceY = yEnemy2[i] - yStation
                        angle = atan2(distanceY, distanceX)
                        Angle = degrees(angle)
                        f = int(-1*(Angle/3))
                        f = f - 60
                ##        print(xEnemy, yEnemy)
                ##        print(i)
                        hyp = sqrt(((distanceX)**2)+(distanceY)**2)
                        distanceX = distanceX / hyp
                        distanceY = distanceY / hyp
                        xEnemy2[i] = xEnemy2[i] -speedEnemy*distanceX
                        yEnemy2[i] = yEnemy2[i] -speedEnemy*distanceY

                        alien2Image = alien2ImageFiles[f]
                            
                        alien2Drawing[i] = screen.create_image( xEnemy2[i], yEnemy2[i], image = alien2Image, anchor=CENTER )

        if len(alien3Drawing) > 0:
                
                for i in range(len(alien3Drawing)):

                 
                        distanceX = xEnemy3[i] - xStation
                        distanceY = yEnemy3[i] - yStation
                        angle = atan2(distanceY, distanceX)
                        Angle = degrees(angle)
                        f = int(-1*(Angle/3))
                        f = f - 60
                ##        print(xEnemy, yEnemy)
                ##        print(i)
                        hyp = sqrt(((distanceX)**2)+(distanceY)**2)
                        distanceX = distanceX / hyp
                        distanceY = distanceY / hyp
                        xEnemy3[i] = xEnemy3[i] -speedEnemy*distanceX
                        yEnemy3[i] = yEnemy3[i] -speedEnemy*distanceY

                        alien3Image = alien3ImageFiles[f]
                            
                        alien3Drawing[i] = screen.create_image( xEnemy3[i], yEnemy3[i], image = alien3Image, anchor=CENTER )

        if len(alien4Drawing) > 0:
                
                for i in range(len(alien4Drawing)):

         
                        distanceX = xEnemy4[i] - xStation
                        distanceY = yEnemy4[i] - yStation
                        angle = atan2(distanceY, distanceX)
                        Angle = degrees(angle)
                        f = int(-1*(Angle/3))
                        f = f - 60
                ##        print(xEnemy, yEnemy)
                ##        print(i)
                        hyp = sqrt(((distanceX)**2)+(distanceY)**2)
                        distanceX = distanceX / hyp
                        distanceY = distanceY / hyp
                        xEnemy4[i] = xEnemy4[i] -speedEnemy*distanceX
                        yEnemy4[i] = yEnemy4[i] -speedEnemy*distanceY

                        alien4Image = alien4ImageFiles[f]
                            
                        alien4Drawing[i] = screen.create_image( xEnemy4[i], yEnemy4[i], image = alien4Image, anchor=CENTER )


        
        
def updateObjects():
        global playerDrawing, stationDrawing, player, station, hits, hearts, fullHeart, lostHeart, gameEnded, scoreText
               
        if hits > 2:
                gameEnded = True
        station = PhotoImage( file = "stationHit" + str(hits) +".gif" )
        

        stationDrawing = screen.create_image( xStation, yStation, image = station, anchor=CENTER )
        scoreText = screen.create_text(990,30, text = score,  font="impact 40", fill="#FF004F", anchor="e")
        hearts = []
        nothit = 3 - hits
        
        for i in range(3):
                if nothit > 0:
                        hearts.append(screen.create_image(90 * i + 45, 50, image = fullHeart))
                        nothit = nothit - 1
                else:
                        hearts.append(screen.create_image(90 * i + 45, 50, image = lostHeart))

        for i in range(len(fire)):
                fireTimer[i] -= 1

        

def spawnNewMissiles():
        global missile, xMissile, yMissile
        xMissile.append(xPlayer)
        yMissile.append(yPlayer)
        missile.append(0)
        xMissileSpeed.append(missileSpeed*cos(getAngle()))
        yMissileSpeed.append(-missileSpeed*sin(getAngle()))
        

def updateMissilePositions():
        global missile, xMissile, yMissile, missileSpeed, score, fireImage
        
        for i in range (len(yMissile)-1,-1,-1):
                y = yMissile[i]
                x = xMissile[i]
                yMissile[i] = y + yMissileSpeed[i]
                xMissile[i] = x + xMissileSpeed[i]

                for j in range(len(xEnemy1)-1,-1,-1):
                        d = getDistanceBetweenPoints(x,y,xEnemy1[j],yEnemy1[j])
                        if d < 50:
                                alien1Drawing.pop(j)
                                xEnemy1.pop(j)
                                yEnemy1.pop(j)
                                missile.pop(i)
                                xMissile.pop(i)
                                yMissile.pop(i)
                                xMissileSpeed.pop(i)
                                yMissileSpeed.pop(i)
                                score += 100
                                fire.append(screen.create_image(x,y, image = fireImage))
                                fireTimer.append(20)
                                break
                for j in range(len(xEnemy2)-1,-1,-1):
                        d = getDistanceBetweenPoints(x,y,xEnemy2[j],yEnemy2[j])
                        if d < 50:
                                alien2Drawing.pop(j)
                                xEnemy2.pop(j)
                                yEnemy2.pop(j)
                                missile.pop(i)
                                xMissile.pop(i)
                                yMissile.pop(i)
                                xMissileSpeed.pop(i)
                                yMissileSpeed.pop(i)
                                score += 100
                                fire.append(screen.create_image(x,y, image = fireImage))
                                fireTimer.append(20)
                                break
                for j in range(len(xEnemy3)-1,-1,-1):
                        d = getDistanceBetweenPoints(x,y,xEnemy3[j],yEnemy3[j])
                        if d < 50:
                                alien3Drawing.pop(j)
                                xEnemy3.pop(j)
                                yEnemy3.pop(j)
                                missile.pop(i)
                                xMissile.pop(i)
                                yMissile.pop(i)
                                xMissileSpeed.pop(i)
                                yMissileSpeed.pop(i)
                                score += 100
                                fire.append(screen.create_image(x,y, image = fireImage))
                                fireTimer.append(20)
                                break
                for j in range(len(xEnemy4)-1,-1,-1):
                        d = getDistanceBetweenPoints(x,y,xEnemy4[j],yEnemy4[j])
                        if d < 50:
                                alien4Drawing.pop(j)
                                xEnemy4.pop(j)
                                yEnemy4.pop(j)
                                missile.pop(i)
                                xMissile.pop(i)
                                yMissile.pop(i)
                                xMissileSpeed.pop(i)
                                yMissileSpeed.pop(i)
                                score += 100
                                fire.append(screen.create_image(x,y, image = fireImage))
                                fireTimer.append(20)
                                break
def deleteOffscreenMissiles():

        global missile, xMissile, Ymissile, xMissileSpeed, yMissileSpeed

        for z in range(0, len(missile)):

                if xMissile[z] < 0 or xMissile[z] > 1000 or yMissile[z] < 0 or xMissile[z] > 1000:
                        deleteMissileImage = missile[z]
                        deletexMissile = xMissile[z]
                        deleteyMissile = yMissile[z]
                        deletexMissileSpeed = xMissileSpeed[z]
                        deleteyMissileSpeed = yMissileSpeed[z]

                        missile.remove(deleteMissileImage)
                        xMissile.remove(deletexMissile)
                        yMissile.remove(deleteyMissile)
                        xMissileSpeed.remove(deletexMissileSpeed)
                        yMissileSpeed.remove(deleteyMissileSpeed)

                        break

def ifAlienDies(): #goes through each alien array then figures if we need to delete them, then deletes them
        global xEnemy1, yEnemy1, xEnemy2, yEnemy2, xEnemy3, yEnemy3, xEnemy4, yEnemy4, alien1Drawing, alien2Drawing, alien3Drawing, alien4Drawing, whichAlien, alien1Alive, alien2Alive, alien3Alive, alien4Alive
        global hits
        
        if len(alien1Drawing) > 0:       

                for i in range (len(alien1Drawing)):
                        if sqrt((xStation - xEnemy1[i])**2 + (yStation - yEnemy1[i])**2) <= 30:
                                deleteEnemyX = xEnemy1[i]
                                deleteEnemyY = yEnemy1[i]
                                deleteDrawing = alien1Drawing[i]

                                xEnemy1.remove(deleteEnemyX)
                                yEnemy1.remove(deleteEnemyY)
                                alien1Drawing.remove(deleteDrawing)

                                #alien1Alive[i] = False
                                hits += 1

                                break

        if len(alien2Drawing) > 0:       

                for i in range (len(alien2Drawing)):
                        if sqrt((xStation - xEnemy2[i])**2 + (yStation - yEnemy2[i])**2) <= 30:
                                deleteEnemyX = xEnemy2[i]
                                deleteEnemyY = yEnemy2[i]
                                deleteDrawing = alien2Drawing[i]

                                xEnemy2.remove(deleteEnemyX)
                                yEnemy2.remove(deleteEnemyY)
                                alien2Drawing.remove(deleteDrawing)

                                #alien2Alive[i] = False
                                hits += 1
                                break

        if len(alien3Drawing) > 0:       

                for i in range (len(alien3Drawing)):
                        if sqrt((xStation - xEnemy3[i])**2 + (yStation - yEnemy3[i])**2) <= 30:
                                deleteEnemyX = xEnemy3[i]
                                deleteEnemyY = yEnemy3[i]
                                deleteDrawing = alien3Drawing[i]

                                xEnemy3.remove(deleteEnemyX)
                                yEnemy3.remove(deleteEnemyY)
                                alien3Drawing.remove(deleteDrawing)

                                #alien3Alive[i] = False
                                hits += 1
                                break
        if len(alien4Drawing) > 0:       

                for i in range (len(alien4Drawing)):
                        if sqrt((xStation - xEnemy4[i])**2 + (yStation - yEnemy4[i])**2) <= 30:
                                deleteEnemyX = xEnemy4[i]
                                deleteEnemyY = yEnemy4[i]
                                deleteDrawing = alien4Drawing[i]

                                xEnemy4.remove(deleteEnemyX)
                                yEnemy4.remove(deleteEnemyY)
                                alien4Drawing.remove(deleteDrawing)
                                hits += 1
                                #alien4Alive[i] = False
                                break




def drawNewAlien(): #selects a random alien
        global alien1Drawing, alien2Drawing, alien3Drawing, alien4Drawing, whichAlien

        whichAlien = randint(1, 4)

        getAlienCoords()
        
        
                
def drawMissile():
        global xMissile, yMissile, missile
        
        for z in range(0,len(yMissile)):
                missile[z] = screen.create_oval( xMissile[z] - 5, yMissile[z] - 5,xMissile[z] + 5,yMissile[z] + 5,fill="yellow")
                

def mouseMotionHandler(event):
        global xMouse, yMouse, mouseAngle

        xMouse = event.x
        yMouse = event.y

def getAngle():
        global xMouse, yMouse, xPlayer, yPlayer
        
        dx = xMouse - xPlayer
        dy = yPlayer - yMouse

        radianAngle = atan2( dy, dx )

        if dy >= 0:
                return radianAngle
        
        else:
                return radianAngle + 2*pi

def deleteMissile():
        global yMissile, missile
        
        for z in range(0,len(yMissile)):
                screen.delete(missile[z])

def updatePlayer():
        global playerDrawing, playerImage, mouseAngle, xPlayer, yPlayer, xSpeed, ySpeed 

        xPlayer = xPlayer + xSpeed
        yPlayer = yPlayer + ySpeed
        mouseAngle = degrees(getAngle())

        screen.delete(playerDrawing)
        deleteMissile()

        i = int(mouseAngle/3)
        playerImage = playerImageFiles[i]
            
        playerDrawing = screen.create_image( xPlayer, yPlayer, image = playerImage, anchor=CENTER )

        if xPlayer > 1000:
                xPlayer = 0

        elif yPlayer > 1000:
                yPlayer = 0

        elif xPlayer < 0:
                xPlayer = 1000

        elif yPlayer < 0:
                yPlayer = 1000



def mouseClickHandler( event ):
        global xMouse, yMouse

        xMouse = event.x
        yMouse = event.y

        spawnNewMissiles()


def keyDownHandler( event ):
        global xSpeed, ySpeed, xPlayer, yPlayer
    
        if event.keysym == "a" or event.keysym == "A":          #LEFT 
                xSpeed = -10
        
        elif event.keysym == "d" or event.keysym == "D":        #RIGHT 
                xSpeed = 10

        elif event.keysym == "w" or event.keysym == "W":        #UP 
                ySpeed = -10

        elif event.keysym == "s" or event.keysym == "S":        #DOWN 
                ySpeed = 10

def keyUpHandler( event ):
    global xSpeed, ySpeed

    xSpeed = 0
    ySpeed = 0

def endGameClickHandler( event ):
        global Play, playText, Rules, rulesText, Quit, quitText, titleText, numEnemiesPerFrame, speedEnemy, difficulty, startImage, enemyImage1, enemyImage2, enemyImage3, enemyImage4, station

        xMouse = event.x
        yMouse = event.y

        if 400 < xMouse < 600 and 525 < yMouse < 625:
                screen.delete(gameOver, scoreText, retry, retryText, returnMenu, returnMenuText)
                runGame()

        elif 200 < xMouse < 800 and 675 < yMouse < 775:
                screen.delete(gameOver, scoreText, retry, retryText, returnMenu, returnMenuText)
                startMenu()

def endGame():
        global gameOver, scoreText, retry, retryText, returnMenu, returnMenuText
        screen.bind( "<Button-1>", endGameClickHandler )
        screen.delete('all')
        gameOver = screen.create_text(500,200, text="Game Over", font="impact 54", fill="#FF004F")
        scoreText = screen.create_text(500,300, text="Score: " + str(score), font="impact 40", fill="green")
        
        retry = screen.create_rectangle(400,525,600,625,fill="#FF004F")
        retryText = screen.create_text(500,575, text="RETRY", font="impact 30", fill="black")
        returnMenu = screen.create_rectangle(300,675,700,775,fill="#FF004F")
        returnMenuText = screen.create_text(500,725, text="RETURN TO MENU", font="impact 30", fill="black")


def runGame():
        
        global mouseAngle, alien2Drawing, time, speedEnemy, numEnemiesPerFrame, difficulty, gameEnded, fullHeart, lostHeart
        global startImage, enemyImage1, enemyImage2, enemyImage3, enemyImage4, station

        screen.delete(startImage, enemyImage1, enemyImage2, enemyImage3, enemyImage4, station)
        
        gameEnded = False
        fullHeart = PhotoImage( file = "Heart.gif" )
        lostHeart = PhotoImage( file = "lostHeart.gif" )
        screen.bind( "<Button-1>", mouseClickHandler )
        screen.bind( "<Motion>", mouseMotionHandler)
        screen.bind( "<KeyPress>", keyDownHandler )
        screen.bind( "<KeyRelease>", keyUpHandler )
        
        setInitialValues()

        f = 0

        time = 0
        

        while True:
                updateObjects()
                updateMissilePositions()
                updatePlayer()
                drawMissile()
                alienUpdatingandDrawing() #draws and updates aliens
                
                if f % numEnemiesPerFrame == 0:   #every 100 frames adds new alien
                        time += 1


                if time > 0:
                        if time % 2 == 0:
                                drawNewAlien()
                                time += 1
                        
                        
                screen.update()
                sleep(0.01)
                screen.delete(playerDrawing, stationDrawing, scoreText)
                for i in range(len(fire)-1,-1,-1):
                        if fireTimer[i] < 0:
                                screen.delete(fire[i])
                                fireTimer.pop(i)
                                fire.pop(i)
                                
                for i in range(3):
                        screen.delete(hearts[i])

                if len(alien1Drawing) > 0:
                        for i in range(len(alien1Drawing)):    #goes through the arrays for each aliens to delete
                                screen.delete(alien1Drawing[i])

                if len(alien2Drawing) > 0:
                        for i in range(len(alien2Drawing)):
                                screen.delete(alien2Drawing[i])

                if len(alien3Drawing) > 0:
                        for i in range(len(alien3Drawing)):
                                screen.delete(alien3Drawing[i])

                if len(alien4Drawing) > 0:
                        for i in range(len(alien4Drawing)):
                                screen.delete(alien4Drawing[i])

                deleteMissile()
                deleteOffscreenMissiles()
                ifAlienDies() #checks if aliens has died
                

                f = f + 1
                if gameEnded:
                        break
                
        endGame()

#checkForCollisions()   


#At the bottom
root.after( 0, callStartMenu )
screen.pack()
screen.focus_set()
root.mainloop()
