cnt = 0
def hanoi(disc, from_pos, to_pos, aux_pos):
    global cnt
    cnt += 1
    if disc == 1:
        print(from_pos, "->", to_pos)
        return
    hanoi(disc-1, from_pos, aux_pos, to_pos)

    print(from_pos, "->", to_pos)
    hanoi(disc-1, aux_pos, to_pos, from_pos)


hanoi(5, 1, 3, 2)
print(cnt)