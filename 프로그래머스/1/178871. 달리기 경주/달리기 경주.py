def solution(players, callings):
    player = {players[i] : i for i in range(len(players))}
    for calling in callings:
        idx = player[calling]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        player[players[idx]] = idx
        player[players[idx-1]] = idx-1
    return players