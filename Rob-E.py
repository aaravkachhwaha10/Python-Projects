import time

battery = 100
print("Robot starting... Battery at 100%.")
while battery > 15:
    print("Robot is performing actions...")
    time.sleep(1)

    print("Walking...")
    time.sleep(1)
    battery -= 10

    print("Jumping...")
    time.sleep(1)
    battery-=5

    print ("Scanning the area...")
    time.sleep(1)
    battery-=8

    print("Picking up an object...")
    time.sleep(1)
    battery-=7

    print("Battery level:", battery, "%")
    time.sleep(1)

    if battery <= 15:
        print ("Battery Low!(", battery, "%)")
        choice = input("Do you want to recharge the robot? (yes/no)").lower()

        if choice == "yes":
            print ("Recharging battery...")
            time.sleep(2)
            battery = 100
            print("Battery recharged. Current level: 100%")
        else:
            print("Shutting down the robot. Goodbye!")
            break