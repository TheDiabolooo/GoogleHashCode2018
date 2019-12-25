import Vehicule as Vehicule
import Map as Map
import Ride as Ride

steps = 0
file = "inputfile.txt"

with open(file, 'r') as inputFile:
    data = inputFile.readline().split()
    myMap = Map.Map(int(data[0]), int(data[1]), int(data[4]), int(data[2]), int(data[3]))

    ride = []
    for line in inputFile:
        data = line.split()
        ride.append(Ride.Ride(data[0], data[1], data[2], data[3], data[4], data[5]))
    ride.sort(key = lambda P:min(P.s))

    vehicules = []
    for n in range(myMap.vehicule):
        vehicules.append(Vehicule.Vehicule(0, 0, ride[n], True, 0))
        del ride[n]


    while myMap.ride != 0:
        for vehicule in vehicules:
            if vehicule.available == True:
                if vehicule.x < int(vehicule.ride.a):
                    vehicule.x += 1
                    vehicule.step += 1
                elif vehicule.x > int(vehicule.ride.a):
                    vehicule.x -= 1
                    vehicule.step += 1
                elif vehicule.y < int(vehicule.ride.b):
                    vehicule.y +=1
                    vehicule.step += 1
                elif vehicule.y > int(vehicule.ride.b):
                    vehicule.y -= 1
                    vehicule.step += 1
                else:
                    vehicule.available = False
                    

            else:
                if vehicule.x < int(vehicule.ride.x):
                    vehicule.x += 1
                    vehicule.step += 1
                elif vehicule.x > int(vehicule.ride.x):
                    vehicule.x -= 1
                    vehicule.step += 1
                elif vehicule.y < int(vehicule.ride.y):
                    vehicule.y +=1
                    vehicule.step += 1
                elif vehicule.y > int(vehicule.ride.y):
                    vehicule.y -= 1
                    vehicule.step += 1
                else:
                    vehicule.available = True
                    step = (abs(int(vehicule.ride.x)-int(vehicule.ride.a))+abs(int(vehicule.ride.y)-int(vehicule.ride.b)))+(abs(int(vehicule.ride.a)-vehicule.x)+abs(int(vehicule.ride.b)-vehicule.y))
                    vehicules.append(Vehicule.Vehicule(int(vehicule.ride.x), int(vehicule.ride.y), ride[0], True, step))
                    print(vehicule.ride.a, vehicule.ride.b, vehicule.ride.x, vehicule.ride.y, vehicule.step)
                    myMap.ride -= 1

        steps += 1
            

        
