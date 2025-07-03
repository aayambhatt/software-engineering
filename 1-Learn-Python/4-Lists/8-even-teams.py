def split_players_into_teams(players):
    """
    even_slice = players[0:len(players):2]
    odd_slice = players[1:len(players):2]
    return even_slice, odd_slice
    """

    even_list = []
    odd_list = []
    for i in range(0,len(players)):
        if i%2==0:
            even_list.append(players[i])
        else:
            odd_list.append(players[i])
    return even_list, odd_list    

team = [1,2,3,4,5,6,7,8,9,10]
print(split_players_into_teams(team))
