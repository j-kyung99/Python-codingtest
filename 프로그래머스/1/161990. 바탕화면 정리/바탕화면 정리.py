def solution(wallpaper):
    file = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                file.append((i, j))
    updown = [item[0] for item in file]
    leftright = [item[1] for item in file]
    return [min(updown), min(leftright), max(updown)+1, max(leftright)+1]