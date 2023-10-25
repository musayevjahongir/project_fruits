def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    a=[]
    s=0
    from csv import reader
    f=open(data)
    f=reader(f)
    for i in f:
        a.append(i)
    for i in a[1:]:
        s+=float(i[1])
    return s
print(get_total_price("fruits.csv"))

    