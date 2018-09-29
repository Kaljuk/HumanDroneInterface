import pygame


class InputDriver:
	def __init__(self):
		pygame.init()
		pygame.joystick.init()
		self.joystick = pygame.joystick.Joystick(0)
		self.joystick.init()


	def value_to_pwm(self, value):
		return 1500 + int(value / 0.002)
    
    
	def get_pwm_inputs(self):
		#important to ping for events
		pygame.event.get() 
		
		#new stuff
		roll = round(self.joystick.get_axis(0), 3)
		pitch = round(self.joystick.get_axis(1), 3)
		height = round(self.joystick.get_axis(2), 3)
		yaw = round(self.joystick.get_axis(3), 3)
		btn1 = self.joystick.get_button(0)
		btn2 = self.joystick.get_button(1)
		
		pwm_inputs = []
		pwm_inputs.append(self.value_to_pwm(roll))
		pwm_inputs.append(self.value_to_pwm(pitch))
		pwm_inputs.append(self.value_to_pwm(height))
		pwm_inputs.append(self.value_to_pwm(yaw))
		pwm_inputs.append(self.value_to_pwm(btn1))
		pwm_inputs.append(self.value_to_pwm(btn2))

		return pwm_inputs
