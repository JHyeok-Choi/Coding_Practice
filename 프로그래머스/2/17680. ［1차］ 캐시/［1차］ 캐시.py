def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            answer += 1
            cache.remove(city)
            cache += [city]
        else:
            answer += 5
            cache += [city]
            if len(cache) > cacheSize:
                cache.pop(0)
    
    return answer