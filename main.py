povoleno = BeatFraction.WHOLE

def on_burron_pressed_a():
    global povoleno
    povoleno= True
input.on_button_pressed(Button.A, on_Button_pressed_a)


def on_forever():
    if povoleno:
        basic.show_icon(iconNames.YES)
