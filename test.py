def chessBoardPlace():
    place = []
    for i in 'abcdefgh':
        for j in range(1,9):
            place.append(f"{i}{j}")
    places_new = []
    for i in place:
        places_new.append(i[1]+i[0])

    return place + places_new
    
    

print(chessBoardPlace())


