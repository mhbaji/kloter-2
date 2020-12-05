def cariKata(kata):
    Kalimat = [
        "Pagi itu sangatlah cerah, mentari pagi muncul memancarkan sinar cerah dengan semangat 67 eh semangat 45 maksudnya",
        "Sama denganku, hari ini adalah hari ulang tahun orang yang sangat aku kagumi bahkan kucintai",
        "Semua sudah aku persiapkan termasuk kue ultah serta kadonya",
        "Aku masuk ke kelas dengan hati gembira dan bibir tersenyum-senyum sendiri",
        "Kakiku melangkah tepat di depan pintu masuk kelas dan disambut ceria oleh sahabat sahabatku Syarif dan Renata.",
        "Yaps! Aku hampir lupa, aku Sherly kepanjangan dari Sherlyna rantika putri",
        "Cewek manis berkumis tipis yang kini sedang dilanda asmara cinta."]

    parsingKalimat = ["","","","","","",""]
    for i in range (len(Kalimat)):
        kalimatTemp = Kalimat[i].replace(",","")
        parsingKalimat[i] = kalimatTemp.split(" ")

    hitung= [0,0,0,0,0,0,0]
    for i in range (len(parsingKalimat)):
        for j in range (len(parsingKalimat[i])):
            if parsingKalimat[i][j].lower() == "aku" :
                hitung[i] += 1
    result = 0
    for i in range (len(hitung)):
        if hitung[i] > 0:
            result +=1
            print("Result ", result, ": kalimat ",'"', kata,'"', "muncul ", hitung[i]," kali pada index ", i)

cariKata("Aku")