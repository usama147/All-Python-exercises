avgspeed = float(input("enter avg speed "))
speed = int(input("enter speed "))
if speed >= 65:
    demerit_points = (speed - avgspeed) // 5
    print(demerit_points)
    if demerit_points > 12:
        print("Time to go to Jail")
else:
    print("OK")
