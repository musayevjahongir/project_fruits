def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    from csv import reader
    f=open(data)
    f=reader(f)
    a=[]
    b=[]
    for i in f:
        a.append(i[1])
    a=a[1:]
    for i in a:
        b.append(float (i))
    return max(b)
print(get_cheapest_fruit("fruits.csv"))