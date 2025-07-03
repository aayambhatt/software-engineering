def remove_duplicates(spells):
    track_spells = set()
    unique_list = []
    for spell in spells:
        if spell not in track_spells:
            track_spells.add(spell)
            unique_list.append(spell)
    return unique_list
    
