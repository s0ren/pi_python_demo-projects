print("Hej Søren, eller andre... fra smagpi")

from sense_hat import SenseHat

sense = SenseHat()

while True:
    sense.show_message("Godformiddag til hele 22104p!", 0.03)
