def solution(wallpaper):
    x = []
    y = []
    
    for i_y,i in enumerate(wallpaper):
        for i_x,j in enumerate(i):
            if j=='#':
                x.append(i_x)
                y.append(i_y)
    
    return [min(y), min(x), max(y)+1, max(x)+1]