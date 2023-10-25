def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
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
            b=n
            s=i
    return s[0]
print(get_expensive_fruit("fruits.csv"))


