def craft_sword(metal_bar):
    swords = {
        "bronze": "bronze sword",
        "iron": "iron sword",
        "steel": "steel sword"
    }
    try:
        return swords[metal_bar]
    except KeyError:
        raise ValueError("invalid metal bar")
