def get_pox_arr(room):
    p_arr = []
    o_arr = []
    x_arr = []

    for i in range(0, 5): # n_row
        for j in range(0, 5): # n_info_in_row
            if room[i][j] == 'P':
                p_arr.append((i, j))
            elif room[i][j] == 'O':
                o_arr.append((i, j))
            elif room[i][j] == 'X':
                x_arr.append((i, j))
            else:
                print('Exception: Info error!')
                return False
                
    return p_arr, o_arr, x_arr


def get_l1_norm(main_coord, sub_coord):
    x = abs(main_coord[0] - sub_coord[0])
    y = abs(main_coord[1] - sub_coord[1])

    # Calcutaing L1 norm
    if x + y == 0:
        return 0
    elif x + y == 1:
        return 1
    elif x + y == 2:
        return 2
    elif x + y > 2:
        return 999
    else:
        print('Error: get_l1_norm()')
        return False


def is_partitioned(main_coord, sub_coord, x_arr):
    main_x = main_coord[0]
    main_y = main_coord[1]
    sub_x = sub_coord[0]
    sub_y = sub_coord[1]

    '''
    Cases:
        # of needed partition(s)
            1: Same x or y coord.
            2: Difference x or y coord.
    '''
    if main_x == sub_x or main_y == sub_y: # Needed partition: 1
        if main_x == sub_x and main_y != sub_y: # Same x coord.
            p_x = main_x # == sub_x

            if main_y < sub_y: # Top side
                p_y = main_y + 1
            elif main_y > sub_y: # Bottom side
                p_y = main_y - 1
            else:
                print('Error: Same x coord., same y coord.')
                return False

            if (p_x, p_y) in x_arr:
                return 1
            elif (p_x, p_y) not in x_arr:
                # print(x_arr)
                # print(f'X: Error: (p_x, p_y) not in not not in x_arr {p_x},{p_y}')
                # print(f'main coord.{main_x, main_y}, sub coord. {sub_x, sub_y}')
                return 0
            else:
                print(f'Error: (p_x, p_y) not in not not in x_arr {p_x},{p_y}')
                return False

        elif main_x != sub_x and main_y == sub_y: # Same y coord.
            p_y = main_y # == sub_y

            if main_x < sub_x: # Right side
                p_x = main_x + 1
            elif main_x > sub_x: # Left side
                p_x = main_x - 1

            if (p_x, p_y) in x_arr:
                return 1
            elif (p_x, p_y) not in x_arr:
                # print(x_arr)
                # print(f'Y: Error: (p_x, p_y) not in not not in x_arr {p_x},{p_y}')
                # print(f'main coord.{main_x, main_y}, sub coord. {sub_x, sub_y}')
                return 0
            else:
                print(f'Error: (p_x, p_y) not in not not in x_arr {p_x},{p_y}')
                return False

        else: # Exception
            print('Coord. error!')
            return False
    elif main_x != sub_x and main_y != sub_y: # Needed partition: 2
        left_side = main_x > sub_x
        right_side = main_x < sub_x
        top_side = main_y < sub_y
        bottom_side = main_y > sub_y

        if right_side and top_side: # 1 in clock
            p1_x = main_x
            p1_y = main_y + 1
            p2_x = main_x + 1
            p2_y = main_y

            p1 = (p1_x, p1_y)
            p2 = (p2_x, p2_y)
        elif right_side and bottom_side: # 5 in clock
            p1_x = main_x + 1
            p1_y = main_y
            p2_x = main_x
            p2_y = main_y - 1

            p1 = (p1_x, p1_y)
            p2 = (p2_x, p2_y)
        elif left_side and bottom_side: # 7 in clock
            p1_x = main_x - 1
            p1_y = main_y
            p2_x = main_x
            p2_y = main_y - 1

            p1 = (p1_x, p1_y)
            p2 = (p2_x, p2_y)
        elif left_side and top_side: # 11 in clock
            p1_x = main_x
            p1_y = main_y + 1
            p2_x = main_x - 1
            p2_y = main_y

            p1 = (p1_x, p1_y)
            p2 = (p2_x, p2_y)
        else:
            print('Error: Main and sub coord.')
            return False

        if (p1 in x_arr) and (p2 in x_arr):
            return 1
        else:
            return 0
    else:
        print('Error: Main, sub coord.')
        return False


def main(p_arr, x_arr):
    if not p_arr: # No fulled tables
        retval = 1
    elif p_arr:
        for main_coord in p_arr: # Bubble checking
            for sub_coord in p_arr: # Call sub coords
                if main_coord == sub_coord: # Pass same coord
                    continue
                elif main_coord != sub_coord: # Init comparing
                    l1_norm = get_l1_norm(main_coord, sub_coord)

                    if l1_norm <= 2:
                        if l1_norm == 0 or l1_norm == 1:
                            retval = 0
                            break # Once 0 => Ends
                        elif l1_norm == 2: # Main part
                            partition_passed = is_partitioned(main_coord, sub_coord, x_arr)

                            if partition_passed:
                                retval = 1
                            elif not partition_passed:
                                retval = 0
                                break # Once 0 => Ends
                        else:
                            print('Exception: L1-norm error!')
                            return False
                    elif l1_norm >= 3:
                        retval = 1
                    else:
                        print('Exception: Maybe L1-norm is minus value')
                        return False
                else:
                    print('Error: main_coord is not diff. and same with sub_coord!')
                    return False

            if retval == 0: 
                break # Once 0 => Ends    

    return retval


def solution(places):
    answer = []
    
    for room in places:
        p_arr, o_arr, x_arr = get_pox_arr(room)
        print(p_arr)
        print(x_arr)
        print('------------------------------------------------------------')

        retval = main(p_arr, x_arr)
                    
        answer.append(retval)
  
    # print(answer)
    return answer


solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
])