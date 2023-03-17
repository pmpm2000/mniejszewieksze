# w krotce (int, list, list) pierwsza lista to od czego jest wieksze, a druga mniejsze
# kierunki: 1 - gora, 2 - prawo, 3 - dol, 4 - lewo
# (2, [1,2], [3,4]) - pole to liczba 2 i jest wieksza od liczby na gorze i prawej,
# a mniejsza od liczby na dole i lewej
def create_list(file1, file2, file3):
    # liczby
    zerocount = 0
    data = list()
    with open(file1) as f1:
        for line in f1:
            row = line.split(";")
            temp = list()
            for i in row:
                temp.append([int(i), list(), list()])
                if i == "0": zerocount += 1
            data.append(temp)
    size = len(data)
    f1.close()

    # wieksze/mniejsze w wierszach
    f2 = open(file2)
    for i in range(size):
        line = f2.readline()
        for j in range(size-1):
            if line[j] == "<":
                data[i][j][2].append(2)
                data[i][j+1][1].append(4)
            elif line[j] == ">":
                data[i][j][1].append(2)
                data[i][j+1][2].append(4)
    f2.close()

    # wieksze/mniejsze w kolumnach
    f3 = open(file3)
    for i in range(size-1):
        line = f3.readline()
        for j in range(size):
            if line[j] == "g":
                data[i][j][2].append(3)
                data[i+1][j][1].append(1)
            elif line[j] == "d":
                data[i][j][1].append(3)
                data[i+1][j][2].append(1)
    f3.close()
    return [data, zerocount]


def solve1():
# sprawdzanie jakie liczby sa juz w kolumnie lub wierszu
    for i in range(main_size):
        for j in range(main_size):
            if main_data[i][j][0] == 0:
                for k in range(main_size):
                    num = main_data[i][k][0]
                    try:
                        possibilities[i][j].remove(num)
                        print(i, j, "nie moze byc", num, "bo juz jest w wierszu")
                    except:
                        pass
                for k in range(main_size):
                    num = main_data[k][j][0]
                    try:
                        possibilities[i][j].remove(num)
                        print(i, j, "nie moze byc", num, "bo juz jest w kolumnie")
                    except:
                        pass


def solve2():
# jesli jest mniejsze od czegos to nie moze byc max (max z dostepnych)
# analogicznie z min
    for i in range(main_size):
        for j in range(main_size):
            if main_data[i][j][0] == 0:
                bigger = main_data[i][j][1]
                if bigger:
                    if (1 in bigger and 3 in bigger) or (2 in bigger and 4 in bigger):
                        try:
                            possibilities[i][j].remove(2)
                            print(i, j, "nie moze byc 2 bo ma byc wieksza")
                        except:
                            pass
                    try:
                        possibilities[i][j].remove(1)
                        print(i, j, "nie moze byc 1 bo ma byc wieksza")
                    except:
                        pass

                smaller = main_data[i][j][2]
                if smaller:
                    if (1 in smaller and 3 in smaller) or (2 in smaller and 4 in smaller):
                        try:
                            possibilities[i][j].remove(main_size-1)
                            print(i, j, "nie moze byc", main_size-1, "bo ma byc mniejsza")
                        except:
                            pass
                    try:
                        possibilities[i][j].remove(main_size)
                        print(i, j, "nie moze byc", main_size, "bo ma byc mniejsza")
                    except:
                        pass
# do dorobienia - jesli w rzedzie (ale nie obok!) jest 6 a liczba jest od czegos mniejsza to usuwamy opcje 5


def solve3(zerocount):
# jesli w wierszu lub kolumnie jest tylko raz to wpisac, jak lista ma 1 element to wpisac
    for i in range(main_size):
        cnt = [0] * (main_size+1)
        for j in range(main_size):
            for k in range(main_size+1):
                cnt[k] += possibilities[i][j].count(k)
        for j in range(len(cnt)):
            #print(j, "wystapila", cnt[j], "razy w", i)
            if cnt[j] == 1:
                for k in range(main_size):
                    if j in possibilities[i][k] and not main_data[i][k][0]:
                        main_data[i][k][0] = j
                        print("Set element", i, k, "to", j)
                        zerocount -= 1
    for i in range(main_size):
        cnt = [0] * (main_size+1)
        for j in range(main_size):
            for k in range(main_size+1):
                cnt[k] += possibilities[j][i].count(k)
        for j in range(len(cnt)):
            #print(j, "wystapila", cnt[j], "razy w", i)
            if cnt[j] == 1:
                for k in range(main_size):
                    if j in possibilities[k][i] and not main_data[k][i][0]:
                        main_data[k][i][0] = j
                        print("Set element", k, i, "to", j)
                        zerocount -= 1
    for i in range(main_size):
        for j in range(main_size):
            if len(possibilities[i][j]) == 1 and not main_data[i][j][0]:
                main_data[i][j][0] = possibilities[i][j][0]
                print("Set element", i, j, "to", possibilities[i][j][0])
                zerocount -= 1
    refresh_numbers()
    return zerocount


def solve4():
# wykreslanie niewlasciwych przedzialow (mniejsze od 4 -> skreslamy wszystkie wieksze i rowne)
    for i in range(main_size):
        for j in range(main_size):
            for k in main_data[i][j][1]:
                if k == 1 and main_data[i-1][j][0]:
                    for l in range(main_data[i-1][j][0] + 1):
                        try:
                            possibilities[i][j].remove(l)
                            print(i, j, "nie moze byc", l, "bo ma byc wieksza od", main_data[i-1][j][0])
                        except:
                            pass
                if k == 2 and main_data[i][j+1][0]:
                    for l in range(main_data[i][j+1][0] + 1):
                        try:
                            possibilities[i][j].remove(l)
                            print(i, j, "nie moze byc", l, "bo ma byc wieksza od", main_data[i][j+1][0])
                        except:
                            pass
                if k == 3 and main_data[i+1][j][0]:
                    for l in range(main_data[i+1][j][0] + 1):
                        try:
                            possibilities[i][j].remove(l)
                            print(i, j, "nie moze byc", l, "bo ma byc wieksza od", main_data[i+1][j][0])
                        except:
                            pass
                if k == 4 and main_data[i][j-1][0]:
                    for l in range(main_data[i][j-1][0] + 1):
                        try:
                            possibilities[i][j].remove(l)
                            print(i, j, "nie moze byc", l, "bo ma byc wieksza od", main_data[i][j-1][0])
                        except:
                            pass
            for k in main_data[i][j][2]:
                if k == 1 and main_data[i-1][j][0]:
                    for l in range(main_data[i-1][j][0], main_size):
                        try:
                            possibilities[i][j].remove(l)
                            print(i, j, "nie moze byc", l, "bo ma byc mniejsza od", main_data[i - 1][j][0])
                        except:
                            pass
                if k == 2 and main_data[i][j+1][0]:
                    for l in range(main_data[i][j+1][0], main_size):
                        try:
                            possibilities[i][j].remove(l)
                            print(i, j, "nie moze byc", l, "bo ma byc mniejsza od", main_data[i][j+1][0])
                        except:
                            pass
                if k == 3 and main_data[i+1][j][0]:
                    for l in range(main_data[i+1][j][0], main_size):
                        try:
                            possibilities[i][j].remove(l)
                            print(i, j, "nie moze byc", l, "bo ma byc mniejsza od", main_data[i+1][j][0])
                        except:
                            pass
                if k == 4 and main_data[i][j-1][0]:
                    for l in range(main_data[i][j-1][0], main_size):
                        try:
                            possibilities[i][j].remove(l)
                            print(i, j, "nie moze byc", l, "bo ma byc mniejsza od", main_data[i][j-1][0])
                        except:
                            pass


def refresh_numbers():
# usuwanie possibilities dla wpisanych juz liczb
    for i in range(main_size):
        for j in range(main_size):
            num = main_data[i][j][0]
            if num:
                for k in range(main_size+1):
                    if k != num:
                        try:
                            possibilities[i][j].remove(k)
                        except:
                            pass


if __name__ == "__main__":
    fromfile = create_list("liczby.txt", "wiersze.txt", "kolumny.txt")
    main_data = fromfile[0]
    zerocount = fromfile[1]
    main_size = len(main_data)
    possibilities = list()
    for i in main_data:
        temp = list()
        for j in i:
            temp.append(list(range(1, main_size+1)))
        possibilities.append(temp)
    for i in range(30):
        solve1()
        solve2()
        zerocount = solve3(zerocount)
        solve4()
    refresh_numbers()
    print(possibilities)






