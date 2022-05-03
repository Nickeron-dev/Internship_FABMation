from gpiozero import AngularServo
from time import sleep

PEN_HEIGHT_SERVO_PORT = 27
BASE_SERVO_PORT = 26
SHOULDER_SERVO_PORT = 22

base_servo = AngularServo(BASE_SERVO_PORT, min_pulse_width=0.0006, max_pulse_width=0.0023)
shoulder_servo = AngularServo(SHOULDER_SERVO_PORT, min_pulse_width=0.0006, max_pulse_width=0.0023)
pen_height_servo = AngularServo(PEN_HEIGHT_SERVO_PORT, min_pulse_width=0.0006, max_pulse_width=0.0023)

while (True):
	
