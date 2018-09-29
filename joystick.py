import inputDriver
import sys


def main():
    inputDrv = inputDriver.InputDriver()

    try:
        while _running:
            inputs = inputDrv.get_pwm_inputs()
            print (inputs)
    except KeyboardInterrupt:
		sys.exit(-1)

if __name__ == '__main__':
    _running = True
    main()
