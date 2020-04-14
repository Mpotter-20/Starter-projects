#intro screen
print( """This Program solves for this equation
(a/b) + (x*2) = c""")
print("")

#inputs for equation
a = input("Enter a number for A >")
b = input("Enter a number for B > ")
c = input("Enter the sum of a the equation. > ")

#equation
x = ((int(c) - (int(a) / int(b))) / 2)
u = (int(a) / int(b) + (x) * 2)
xr = str(round(x , 3))


#Output
if int(u) == int(c):
    print( "") 
    print("x = " + str(xr))
    print("(" + str(a) + "/" + str(b) + ")" + " + " + "(" + str(xr) + " * 2" + ")" + " = " + str(c))
    
#Error checker
else:
    print("ERROR")
    print( "x = " + str(x) + "\n" "u = " + str(u))

#exit
input("press ANY KEY to EXIT")

