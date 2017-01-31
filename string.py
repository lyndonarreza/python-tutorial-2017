def String(age, firstname, lastname):
    name = firstname
    last = lastname
    age = age
    address = "Joaquin Calinan, Davao City"
    if age <= 30:
        # string formatting the %s stands for string
        # the %d stands for digits
        # the first %s stands for name and has the value of lyndon
        # the second %s stands for last and has the vlue of Arreza
        # the third %d as you can see its not %s! its because its a digit and %d format will use for the digit
        print("%s %s and age %d" % (name, last, age))


String(firstname="Lyndon", lastname="Arreza", age=21)


