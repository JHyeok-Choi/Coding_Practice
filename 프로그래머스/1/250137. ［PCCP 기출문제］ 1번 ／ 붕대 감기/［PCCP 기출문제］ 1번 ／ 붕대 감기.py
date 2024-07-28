def solution(bandage, health, attacks):
    casting = 0
    maxhp = health
    time = attacks[0][0]
    
    for att, atk in attacks:
        health += ((att - time) // bandage[0]) * bandage[2] + (att - time) * bandage[1]
        time = att + 1
        
        if health > maxhp:
            health = maxhp
        
        health -= atk
        if health <= 0:
            return -1
            
    return health
