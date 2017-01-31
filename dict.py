
dream = {'house':'big', 'programmer':'good', 'food':'abundant', 'life':'happy', 'frriends':'many'}

def dream_dict():
    print "first print dream", dream
    small = dream["house"] = "small"

    for item in dream:
        if small not in item:
            small = dream["house"] = "small"

        else:

            print "Your house is already big",

    print "You are in dictionary", dream

dream_dict();

def dream_delete_dict(dream):
    # this will delete the key house in the dream dictionary
    for k in dream.keys():

        if k == 'house':
            del dream[k]

    print "This will delete house key and the house value in the dream dictionary", dream

dream_delete_dict(dream)


def dream_dict_clear(dream):
    old_dream = {'old':'house', 'age':10, 'plane':'big'}

    old = len(old_dream)
    new = len(dream)
    if old < new:
        old_dream.clear()
        print "this will delete dream dictionary ", old_dream
        old_dream['food'] = 'sweet'
        print "this will add new value in the dictionary food and sweet", old_dream

dream_dict_clear(dream);

def dream_add_dict():
    day_one_sale = {'snacks': 20, 'potato': 10, 'icecream': 100, 'tinapay': 10, 'chiken cubes':10,}
    day_two_sale = {'snacks': 50, 'potato': 1, 'icecream': 0, 'chiken cubes': 34, 'macaroni':23,}
    for k in day_two_sale:
        if k in day_one_sale:
            # it will add the value of day_one-sale and day_two_sale
            day_one_sale[k]+= day_two_sale[k]
    print "This is day one", day_one_sale

dream_add_dict()
