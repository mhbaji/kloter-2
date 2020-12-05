def perjalananSales(awal, a, d, c):
    sTokoToA = 2
    sAToB = 5
    sBToC = 1.5
    sCToD = 2.5

    hargaBensin = 7000

    bensinTokoToA = sTokoToA/2.5
    hargaBensinTokoToA = bensinTokoToA*hargaBensin

    sAToD = sAToB + sBToC + sCToD
    bensinAToD = sAToD/2.5
    hargaBensinAToD = bensinAToD*hargaBensin

    sDToC = sCToD
    bensinDToC = sDToC/2.5
    hargaBensinDToC = bensinDToC*hargaBensin

    sCToToko = sBToC + sAToB + sTokoToA
    bensinCToToko = sCToToko/2.5
    hargaBensinCToToko = bensinCToToko*hargaBensin

    totalJarak = sTokoToA + sAToD + sDToC + sCToToko
    totalBensin = bensinTokoToA + bensinAToD + bensinDToC + bensinCToToko
    totalHarga = hargaBensinTokoToA + hargaBensinAToD + hargaBensinDToC + hargaBensinCToToko
    
    print(awal, " - ", a, " = ", sTokoToA, " KM | Rp ", hargaBensinTokoToA, " | ",bensinTokoToA, " Liter")
    print(a, " - ", d, " = ", sAToD, " KM | Rp ", hargaBensinAToD, " | ",bensinAToD, " Liter")
    print(d, " - ", c, " = ", sDToC, " KM | Rp ", hargaBensinDToC, " | ",bensinDToC, " Liter")
    print(c, " - ", awal, " = ", sCToToko, " KM | Rp ", hargaBensinCToToko, " | ",bensinCToToko, " Liter")
    print("Total Jarak = ", totalJarak, " KM")
    print("Total Harga = Rp ", totalHarga)
    print("Total Bensin = ", totalBensin, "Liter")

perjalananSales("Toko","Tempat A", "Tempat D", "Tempat C")