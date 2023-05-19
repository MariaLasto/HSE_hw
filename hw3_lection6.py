with open("grades.txt", "r", encoding='utf-8') as f:
    res = [x.split() for x in f.readlines()]
with open("second_grade6.txt", "w", encoding="utf-8") as f:
    for x in res:
        f.write(f"{x[0]} {x[2]}\n")










