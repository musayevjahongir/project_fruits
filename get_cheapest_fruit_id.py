def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    from csv import reader
    f=open(data)
    f=reader(f)
    a=[]
    b=1000000000
    s=0
    for i in f:
        a.append(i)
    for i in a[1:]:
        n=float(i[1])
        if n<b:
            b=n
        s+=1
    return s
print(get_cheapest_fruit_id("fruits.csv") )