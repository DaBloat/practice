def dir_reduc(arr):
    check = [['NORTH','SOUTH'],['SOUTH','NORTH'],['WEST','EAST'],['EAST','WEST']]
    reduc = False
    pointer = 0
    indx = 0
    while not reduc:
        try:
            print(arr)
            print(indx, pointer)
            if pointer == indx:
                pointer += 1
            elif [arr[indx],arr[pointer]] in check:
                print([arr[indx],arr[pointer]])
                arr.pop(indx)
                arr.pop(pointer-1)
                indx = 0
                pointer = 0
                print(arr)
            else:
                if len(arr) != 1:
                    indx += 1
        except IndexError:
            reduc = True
    return arr


# print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dir_reduc(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH", "SOUTH", "NORTH","WEST", "EAST"]))
