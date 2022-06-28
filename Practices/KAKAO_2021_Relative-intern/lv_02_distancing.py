def get_l1_norm(main_coord, sub_coord):
    x = abs(main_coord[0] - sub_coord[0])
    y = abs(main_coord[1] - sub_coord[1])

    # Calcutaing L1 norm
    if x + y == 0:
        return 0
    if x + y == 1:
        return 1
    elif x + y == 2:
        return 2
    elif x + y > 2:
        return 999

def is_partitioned(main_coord, sub_coord, x_arr):
    x1 = main_coord[0]
    y1 = main_coord[1]
    x2 = sub_coord[0]
    y2 = sub_coord[1]

    '''
    Cases:
        # of needed partitions
            # 1: Same x or y coord.
            # 2: Difference x or y coord.
    '''
    if x1 == x2 or y1 == y2: # n_n_partition == 1
        if x1 == x2 and y1 != y2: # Same x coord.
            p_x = x1

            if y2 > y1: # Top side
                p_y = y1 + 1
            elif y1 > y2: # Bottom side
                p_y = y1 - 1

            if (p_x, p_y) in x_arr:
                if p_x < 0 or p_y < 0:
                    return 0
                else:
                    return 1
            elif (p_x, p_y) not in x_arr:
                return 0
        elif y1 == y2 and x1 != x2: # Same y coord.
            p_y = y1

            if x2 > x1: # Right side
                p_x = x1 + 1
            elif x1 > x2: # Left side
                p_x = x1 - 1

            if (p_x, p_y) in x_arr:
                if p_x < 0 or p_y < 0:
                    return 0
                else:
                    return 1
            elif (p_x, p_y) not in x_arr:
                return 0
        else:
            print('Coord. error!')
            return False

    elif x1 != x2 and y1 != y2: # n_n_partition == 2
        if (x2 - x1 > 0) and (y2 - y1 > 0): # 1 in clock
            p1_x = x1
            p1_y = y1 + 1
            p2_x = x1 + 1
            p2_y = y1

            p1 = (p1_x, p1_y)
            p2 = (p2_x, p2_y)
        elif (x2 - x1 > 0) and (y2 - y1 < 0): # 5 in clock
            p1_x = x1 + 1
            p1_y = y1
            p2_x = x1
            p2_y = y1 - 1

            p1 = (p1_x, p1_y)
            p2 = (p2_x, p2_y)
        elif (x2 - x1 < 0) and (y2 - y1 < 0): # 7 in clock
            p1_x = x1 - 1
            p1_y = y1
            p2_x = x1
            p2_y = y1 - 1

            p1 = (p1_x, p1_y)
            p2 = (p2_x, p2_y)
        elif (x2 - x1 < 0) and (y2 - y1 > 0): # 11 in clock
            p1_x = x1
            p1_y = y1 + 1
            p2_x = x1 - 1
            p2_y = y1

            p1 = (p1_x, p1_y)
            p2 = (p2_x, p2_y)
        else:
            print('Coord. error!')
            return False

        if p1 in x_arr and p2 in x_arr:
            if p1_x < 0 or p1_y < 0 or p2_x < 0 or p2_y < 0:
                return 0
            else:
                return 1
        elif p1 not in x_arr and p2 not in x_arr:
            return 0
    else:
        print('Number of partition error!')
        return False


def solution(places):
    answer = []
    
    # Room loop
    for room in places:
        p_arr = [] # Fulled table
        o_arr = [] # Empty table
        x_arr = [] # Partition
        
        for i in range(0, 5): # Row
            for j in range(0, 5): # Info
                if room[i][j] == 'P':
                    p_arr.append((i, j))
                elif room[i][j] == 'O':
                    o_arr.append((i, j))
                elif room[i][j] == 'X':
                    x_arr.append((i, j))
                else:
                    print('Exception: Info error!')
                    return False

        # # Test codes for building array works
        # print(p_arr)
        # print(o_arr)
        # print(x_arr)
        # print('----------------------------')

        # Judging
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
                            elif l1_norm == 2: # TODO
                                partition_flag = is_partitioned(main_coord, sub_coord, x_arr)
                                if partition_flag:
                                    retval = 1
                                elif not partition_flag:
                                    retval = 0 
                                    break # Once 0 => Ends
                            else:
                                print('Exception: L1-norm error!')
                                return False
                        elif l1_norm >= 3:
                            retval = 1
                        else:
                            print('Exception: L1-norm error!')
                            return False

                if retval == 0: 
                    break # Once 0 => Ends
                    
        answer.append(retval)
  
    print(answer)
    return answer


solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
])