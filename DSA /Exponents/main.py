def get_estimated_spread(audiences_followers):
    total = 0
    length = len(audiences_followers)
    
    if length == 0:
        return 0
        
    for i in audiences_followers:
        total += i

    average = total / length

    spread = average * (length ** 1.2)

    return spread
