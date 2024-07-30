def find_volume(length=1, width=1, depth=1):
    return length * width * depth, ' m3', width * depth, ' m2' 

if __name__ == "__main__":

    first_volume = find_volume(2, 4, 7) 
    print(first_volume)

    second_volume, unidad3, firs_area, unidad2 = find_volume(6, 5, 9)
    print(second_volume, unidad3)
    print(firs_area, unidad2)
