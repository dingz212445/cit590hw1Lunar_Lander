"""Lunar Lander game with Python"""
def lunar_lander():
    altitude = 1000
    fuel = 1000
    velocity = 0
    while altitude > 0:
        t = int(input("how many seconds passed?\n"))
        while t >= 0:
            altitude = altitude - velocity
            velocity = velocity + 1.6
            if altitude <= 0:
                break
            t = t - 1
        print("altitude:", altitude, "\n velocity:", velocity, "\n fuel:", fuel, "\n")
        if altitude <= 0:
            break
        fuel_burn = int(input("how much fuel to burn?\n"))
        if fuel_burn > fuel:
            fuel_burn = fuel
        fuel = fuel - fuel_burn
        velocity = velocity - fuel_burn * 0.15
    if velocity > 10:
        print("crashed.\n")
    else:
        print("landed.\n")

def play_again():
    again = int(input("Want to try again?(1-yes,0-no)\n"))
    while again != 1 and again != 0:
        again = int(input("Want to try again?(1-yes,0-no)\n"))
    return again

def main():
    lunar_lander()
    while play_again() == 1:
        lunar_lander()
        

if __name__ == "__main__":
    main()
