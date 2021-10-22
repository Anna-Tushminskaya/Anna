import wrap

wrap.world.create_world(825, 525, 100, 100)
wrap.world.set_back_image('C:/Users/Анечка/Desktop/1.jpg')
x = 100
y = 300
shange = 70

mario = wrap.sprite.add("mario-1-big", x, y, "walk1")
ghost = wrap.sprite.add("mario-enemies", x,y, "fish_red", visible=False)


@wrap.on_key_always(wrap.K_RIGHT)
def move_right():
    angle = wrap.sprite.get_angle_modif(mario)
    wrap.sprite.set_angle_modif(mario, angle + 10)


@wrap.on_key_always(wrap.K_LEFT)
def move_left():
    angle = wrap.sprite.get_angle_modif(mario)
    wrap.sprite.set_angle_modif(mario, angle - 10)


@wrap.on_key_always(wrap.K_UP)
def move_forward():
    angle = wrap.sprite.get_angle_modif(mario)
    wrap.sprite.move_at_angle(mario, angle, 20)

@wrap.on_mouse_move()
def move_ghost(pos_x, pos_y):
    wrap.sprite.move_to(ghost,pos_x,pos_y)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def show_ghost():
    wrap.sprite.show(ghost)

@wrap.on_mouse_up(wrap.BUTTON_LEFT)
def hide_ghost():
    wrap.sprite.hide(ghost)