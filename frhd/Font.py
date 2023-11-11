def shift(char, x, y):
    for line in char:
        for (point,ind) in line:
            if ind % 2 == 0:
                point += x
            else:
                point += y
            

def DrawLetter(x, y, letter):
    match letter:
        case "A":
            A = [[0, 0, 0, -20, 10, -20, 10, 0], [10, -10, 0, -10]]
            return shift(A, x, y)
        case "B":
            B = [[0, 0, 0, -20, 10, -20, 10, -10, 0, -10, 10, -10, 10, 0, 0, 0]]
            return shift(B, x, y)