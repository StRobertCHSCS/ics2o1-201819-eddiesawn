import arcade


WIDTH = 600
HEIGHT =600

kirb = 100

RECT_WIDTH = 50
RECT_HEIGHT = 50


center_x = 100
center_y = 60
delta_x = 10
delta_y = 5

my_button = [160, 250, 150, 50]
show_text = False

def button():
    arcade.start_render()
    arcade.draw_xywh_rectangle_filled(my_button[0],
                                      my_button[1],
                                      my_button[2],
                                      my_button[3],
                                      arcade.color.blue)

def on_update(button):
    pass

def kirb():
    arcade.start_render()
    texture = arcade.load_texture("images/kirb.jpg")
    scale = 1
    arcade.draw_texture_rectangle(100, 100, scale * texture.width,
                                  scale * texture.height, texture, 0)


def on_update(delta_time):

    global center_x, center_y
    global delta_x, delta_y

    center_x += delta_x
    center_y += delta_y

    # Figure out if we hit the edge and need to reverse.
    if center_x < RECT_WIDTH // 2 or center_x > WIDTH - RECT_WIDTH // 2:
        delta_x *= -1

    if center_y < RECT_HEIGHT // 2 or center_y > HEIGHT - RECT_HEIGHT // 2:
        delta_y *= -1



def on_key_press(key, modifiers):
    pass

def on_draw():
    arcade.start_render()

    kirb = arcade.load_texture("images/kirb.png")
    scale = 0.3
    arcade.draw_texture_rectangle(center_x, center_y, scale * kirb.width,
                                  scale * kirb.height, kirb, 0)

    arcade.draw_text("Protect Yourself From Malware!", 200, 300, arcade.color.BLACK)

    arcade.draw_text("Use These Antiviruses to protect yourself!", 160, 250, arcade.color.BLACK)

    avg = arcade.load_texture("images/avg.png")
    arcade.draw_texture_rectangle(150, 120, .1 * avg.width, .1 * avg.height, avg, 0)

    malwarebytes = arcade.load_texture("images/malwarebytes.png")
    arcade.draw_texture_rectangle(450, 120, .1 * malwarebytes.width, .1 * malwarebytes.height, malwarebytes, 0)

    avast = arcade.load_texture("images/avast.png")
    arcade.draw_texture_rectangle(150, 450, .75 * avast.width, .75 * avast.height, avast, 0)

    bitdefender = arcade.load_texture("images/bitdefender.png")
    arcade.draw_texture_rectangle(450, 450, 0.2 * bitdefender.width, 0.2 * bitdefender.height, bitdefender, 0)


def on_key_release(key, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):
    pass

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Computers and Society Poster")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_update = on_update
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
