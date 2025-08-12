import random

maze = [['#', '!', '.', '.', 'R', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '#', '.', 'H', '.', '.', '.', '.', '.', '!'],
        ['F', '.', '.', '.', '#', '.', '!', '.', '.', 'R', '.', '.', '#', '#', '.'],
        ['.', '.', '#', '.', '.', '#', '.', '.', '.', '.', 'F', '.', '.', '.', '.'],
        ['.', '!', '.', '.', '#', '.', '#', '.', '#', '.', '.', '#', '.', '.', '.'],
        ['.', '.', 'H', '.', '.', '!', '.', '.', 'H', '.', '.', 'F', '.', '.', 'R'],
        ['#', '#', '#', '#', '.', '.', '#', '.', '.', '.', 'T', '.', '.', '.', 'E'],
        ['.', '.', '#', '.', 'F', '.', '#', '#', '.', '#', '#', '#', '#', '.', '.'],
        ['.', '#', '.', '.', '.', '.', '!', '.', '#', '.', '.', '.', '#', '.', '.'],
        ['.', 'T', 'T', '.', '#', '#', '.', '.', '.', '.', 'T', '.', '.', '.', 'R'],
        ['.', '.', '.', '#', '.', '.', '.', '#', '.', '#', '.', '#', '.', 'T', '.'],
        ['B', '.', '#', '.', '.', '!', '.', '!', '.', '.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', 'F', '!', '.', '.', '.', 'H', '.', '.', 'R', '.', '.', '.'],
        ['.', '.', 'H', '.', '.', '.', '!', '.', '.', '.', '#', '.', '.', '#', '.'],
        ['.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '#', '.', '.', '#', '#']]


def find_start_and_end(maze):
    start = end = None
    for row_idx, row in enumerate(maze): 
        for col_idx, cell in enumerate(row):
            if cell == 'B':
                start = (row_idx, col_idx)
            elif cell == 'E':
                end = (row_idx, col_idx)
    return start, end
            

def move(location, direction, moves, bonus_list):
    while True:  
        if direction not in ['w','a','s','d','W','A','S','D', '+', 'exit','EXIT']:
            print("Geçersiz giriş yaptınız. Lütfen w/a/s/d, '+' veya 'exit' girin.")
            direction = input("Hareket için(w/a/s/d) Bonus kullanmak için(+) girin, Çıkmak için (exit) girin: ")
            continue
        row, col = location
        new_row, new_col = row, col

        if direction == 'w' or direction == 'W':
            new_row -= 1
        elif direction == 's' or direction == 'S':
            new_row += 1
        elif direction == 'a' or direction == 'A':
            new_col -= 1
        elif direction == 'd' or direction == 'D':
            new_col += 1
        elif direction == '+':
            location, moves, bonus_list = use_bonus(bonus_list, moves, location)
            return location, moves, bonus_list


        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            if maze[new_row][new_col] == '#':
                print("\nDuvarla karşılaştınız. R bonusunu kullanabilirsiniz.")
                location, moves, bonus_list = remove_wall(location, moves, bonus_list, new_row, new_col)
            elif maze[new_row][new_col] == '!':
                print("\nMayınla karşılaştınız. F bonusunu kullanabilirsiniz.")
                location, moves, bonus_list = defuse_mine(location, moves, bonus_list,new_row, new_col)
            elif maze[new_row][new_col] in ['T', 'R', 'F', 'H']:
                bonus_list.append(maze[new_row][new_col])
                print(f"\n{maze[new_row][new_col]} bonusu kazandınız.")
                maze[new_row][new_col] = '.'
                location = (new_row, new_col)
                moves += 1 
            else:
                location = (new_row, new_col)
                moves += 1 
        else:
            print("Sınır dışına çıkamazsınız.")

        return location, moves, bonus_list
    

def use_bonus(bonus_list, moves, location):
    if 'T' not in bonus_list and 'R' not in bonus_list and 'F' not in bonus_list and 'H' not in bonus_list:
        print("\nBonus Listesi:", bonus_list)
        print("Bonus bulunmamaktadır.")
        return location, moves, bonus_list
    while True:
        print("Bonus Listesi:", bonus_list)
        print("Kullanmak istediğiniz bonusu girin:")
        selected_bonus = input()
        selected_bonus_upper = ""
        for char in selected_bonus:
            if 'a' <= char <= 'z':
                selected_bonus_upper += chr(ord(char) - 32)
            else:
                selected_bonus_upper += char

        if selected_bonus_upper in bonus_list:
            if selected_bonus_upper == 'R':
                print("\nDuvarla karşılaşmadıysanız R bonusunu kullanamazsınız.") 
            elif selected_bonus_upper == 'F':
                print("\nMayınla karşılaşmadıysanız F bonusunu kullanamazsınız.")
            else:
                location, moves, bonus_list = t_h_bonus(location, selected_bonus_upper, moves, bonus_list)
            return location, moves, bonus_list
        else:
            print("Bonus listede bulunamadı. Lütfen tekrar deneyin.")
            continue


def remove_wall(location, moves, bonus_list, new_row, new_col):
    row, col = location
    if 'R' in bonus_list:
        maze[new_row][new_col] = '.'
        print("\nDuvar kaldırıldı")
        return (new_row, new_col), moves + 1, bonus_list
    else:
        print("R bonusunuz olmadığı için duvar kaldırılamadı.")
        return (row, col), moves, bonus_list



def defuse_mine(location, moves, bonus_list,new_row, new_col):
    row, col = location
    if "F" in bonus_list:
        maze[new_row][new_col] = '.'
        print("Mayın imha edildi")
        for index, bonus in enumerate(bonus_list):
            if bonus == 'F':
                bonus_list[index] = '.'
                break
        return (new_row, new_col), moves + 1, bonus_list
    else:
        maze[new_row][new_col] = '.'
        print("F bonusu olmadığı için MAYIN PATLADI")
        return (row, col), moves + 5, bonus_list

    
def t_h_bonus(location, bonus, moves, bonus_list):
    if bonus == 'T':
        for index, bonus in enumerate(bonus_list):
            if bonus == 'T':
                bonus_list[index] = '.'
                break
        while True:
            print("Yeni bir konum belirtin (x, y):")
            new_pos = input()
            if ',' not in new_pos:
                print("\nLütfen doğru formatta (x,y) girin.")
                continue
            comma_idx = new_pos.index(',')
            new_x = int(new_pos[:comma_idx])
            new_y = int(new_pos[comma_idx + 1:])
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]):
                if maze[new_x][new_y] == '!':
                    print("\nIşınlandığınız konumda bir mayın var. Lütfen tekrar deneyin.")
                    continue
                elif maze[new_x][new_y] == '#':
                    print("\nIşınlandığınız konumda bir duvar var. Lütfen tekrar deneyin.")
                    continue
                else:
                    if maze[new_x][new_y] in ['T', 'R', 'F', 'H']:
                        bonus_list.append(maze[new_x][new_y])
                        print(f"\n{maze[new_x][new_y]} bonusu kazandınız.")
                        maze[new_x][new_y] = '.'
                    return (new_x, new_y), moves, bonus_list
            else:
                print("\nGeçersiz bir konum girdiniz. Lütfen tekrar deneyin.")
                continue

    elif bonus == 'H':
        for index, bonus in enumerate(bonus_list):
            if bonus == 'H':
                bonus_list[index] = '.'
                break
        if moves >= 2:
            print("\nHamle sayısı iki azaltıldı.")
            return location, moves - 2, bonus_list
        else:
            print("\nHamle sayısı negatif değer olamaz.")
    else:
        print("Bonus listede bulunamadı.")
        return location, moves, bonus_list
    

def redistribute_mine(maze, moves):
    num_rows = len(maze)
    num_cols = len(maze[0])
    mine_count = sum(row.count('!') for row in maze)

    if moves > 0 and moves % 5 == 0:
        for row_idx, row in enumerate(maze):
            for col_idx, cell in enumerate(row):
                if cell == '!':
                    while True:
                        new_x = random.randint(0, num_rows - 1)
                        new_y = random.randint(0, num_cols - 1)
                        if maze[new_x][new_y] not in ['#','!', 'B', 'E','T', 'R', 'F', 'H']:
                            maze[row_idx][col_idx] = '.'
                            maze[new_x][new_y] = '!'
                            break
                    break #herseferinde yalnızca bir mayın
    return maze


def redistribute_bonus(maze, moves):
    num_rows = len(maze)  
    num_cols = len(maze[0])  
    bonus_count = sum(row.count('T') + row.count('R') + row.count('F') + row.count('H') for row in maze)  

    if moves > 0 and moves % 5 == 0:
        for x in range(num_rows):
            for y in range(num_cols):
                 if maze[x][y] in ['T', 'R', 'F', 'H']:
                    bonus = maze[x][y]
                    maze[x][y] = '.'
                    while True:
                        new_x = random.randint(0, num_rows - 1)
                        new_y = random.randint(0, num_cols - 1)
                        if maze[new_x][new_y] not in ['#', '!', 'B', 'E','T', 'R', 'F', 'H']:
                            maze[new_x][new_y] = bonus
                            break
                        else:
                            continue
    return maze


#TEST
start, end = find_start_and_end(maze)
print("MAZE GAME:")
print("Başlangıç Noktası:", start)

location = start
moves = 0
bonus_list = []

while True:
    maze = redistribute_mine(maze, moves)
    maze = redistribute_bonus(maze, moves)
    print("Labirent Durumu:")
    for row in maze:
        row_str = ""
        for cell in row:
            row_str += cell + " "
        print(row_str)
    
    direction = input("Hareket için(w/a/s/d) Bonus kullanmak için(+) girin, Çıkmak için (exit) girin: ")

    if direction == 'exit' or direction == 'EXIT':
        print("\nOyundan çıkış yaptınız.")
        print("Toplam Hamle Sayısı:", moves)
        break

    location, moves, bonus_list = move(location, direction, moves, bonus_list)
    print(f"\nKarakterin Yeni Konumu: ({location[0]}, {location[1]})")
    print("Hamle Sayısı:", moves)
   
    if location == end:
        print("\nÇıkış noktasına ulaşıldı. Tebrikler!")
        print("Toplam Hamle Sayısı:", moves)
        break