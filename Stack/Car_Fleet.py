def carFleet(target, position, speed):
    pos_speed_dict = {}
    for i in range(len(speed)):
        pos_speed_dict[position[i]]=speed[i]
    
    sort_pos=sorted(position)
    time_taken=[]
    for i in range(len(sort_pos)):
        time_taken.append((target - sort_pos[i])/pos_speed_dict[sort_pos[i]])
    car_fleet = len(position)
    pointer = len(position)-1
    curr_time = time_taken[pointer]
    while pointer != 0:
        pointer-=1
        if time_taken[pointer]<=curr_time:
            car_fleet-=1
        else:
            curr_time = time_taken[pointer]
    return car_fleet

if __name__ == "__main__":
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print("target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]")
    print(carFleet(target,position,speed))