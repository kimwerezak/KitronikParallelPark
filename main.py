#Moves Kitronik robot forward.
Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD, 20)
basic.pause(1000)
Kitronik_Move_Motor.stop()

#Reverses to the right to move into parking spot.
Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_LEFT,
    Kitronik_Move_Motor.MotorDirection.REVERSE,
    15)
basic.pause(2000)
Kitronik_Move_Motor.stop()

#Reverses to left to straighten out.
Kitronik_Move_Motor.motor_on(Kitronik_Move_Motor.Motors.MOTOR_RIGHT,
    Kitronik_Move_Motor.MotorDirection.REVERSE,
    15)
basic.pause(2000)
Kitronik_Move_Motor.stop()