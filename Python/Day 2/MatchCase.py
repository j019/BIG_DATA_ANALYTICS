## Match Case



fruit ="Avacado"

match fruit:
    case "banana"|"Apple":
        print("Regular fruits")
    case "Mango"|"Avacado":
        print("Special Fruits")
    case _:
        print("No fruits")
