
#input the parameter
born_year = int(input("The year you were born is: ")) 
eighteen_year = born_year + 18   


def find_favorite_bond_actor(eighteen_year):
    # define the time of the bond actors
    bond_actors = [
        ("Roger_Moore",1973,1986),
        ("Timothy_Dalton",1987,1994),
        ("Pierce_Brosnan",1995,2005),
        ("Daniel_Craig",2006,2021)
    ]

    # use function to find the favourite actor
    favorite_bond_actor = None 
    for actor, start_year, end_year in bond_actors:
        if eighteen_year >= start_year and eighteen_year <= end_year:
            favorite_bond_actor = actor
            break
    return favorite_bond_actor


print(f"The favorite Bond actor for someone born in {born_year} is {find_favorite_bond_actor(eighteen_year)}.")