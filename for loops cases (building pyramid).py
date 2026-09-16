#for loops cases (building pyramid)

SHOW_PROGRESS = True   # ubah ke False pas submit ke judge

n_kasus = int(input('Enter the number of test cases: '))
block = int(input('Enter the number of blocks: '))

for i in range(n_kasus):
    sisa = block
    height = 0
    for day in range(1, block + 1):      # day 1, 2, 3, ... jalan sendiri
        if sisa < day:
            if SHOW_PROGRESS:
                print(f'  day {day}: blok nggak cukup, berhenti')
            break
        sisa -= day
        height = day
        if SHOW_PROGRESS:
            print(f'  day {day}: pakai {day} blok, sisa {sisa}')
    print('The height of the pyramid:', height)