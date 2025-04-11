// Moves Kitronik robot forward.
Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.Forward, 20)
basic.pause(1000)
Kitronik_Move_Motor.stop()
// Reverses to the right to move into parking spot.
Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorLeft, Kitronik_Move_Motor.MotorDirection.Reverse, 15)
basic.pause(2000)
Kitronik_Move_Motor.stop()
// Reverses to left to straighten out.
Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorRight, Kitronik_Move_Motor.MotorDirection.Reverse, 15)
basic.pause(2000)
Kitronik_Move_Motor.stop()
