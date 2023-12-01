def on_button_pressed_a():
    basic.show_number(input.compass_heading())
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
