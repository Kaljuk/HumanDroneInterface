from inputDriver import InputDriver
from serialDriver import SerialDriver
import sys


def main():
    
	inputDrv = InputDriver()
	serDrv = SerialDriver()
	try:
		while _running:
			inputs = inputDrv.get_pwm_inputs()
			print (inputs)
			serDrv.write(str(inputs))
			
	except KeyboardInterrupt:
		sys.exit(-1)
		
if __name__ == '__main__':
    _running = True
    main()
