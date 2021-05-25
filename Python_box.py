#displaying a box. Input the size of box
#variables
length = int()
width = int()
stars = str()

#ask user for length and width
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))   

stars = "*" + ((width - 2) * " ") + "*"

#loop to draw the box
for counter in range (0, length):
    if counter == 0 or counter == (length - 1):
        print("*" * width)
    else:
        print(stars)


