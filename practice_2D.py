# Declaring a 2D array 
rows = 10
col = 10
myarray = [['~']* col for i in range(rows)]
# print(myarray)

# for i in range(rows):
#     for j in range(col):
#          print(myarray)

# loop through the array to print each value
# for x in myarray:
#     for y in x:
#         print(y)

# loop through the array using indexes!(Coordinates)
for x in range(len(myarray)):
    for y in range(len(myarray[x])):
        print(x,y, myarray[x][y])

        # this must be used for battle ship! (x,y) check if value of the coordinate is a ship



