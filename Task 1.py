# Ara E. Collanto
# Task 1

#Using for loop
Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

x = 0
for key, value in Sessions_Attended.items():
    y = value.split(",")
    z = len(y)
    x = z + x

print("I have attended ",x, " sessions!" )

#Using Static assignments
#Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

#x = Sessions_Attended['sessions']
#x = x.split(",")

#print("I have attended ",len(x), " sessions!" )
