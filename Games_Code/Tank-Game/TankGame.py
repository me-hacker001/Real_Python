import os

import pygame
import random

pygame.init()

display_width = 800
display_height = 600

game_layout_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks Game - Brought To You By Itsourcecode.com')

Resources = pygame.image.load("Games_Code/Tank-Game/resources/game_background.png")
pygame.display.set_icon(Resources)


wheat = (245, 222, 179)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)


clock = pygame.time.Clock()

tnk_width = 40
tnk_height = 20

tur_width = 5
whl_width = 5

grnd_height = 35

s_font = pygame.font.SysFont("Times New Roman", 25)
m_font = pygame.font.SysFont("Times New Roman", 50)
l_font = pygame.font.SysFont("Times New Roman", 85)
vs_font = pygame.font.SysFont("Times New Roman", 25)


def Score(Score):
        txt = s_font.render("Score: " + str(Score), True, white)
        game_layout_display.blit(txt, [0, 0])


def txt_object(txt, color, size="small"):
    if size == "small":
        txtSrfc = s_font.render(txt, True, color)
    if size == "medium":
        txtSrfc = m_font.render(txt, True, color)
    if size == "large":
        txtSrfc = l_font.render(txt, True, color)
    if size == "vsmall":
        txtSrfc = vs_font.render(txt, True, color)

    return txtSrfc, txtSrfc.get_rect()


def txt_btn(message, color, btnx, btny, btnwidth, btnheight, size="vsmall"):
    txtSrf, textRect = txt_object(message, color, size)
    textRect.center = ((btnx + (btnwidth / 2)), btny + (btnheight / 2))
    game_layout_display.blit(txtSrf, textRect)

# function for texts that has to appear over screen
def msg_screen(message, color, y_displace=0, size="small"):
    txtSrf, textRect = txt_object(message, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    game_layout_display.blit(txtSrf, textRect)


def tank(x, y, turret_position):
    x = int(x)
    y = int(y)

    pos_Turrets = [(x - 27, y - 2),
                       (x - 26, y - 5),
                       (x - 25, y - 8),
                       (x - 23, y - 12),
                       (x - 20, y - 14),
                       (x - 18, y - 15),
                       (x - 15, y - 17),
                       (x - 13, y - 19),
                       (x - 11, y - 21)
                       ]

    pygame.draw.circle(game_layout_display, blue, (x, y), int(tnk_height / 2))
    pygame.draw.rect(game_layout_display, blue, (x - tnk_height, y, tnk_width, tnk_height))

    pygame.draw.line(game_layout_display, blue, (x, y), pos_Turrets[turret_position], tur_width)

    pygame.draw.circle(game_layout_display, blue, (x - 15, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 10, y + 20), whl_width)

    pygame.draw.circle(game_layout_display, blue, (x - 15, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 10, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 5, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 5, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 10, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 15, y + 20), whl_width)

    return pos_Turrets[turret_position]


def computer_tank(x, y, turret_position):
    x = int(x)
    y = int(y)

    pos_Turrets = [(x + 27, y - 2),
                       (x + 26, y - 5),
                       (x + 25, y - 8),
                       (x + 23, y - 12),
                       (x + 20, y - 14),
                       (x + 18, y - 15),
                       (x + 15, y - 17),
                       (x + 13, y - 19),
                       (x + 11, y - 21)
                       ]

    pygame.draw.circle(game_layout_display, blue, (x, y), int(tnk_height / 2))
    pygame.draw.rect(game_layout_display, blue, (x - tnk_height, y, tnk_width, tnk_height))

    pygame.draw.line(game_layout_display, blue, (x, y), pos_Turrets[turret_position], tur_width)

    pygame.draw.circle(game_layout_display, blue, (x - 15, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 10, y + 20), whl_width)

    pygame.draw.circle(game_layout_display, blue, (x - 15, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 10, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x - 5, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 5, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 10, y + 20), whl_width)
    pygame.draw.circle(game_layout_display, blue, (x + 15, y + 20), whl_width)

    return pos_Turrets[turret_position]


def game_ctrls():
    gameControl = True

    while gameControl:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_layout_display.fill(black)
        msg_screen("Controls", white, -100, size="large")
        msg_screen("Fire: Spacebar", wheat, -30)
        msg_screen("Move Turret: Up and Down arrows", wheat, 10)
        msg_screen("Move Tank: Left and Right arrows", wheat, 50)
        msg_screen("Press D to raise Power % AND Press A to lower Power % ", wheat, 140)
        msg_screen("Pause: P", wheat, 90)

        btn("Play", 150, 500, 100, 50, green, light_green, action="play")
        btn("Main", 350, 500, 100, 50, yellow, light_yellow, action="main")
        btn("Quit", 550, 500, 100, 50, red, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)


def btn(txt, x, y, width, height, inactive_color, active_color, action=None,size=" "):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(game_layout_display, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_ctrls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

    else:
        pygame.draw.rect(game_layout_display, inactive_color, (x, y, width, height))

    txt_btn(txt, black, x, y, width, height)


def pause():
    paused = True
    msg_screen("Paused", white, -100, size="large")
    msg_screen("Press C to continue playing or Q to quit", wheat, 25)
    pygame.display.update()
    while paused:
        # game_layout_display.fill(black)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)


def barrier(x_loc, ran_height, bar_width):
    pygame.draw.rect(game_layout_display, green, [x_loc, display_height - ran_height, bar_width, ran_height])


def explosion(x, y, size=50):

    exp = True

    while exp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x, y

        choice_colors = [red, light_red, yellow, light_yellow]

        mgntde = 1

        while mgntde < size:
            exploding_bit_x = x + random.randrange(-1 * mgntde, mgntde)
            exploding_bit_y = y + random.randrange(-1 * mgntde, mgntde)

            pygame.draw.circle(game_layout_display, choice_colors[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y),
                               random.randrange(1, 5))
            mgntde += 1

            pygame.display.update()
            clock.tick(100)

        exp = False


def playerfireShell(xy, tankx, tanky, turPost, gun_power, xloc, bar_width, ranHeight, eTankX, eTankY):

    fire = True
    damage = 0

    startShell = list(xy)

    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # print(startShell[0],startShell[1])
        pygame.draw.circle(game_layout_display, red, (startShell[0], startShell[1]), 5)

        startShell[0] -= (12 - turPost) * 2

        # y = x**2
        startShell[1] += int(
            (((startShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPost + turPost / (12 - turPost)))

        if startShell[1] > display_height - grnd_height:
            print("Last shell:", startShell[0], startShell[1])
            hit_x = int((startShell[0] * display_height - grnd_height) / startShell[1])
            hit_y = int(display_height - grnd_height)
            print("Impact:", hit_x, hit_y)

            if eTankX + 10 > hit_x > eTankX - 10:
                print("Critical Hit!")
                damage = 25
            elif eTankX + 15 > hit_x > eTankX - 15:
                print("Hard Hit!")
                damage = 18
            elif eTankX + 25 > hit_x > eTankX - 25:
                print("Medium Hit")
                damage = 10
            elif eTankX + 35 > hit_x > eTankX - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startShell[0] <= xloc + bar_width
        check_x_2 = startShell[0] >= xloc

        check_y_1 = startShell[1] <= display_height
        check_y_2 = startShell[1] >= display_height - ranHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startShell[0], startShell[1])
            hit_x = int((startShell[0]))
            hit_y = int(startShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage


def computerfireShell(xy, tankx, tanky, turPost, gun_power, xloc, bar_width, ranHeight, ptankx, ptanky):

    damage = 0
    cPower = 1
    pow_found = False

    while not pow_found:
        cPower += 1
        if cPower > 100:
            pow_found = True
        # print(currentPower)

        fire = True
        startShell = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # pygame.draw.circle(game_layout_display, red, (startShell[0],startShell[1]),5)

            startShell[0] += (12 - turPost) * 2
            startShell[1] += int(
                (((startShell[0] - xy[0]) * 0.015 / (cPower / 50)) ** 2) - (turPost + turPost / (12 - turPost)))

            if startShell[1] > display_height - grnd_height:
                hit_x = int((startShell[0] * display_height - grnd_height) / startShell[1])
                hit_y = int(display_height - grnd_height)
                # explosion(hit_x,hit_y)
                if ptankx + 15 > hit_x > ptankx - 15:
                    print("target acquired!")
                    pow_found = True
                fire = False

            check_x_1 = startShell[0] <= xloc + bar_width
            check_x_2 = startShell[0] >= xloc

            check_y_1 = startShell[1] <= display_height
            check_y_2 = startShell[1] >= display_height - ranHeight

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startShell[0]))
                hit_y = int(startShell[1])
                # explosion(hit_x,hit_y)
                fire = False

    fire = True
    startShell = list(xy)
    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(game_layout_display, red, (startShell[0], startShell[1]), 5)

        startShell[0] += (12 - turPost) * 2



        gun_power = random.randrange(int(cPower * 0.90), int(cPower * 1.10))

        startShell[1] += int(
            (((startShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPost + turPost / (12 - turPost)))

        if startShell[1] > display_height - grnd_height:
            print("last shell:", startShell[0], startShell[1])
            hit_x = int((startShell[0] * display_height - grnd_height) / startShell[1])
            hit_y = int(display_height - grnd_height)
            print("Impact:", hit_x, hit_y)

            if ptankx + 10 > hit_x > ptankx - 10:
                print("Critical Hit!")
                damage = 25
            elif ptankx + 15 > hit_x > ptankx - 15:
                print("Hard Hit!")
                damage = 18
            elif ptankx + 25 > hit_x > ptankx - 25:
                print("Medium Hit")
                damage = 10
            elif ptankx + 35 > hit_x > ptankx - 35:
                print("Light Hit")
                damage = 5

            explosion(hit_x, hit_y)
            fire = False

        check_x_1 = startShell[0] <= xloc + bar_width
        check_x_2 = startShell[0] >= xloc

        check_y_1 = startShell[1] <= display_height
        check_y_2 = startShell[1] >= display_height - ranHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startShell[0], startShell[1])
            hit_x = int((startShell[0]))
            hit_y = int(startShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage


def power(level):
    text = s_font.render("Power: " + str(level) + "%", True, wheat)
    game_layout_display.blit(text, [display_width / 2, 0])


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        game_layout_display.fill(black)
        msg_screen("Welcome to Tanks War!", white, -100, size="large")
        msg_screen("The goal is to shoot and destroy", wheat, 15)
        msg_screen("the enemy tank before they destroy you.", wheat, 60)
        msg_screen("The more enemies you destroy, the highest score you get.", wheat, 110)
        msg_screen("Brought To You by :itsourcecode.com", wheat, 280)
        # msg_screen("Press C to play, P to pause or Q to quit",black,180)


        btn("Play", 150, 500, 100, 50, wheat, light_green, action="play",size="vsmall")
        btn("Controls", 350, 500, 100, 50, wheat, light_yellow, action="controls",size="vsmall")
        btn("Quit", 550, 500, 100, 50, wheat, light_red, action="quit",size="vsmall")

        pygame.display.update()

        clock.tick(15)


def game_over():
    game_over = True

    while game_over:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_layout_display.fill(black)
        msg_screen("Game Over", white, -100, size="large")
        msg_screen("You died.", wheat, -30)

        btn("Play Again", 150, 500, 150, 50, wheat, light_green, action="play")
        btn("Controls", 350, 500, 100, 50, wheat, light_yellow, action="controls")
        btn("Quit", 550, 500, 100, 50, wheat, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)


def you_win():
    win = True

    while win:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_layout_display.fill(black)
        msg_screen("You won!", white, -100, size="large")
        msg_screen("Congratulations!", wheat, -30)

        btn("play Again", 150, 500, 150, 50, wheat, light_green, action="play")
        btn("controls", 350, 500, 100, 50, wheat, light_yellow, action="controls")
        btn("quit", 550, 500, 100, 50, wheat, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)

def health_bars(p_health, e_health):
    if p_health > 75:
        p_health_color = green
    elif p_health > 50:
        p_health_color = yellow
    else:
        p_health_color = red

    if e_health > 75:
        e_health_color = green
    elif e_health > 50:
        e_health_color = yellow
    else:
        e_health_color = red

    pygame.draw.rect(game_layout_display, p_health_color, (680, 25, p_health, 25))
    pygame.draw.rect(game_layout_display, e_health_color, (20, 25, e_health, 25))


def gameLoop():
    gExit = False
    gOver = False
    FPS = 15

    p_health = 100
    e_health = 100

    bar_width = 50

    mTankX = display_width * 0.9
    mTankY = display_height * 0.9
    tnkMove = 0
    curTurPost = 0
    changeTurs = 0

    eTankX = display_width * 0.1
    eTankY = display_height * 0.9

    f_power = 50
    p_change = 0

    xloc = (display_width / 2) + random.randint(-0.1 * display_width, 0.1 * display_width)
    ranHeight = random.randrange(display_height * 0.1, display_height * 0.6)

    while not gExit:

        if gOver == True:
            # gameDisplay.fill(white)
            msg_screen("Game Over", red, -50, size="large")
            msg_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gExit = True
                        gOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gExit = True
                            gOver = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tnkMove = -5

                elif event.key == pygame.K_RIGHT:
                    tnkMove = 5

                elif event.key == pygame.K_UP:
                    changeTurs = 1

                elif event.key == pygame.K_DOWN:
                    changeTurs= -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:

                    damage = playerfireShell(gun, mTankX, mTankY, curTurPost, f_power, xloc, bar_width,
                                       ranHeight, eTankX, eTankY)
                    e_health -= damage

                    posMovement = ['f', 'r']
                    moveInd = random.randrange(0, 2)

                    for x in range(random.randrange(0, 10)):

                        if display_width * 0.3 > eTankX > display_width * 0.03:
                            if posMovement[moveInd] == "f":
                                eTankX += 5
                            elif posMovement[moveInd] == "r":
                                eTankX -= 5

                            game_layout_display.fill(black)
                            health_bars(p_health, e_health)
                            gun = tank(mTankX, mTankY, curTurPost)
                            e_gun = computer_tank(eTankX, eTankY, 8)
                            f_power += p_change

                            power(f_power)

                            barrier(xloc, ranHeight, bar_width)
                            game_layout_display.fill(green,
                                             rect=[0, display_height - grnd_height, display_width, grnd_height])
                            pygame.display.update()

                            clock.tick(FPS)

                    damage = computerfireShell(e_gun, eTankX, eTankY, 8, 50, xloc, bar_width,
                                         ranHeight, mTankX, mTankY)
                    p_health -= damage

                elif event.key == pygame.K_a:
                    p_change = -1
                elif event.key == pygame.K_d:
                    p_change = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tnkMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTurs = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    p_change = 0

        mTankX += tnkMove

        curTurPost += changeTurs

        if curTurPost > 8:
            curTurPost = 8
        elif curTurPost < 0:
            curTurPost = 0

        if mTankX - (tnk_width / 2) < xloc + bar_width:
            mTankX += 5

        game_layout_display.fill(black)
        health_bars(p_health, e_health)
        gun = tank(mTankX, mTankY, curTurPost)
        e_gun = computer_tank(eTankX, eTankY, 8)

        f_power += p_change

        if f_power > 100:
            f_power = 100
        elif f_power < 1:
            f_power = 1

        power(f_power)

        barrier(xloc, ranHeight, bar_width)
        game_layout_display.fill(green, rect=[0, display_height - grnd_height, display_width, grnd_height])
        pygame.display.update()

        if p_health < 1:
            game_over()
        elif e_health < 1:
            you_win()
        clock.tick(FPS)

    pygame.quit()

    quit()

game_intro()
gameLoop()
