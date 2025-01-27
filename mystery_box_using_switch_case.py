#creating switch cases for choosing a box from the options
def choice():
    #give options to choose from
    box=(input("choose a box from 1.chocolate, 2.biscuit, 3.cool drinks, 4.chips, 5.ice cream, empty - mystery box :"))
    match box:
        #create multiple cases to match the numbers to be given
        case 1:
            print("chocolate-Galaxy(1x)")
        case 2:
            print("biscuit-Dark fantasy(1x)")
        case 3:
            print("cool drinks-Sprite(1x)")
        case 4:
            print("chips-Kurkure(1x)")
        case 5:
            print("ice cream-Magnum(1x)")
        case default:
            print("mystery box-Brownie((1x))")
choice()