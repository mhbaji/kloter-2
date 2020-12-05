def gambarPola(nilai):
    for i in range (nilai):
        for j in range(nilai):
            if i == 0 or i == nilai-1 or j == 0 or j == nilai-1:
                print(" x ", end="")
            elif i == 2 or i == nilai-3 or j == 2 or j == nilai-3:
                if i == 1 or i == nilai-2 or j == 1 or j == nilai-2:
                    print("   ", end="")
                else:
                    print(" y ", end="")

            elif i == 4 or j == 4 or i == nilai-5 or j == nilai-5:
                if i == 4 and (j == 4 or j == nilai-5) or i == nilai-5 and (j == 4 or j == nilai-5):
                    print(" z ", end="")
                else :
                    print("   ", end="")
            else :
                print("   ", end="")
            
        print("")

gambarPola(10)