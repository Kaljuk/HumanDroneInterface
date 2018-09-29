import pygame


def value_to_pwm(value):
    return 1500 + int(value / 0.002)


def get_inputs_as_pwm():

    # we have only one joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    roll = round(joystick.get_axis(0), 3)
    pitch = round(joystick.get_axis(1), 3)
    height = round(joystick.get_axis(2), 3)
    yaw = round(joystick.get_axis(3), 3)
    btn1 = joystick.get_button(0)
    btn2 = joystick.get_button(1)

    pwm_inputs = []
    pwm_inputs.append(value_to_pwm(roll))
    pwm_inputs.append(value_to_pwm(pitch))
    pwm_inputs.append(value_to_pwm(height))
    pwm_inputs.append(value_to_pwm(yaw))
    pwm_inputs.append(value_to_pwm(btn1))
    pwm_inputs.append(value_to_pwm(btn2))

    return [pwm_inputs]


def main():
    pygame.init()
    pygame.joystick.init()

    while _running:
        pygame.event.get()  # Ping for events
        print(get_inputs_as_pwm())


if __name__ == '__main__':
    _running = True
    main()


