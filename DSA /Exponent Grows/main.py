def get_follower_prediction(follower_count, influencer_type, num_months):
    total = 0
    
    if influencer_type == "fitness":
        total = follower_count * ( 4 ** num_months)
    elif influencer_type == "cosmetic":
        total = follower_count * ( 3 ** num_months)
    else:
        total = follower_count * ( 2 ** num_months)

    return total
    
