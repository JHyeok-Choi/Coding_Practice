def solution(bandage, health, attacks):
    casting = 0
    maxhp = health
    
    for t in range(1, attacks[-1][0] + 1):
        if t == attacks[0][0]:
            health -= attacks.pop(0)[1]
            if health <= 0:
                return -1
            casting = 0
        elif health < maxhp:
            casting += 1
            if health < maxhp:
                health += bandage[1]
            if casting == bandage[0]:
                health += bandage[2]
                casting = 0
            if health > maxhp:
                health = maxhp
        
    return health