import brian.sensors as sensors
import brian.motors as motors
from time import sleep

# MOTORS
motor_a =motors.EV3LargeMotor(motors.MotorPort.A)
motor_a.wait_until_ready()
motor_b =motors.EV3LargeMotor(motors.MotorPort.D)
motor_b.wait_until_ready()

motor_a.run_at_speed(300)
motor_b.run_at_speed(300)

# SENSOR
CS = sensors.EV3.ColorSensorEV3(sensors.SensorPort.S1)
CS.set_mode(CS.Mode(4)) # set RGB_RAW mode
CS.wait_until_ready() # wait until sensor is ready

left = True
while(True):
 # STOP
 motor_a.brake()
 motor_b.brake()

 # DRIVE IF BLACK

 while (CS.rgb_values_raw()[0] < 400 ):
  motor_a.run_at_speed(300)
  motor_b.run_at_speed(300)
 
  sleep(0.1)
 
 if (left):
   motor_a.rotate_by_angle(100, 100, False)
   motor_b.rotate_by_angle(-100, 100)
   if (CS.rgb_values_raw()[0] > 400 ):
    left = False

 else:
   motor_a.rotate_by_angle(-100, 100, False)
   motor_b.rotate_by_angle(100, 100)
   if (CS.rgb_values_raw()[0] > 400 ):
    left = True

