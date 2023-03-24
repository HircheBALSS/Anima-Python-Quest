def score(dice):
     # pass your code here

    points = {1:1000, 6:600, 5:500, 4:400, 3:300, 2:200}
    dices = {i:dice.count(i) for i in dice}
    tot = 0
    for k,v in dices.items():
        tot += (points[k] * (v // 3)) if v >= 3 else 0
        tot += 100 * (v % 3) if k == 1 else 0
        tot += 50 * (v % 3) if k == 5 else 0
    return tot