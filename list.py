cities = ['davao', 'manila', 'cebu', 'digos', 'midsayap', 'pigawayan'];

def cities_append(cities):
            mycities = ['calinan', 'baguio'];
            # this will check cities if calinan and baguio are present in the list
            # if not it will add the mycities in the cities list
            if mycities not in cities:

                   cities.append(mycities)
                   print cities

cities_append(cities);

def cities_extend(cities):
        # yourcities has default value of empty []
        yourcities = []
        if yourcities not in cities:
            yourcities = cities.extend(['cotabato','catalunan'])
            print "this will add cotabato and catalunan in thse citiest list using extend", cities
        return

cities_extend(cities);

def cities_insert(cities):
    # if cities len is greater than 5 it will add tamayong at index two
        insert_city = len(cities)
        if insert_city > 5:
            insert_city = cities.insert(2, "tamayong")
            print "This will insert tamayong at index 2", cities
        else:
            print "cities less than 5"
        return insert_city

cities_insert(cities);

def cities_remove(cities):
    tamayong = "tamayong"
    # if tamayong is in the list this will remove tamayong
    if tamayong in cities:
        city = cities.remove(tamayong)
        print "this will remove tamayong in the list", cities
    else:
        print "No tamayong to delete"

cities_remove(cities)

def cities_pop(cities):
    big_city = [];
    for big_city in cities:
        if big_city == "davao":
            big_city = cities.pop(0)
    print "this will remove davao at 0 index ", cities

    return big_city

cities_pop(cities)

def cities_reverse(cities):
    city = 10
    city_length = len(cities)
    if city_length < city:
        city = cities.reverse();
        print "This will reverse the of order of the list", cities

    else:

        print "list order never change"
cities_reverse(cities)








