def solution(places):
    answer = []
    
    for room in places:
        # Get informations in room
        p_arr = []
        o_arr = []
        x_arr = []

        for i in range(0, 5): # n_row
            for j in range(0, 5): # n_info_in_row
                if room[i][j] == 'P':
                    p_arr.append((i, j))
                elif room[i][j] == 'O':
                    o_arr.append((i, j))
                else: # elif room[i][j] == 'X':
                    x_arr.append((i, j))

        # Main code
        if not p_arr: # No fulled tables
            retval = 1
        elif p_arr:
            for main_coord in p_arr: # Bubble checking
                for sub_coord in p_arr: # Call sub coords
                    if main_coord == sub_coord: # Pass same coord
                        continue
                    # Init comparing
                    else: # elif main_coord != sub_coord: 
                        # Get l1-norm
                        abs_x = abs(main_coord[0] - sub_coord[0])
                        abs_y = abs(main_coord[1] - sub_coord[1])

                        # Calcutaing L1 norm
                        if abs_x + abs_y == 1:
                            retval = 0
                            break
                        elif abs_x + abs_y == 2: # Main part of main code
                            main_x = main_coord[0]
                            main_y = main_coord[1]
                            sub_x = sub_coord[0]
                            sub_y = sub_coord[1]

                            '''
                            Cases:
                                # of needed partition(s)
                                    1: Same x or y coord.
                                    2: Difference x and y coord.
                            '''
                            if main_x == sub_x or main_y == sub_y: # Needed partition: 1
                                if main_x == sub_x and main_y != sub_y: # Same x coord., Top or Bottom-side
                                    partition_x = main_x # == sub_x

                                    if main_y < sub_y: # Sub coord. placed at Top-side
                                        partition_y = main_y + 1
                                    # Sub coord. placed at Bottom-side 
                                    else: # elif main_y > sub_y: 
                                        partition_y = main_y - 1

                                    if (partition_x, partition_y) in x_arr:
                                        retval = 1
                                    else: # elif (partition_x, partition_y) not in x_arr:
                                        retval = 0
                                        break
                                # Same y coord., Left or Right-side
                                else: # elif main_x != sub_x and main_y == sub_y: 
                                    partition_y = main_y # == sub_y

                                    if main_x < sub_x: # Sub coord. placed at Right-side
                                        partition_x = main_x + 1
                                    elif main_x > sub_x: # Sub coord. placed at Left-side
                                        partition_x = main_x - 1

                                    if (partition_x, partition_y) in x_arr:
                                        retval = 1
                                    else: # elif (p_x, p_y) not in x_arr:
                                        retval = 0
                                        break
                            # Needed partition: 2
                            else: # elif main_x != sub_x and main_y != sub_y: 
                                left_side = main_x > sub_x
                                right_side = main_x < sub_x
                                top_side = main_y < sub_y
                                bottom_side = main_y > sub_y

                                if right_side and top_side: # 1 o'clock
                                    p1_x = main_x
                                    p1_y = main_y + 1
                                    p2_x = main_x + 1
                                    p2_y = main_y

                                    p1 = (p1_x, p1_y)
                                    p2 = (p2_x, p2_y)
                                elif right_side and bottom_side: # 5 o'clock
                                    p1_x = main_x + 1
                                    p1_y = main_y
                                    p2_x = main_x
                                    p2_y = main_y - 1

                                    p1 = (p1_x, p1_y)
                                    p2 = (p2_x, p2_y)
                                elif left_side and bottom_side: # 7 o'clock
                                    p1_x = main_x - 1
                                    p1_y = main_y
                                    p2_x = main_x
                                    p2_y = main_y - 1

                                    p1 = (p1_x, p1_y)
                                    p2 = (p2_x, p2_y)
                                else: # elif left_side and top_side: # 11 o'clock
                                    p1_x = main_x
                                    p1_y = main_y + 1
                                    p2_x = main_x - 1
                                    p2_y = main_y

                                    p1 = (p1_x, p1_y)
                                    p2 = (p2_x, p2_y)

                                if (p1 in x_arr) and (p2 in x_arr):
                                    retval = 1
                                else:
                                    retval = 0
                                    break
                        else: # elif abs_x + abs_y >= 3:
                            retval = 1

                if retval == 0: 
                    break # Once 0 => Ends    
                    
        answer.append(retval)
  
    # print(answer)
    return answer


# solution([
#     ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
#     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
#     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
#     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
#     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
# ])