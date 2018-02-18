#import fileinput

#nb = 0
#for line in fileinput.input():
#   if int(line) > 0 and nb == 0:
#       x = int(line)
#
#   if int(line) > 0 and nb == 1:
#       y = int(line)
#       nb += 1
#    if nb == 2 and int(line) > 0:
#       if x > y:
#           print("Le plus grand est : " + str(x))
 #       else:
#          print("Le plus grand est : " + str(y))
#   if int(line) > 0:
#       nb += 1
#
#       # import fileinput
#       # for line in fileinput.input():
#       #    print(line)
#
        import fileinput

        x_or_y = 0  # 0 => x, 1 => y
        for line in fileinput.input():
            if x_or_y == 0:
                if int(line) >= 0:
                    x = int(line)
                    x_or_y = 1
                else:
                    print("Enter a number >= 0")
            else:
                if int(line) >= 0:
                    y = int(line)
                    if x > y:
                        print("x > y")
                    else:
                        print("y >= x")
                else:
                    print("Enter a number >= 0")




