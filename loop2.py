#How tall is the tree : 5

    #
   ###
  #####
 #######
#########
    #

tree_height = input("Enter how tall you tree will be: ")
tree_height  = int(tree_height)
spaces = tree_height - 1
hashes = - 1

stump_spaces = tree_height - 1

while tree_height != 0:
    for _i in range(spaces):
        print(' ', end="")
    for _i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1
for _i in range(stump_spaces):
    print(' ', end="")
print("#")  