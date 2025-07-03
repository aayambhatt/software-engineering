def get_most_common_enemy(enemies_dict):
    max_count = float("-inf")   # nothing is smaller than -∞
    most_common_enemy = None    # we don’t know any enemy yet

    for enemy in enemies_dict:
        count = enemies_dict[enemy]

        if count>max_count:
            max_count = count
            most_common_enemy = enemy

    return most_common_enemy

    """
    def get_most_common_enemy(enemies_dict):
    max_count = float("-inf")
    most_common_enemy = None

    for enemy, count in enemies_dict.items():
        if count > max_count:
            max_count = count
            most_common_enemy = enemy

    return most_common_enemy

    
    """
