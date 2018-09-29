# Send random joystick data


import pygame
import spiDriver


def value_to_pwm(value):
    return 1500 + int(value / 0.002)


def main():
    pygame.init()
    # pygame.joystick.init()

    spi = spiDriver.init()

    try:
        while _running:
            # pygame.event.get()  # Ping for events
            inputs = value_to_pwm(15000)
            spiDriver.send(spi, inputs)
            print(inputs)
    except KeyboardInterrupt:
        spiDriver.close(spi)


if __name__ == '__main__':
    _running = True
    main()
