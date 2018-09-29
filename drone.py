# joystick receiver - subMaster

import pygame
import spiDriver





def main():
    pygame.init()
    pygame.joystick.init()

    spi = spiDriver.init()

    try:
        while _running:            
            spiDriver.read(spi)

if __name__ == '__main__':
    _running = True
    main()
