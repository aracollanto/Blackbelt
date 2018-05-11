# Ara E. Collanto
# Task 3

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
def find_even(aaa = []):
    for a in aaa:
        for key, value in a.items():
            b = value.split(",") #To get the values on the dictionary and split it by ","
            #print (b)
            c = len(b)
            #print (c)
            d = 0
            even_numbers = []
            while d < c: 
                e = int(b[d])  #To get the number of every value in the dictionary
                #print(e)
                if (e%2)== 0:
                    even_numbers.append(e)
                d = d+1

    print ("The even numbers are: " ,even_numbers)





find_even(numbers)
