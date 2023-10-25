def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    a=[]
    b=[]
    from csv import reader
    f=open(data)
    f=reader(f)
    for i in f:
        a.append(i)
    for i in a:
        b.append(i[0])
    return b[1:]
print(get_frutis_name("fruits.csv"))

    