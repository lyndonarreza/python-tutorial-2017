mindanao = ('malagos', 'matina', 'puan',"sasa",);

def tuples(mindanao):
    cebu = ('mandawe', 'ilo-ilo', 'caraga',);
    my_list = ();
    cebu_len = len(cebu)
    min_len = len(mindanao)
    # this will check if cebu and mindanao length is not equal
    # if not equal it will print cebu_len
    if min_len != cebu_len:

        print cebu_len
    else:
        print "they are equal"

tuples(mindanao);

def tuple_sort(mindanao):
    obrero = ('puan', 'darong', 'um-Bolton',);
    obrero_len = len(obrero)
    min_len = len(mindanao)
    # this will sort the obrero tuple
    if obrero > min_len:
        print(sorted(obrero))

tuple_sort(mindanao);

def tuple_assign():
    # assigning multiples values at once
    area_list = ();
    old_city = ("tacurong");
    area_one, area_zip = ("tacurong", "midsayap", "midsayap", "gensan",), (8000, 900, 8270)
    assign = area_one, area_zip
    for area_list in assign:
        if old_city not in area_list:
            print area_list
    return old_city

tuple_assign();