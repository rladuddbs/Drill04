from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character_move_up = load_image('character_move_up.png')
character_move_left = load_image('character_move_left.png')
character_move_down = load_image('character_move_down.png')
character_move_right = load_image('character_move_right.png')
character_move_leftup = load_image('character_move_leftup.png')
character_move_rightup = load_image('character_move_rightup.png')
character_look_up = load_image('character_look_up.png')
character_look_left = load_image('character_look_left.png')
character_look_down = load_image('character_look_down.png')
character_look_right = load_image('character_look_right.png')
character_look_leftup = load_image('character_look_left.png')
character_look_rightdown = load_image('character_look_right.png')


def handle_events():
    global running
    global dirX, dirY
    global x, y
    global look
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                dirY -= 1
                look = 1
            elif event.key == SDLK_LEFT:
                dirX += 1
                look = 2
            elif event.key == SDLK_DOWN:
                dirY += 1
                look = 3
            elif event.key == SDLK_RIGHT:
                dirX -= 1
                look = 4


running = True
x = 400
y = 300
dirX = 0
dirY = 0
look = 3
frame = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)



    if(dirX == 0):
        if(dirY == 1):
            character_move_up.clip_draw(frame*18, 0, 18, 22, x, y, 18 * 5, 22 * 5)
        elif(dirY == -1):
            character_move_down.clip_draw(frame*18, 0, 18, 22, x, y, 18 * 5, 22 * 5)
        elif(dirY == 0):
            if (look == 1):
                character_look_up.clip_draw(frame * 18, 0, 18, 22, x, y, 18 * 5, 22 * 5)
            elif (look == 2):
                character_look_left.clip_draw(frame * 17, 0, 17, 22, x, y, 17 * 5, 22 * 5)
            elif (look == 3):
                character_look_down.clip_draw(frame * 18, 0, 18, 22, x, y, 18 * 5, 22 * 5)
            elif (look == 4):
                character_look_right.clip_draw(frame * 17, 0, 17, 22, x, y, 17 * 5, 22 * 5)
    elif(dirX == 1):
        if (dirY == 1):
            character_move_rightup.clip_draw(frame * 16, 0, 16, 24, x, y, 16 * 5, 24 * 5)
        elif (dirY == -1):
            character_move_right.clip_draw(frame * 18, 0, 16, 24, x, y, 16 * 5, 24 * 5)
        elif (dirY == 0):
            character_move_right.clip_draw(frame * 18, 0, 16, 24, x, y, 16 * 5, 24 * 5)
    elif (dirX == -1):
        if (dirY == 1):
            character_move_leftup.clip_draw(frame * 16, 0, 16, 24, x, y, 16 * 5, 24 * 5)
        elif (dirY == -1):
            character_move_left.clip_draw(frame * 18, 0, 18, 24, x, y, 18 * 5, 24 * 5)
        elif (dirY == 0):
            character_move_left.clip_draw(frame * 18, 0, 18, 24, x, y, 18 * 5, 24 * 5)

    if(x < 80): x = 80
    if(x > 1200): x = 1200
    if(y < 80): y = 80
    if(y > 1000): y = 1000

    update_canvas()
    handle_events()
    frame = (frame + 18) % 4
    x += dirX * 10
    y += dirY * 10
    delay(0.08)


close_canvas()