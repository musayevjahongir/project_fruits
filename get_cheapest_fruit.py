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
    b=-1
    n=0
    s=0
    for i in f:
        a.append(i)
    for i in a[1:]:
        n=float(i[1])
        if n>b:
            s=i
            b=n
    return s[0]
print(get_cheapest_fruit("fruits.csv"))