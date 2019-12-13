#import json
import time
import os
import sys
from random import randint
alku=True
raha = randint(20, 100)
#raha=40000
ase="nyrkit"
panssari=""
maxhp = randint(10, 30)
xp=0
taso=1
hp=maxhp
vahinko=3
suoja=1


#nimi,vahinko,hinta
asenimi = ["tikari","piikkinuija","lyhytmiekka","pitkämiekka","sotakirves","kahdenkädenmiekka","tulimiekka"]
asevahinko = [10,13,20,29,36,40,50]
asehinta = [10,28,40,70,99,140,350]

#nimi,suoja,hinta
suojanimi = ["nahkapanssari","ketjuhaarniska","rengashaarniska","rintapanssari","peltihaarniska"]
suojaluku = [10,15,20,25,35]
suojahinta = [30,65,190,300,499]
olli=""
peikko =["metsänpeikko","metsästäjäpeikko","soturipeikko","tappajapeikko","peikkokuningas"]
kokemus =[10,30,60,100,700]
peikkovahinko=[1,1.15,1.3,1.6,1.8]

def kartta():
    os.system('cls')
    omax = 0
    omay = 9

    kartta = [
    [1,1,1,1,1,1,1,1,1,1,0,1,1],
    [1,1,1,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,1,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,1,1,0,0,0,0,1],
    [2,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
         
]

    merkit = " ♠@"
    while True:
        for rivi in kartta:
            for ruutu in rivi:
                print(merkit[ruutu], end = "")
            print()
        hahmo()
        if omay == 0 and omax == 10:
            print("Pääsit peikkokuninkaan luokse, valmistaudu taisteluun.")
            olli=4
            taistelu(olli,peikkohp,rahalootti)
            
            
            #Tähän tulee tosikova kamppailu koodi :)
        if omay == 9 and omax == 0:
            valinta=input("Olet kylän laidalla, haluatko palata kylään? k -painikkeella pääset kylään ")
            if valinta=="k":
                kyla()
    
        nappi=input("Suunta (wasd): ")
        uusix = omax
        uusiy = omay

        if nappi == "w":
            uusiy = omay - 1
            os.system('cls')
        if nappi == "s":
            uusiy = omay + 1
            os.system('cls')
        if nappi == "a":
            uusix = omax - 1
            os.system('cls')
        if nappi == "d":
            uusix = omax + 1
            os.system('cls')
        if kartta[uusiy][uusix] == 0:
            kartta[omay][omax] = 0
            kartta[uusiy][uusix] = 2
            omay = uusiy
            omax = uusix
        #print("OMAY: " +str(omay) + "  OMAX: " + str(omax))
    #kohtaamisia
        
        kohtaaminen = randint(0, 10)
      #  kohtaaminen =10
        
        ###########
        #öllit alueittain
        if omay == 9 or omay==8 and omax==3 or omay==8 and omax==4 or omay==8 and omax==5 or omay==7 and omax==2 or omay==7 and omax==3 or omay==7 and omax==4 or omay==6 and omax==2 or omay==6 and omax==3 or omay==6 and omax==4:
            olli = randint(0,1)
        else:
            olli = randint(1,3)
        
        ###########
        if kohtaaminen < 5:
         #   olli = randint(0, 2)
            if xp < 100:
                olli=0
            print("Metsässä vastaasi tulee " + peikko[olli] + " ja nyt on taisteltava henkesi edestä!")
            print("")
            print("")
            peikkohp=[randint(3,20),randint(7,50),randint(25,100),randint(100,300),600]
            peikkoraha=[randint(1,20),randint(10,40),randint(20,50),randint(30,70),randint(100,400)]
            rahalootti = peikkoraha[olli]
            taistelu(olli,peikkohp,rahalootti)


def kuolema(olli):
    global nimi
    global taso
    global maxhp
    

    time.sleep (2)
    os.system('cls')
    print("")
    print("")
    print("")
    print("")
    print("")
    print(nimi + " oli kuolleessaan tasolla " + str(taso) +". " + peikko[olli] + " lopetti sankarin seikkailun. Maksimi energiat oli " + str(maxhp))
    print("")
    print("")
    lopetus=input("Paina mitä tahansa painiketta lopettaaksesi")
    sys.exit(0)


def taistelu(olli,peikkohp,rahalootti):
        
    taistelu=True
    global raha
    #global peikkohp
    global peikkovahinko
    global xp
    global kokemus
    global ase
    global panssari
    global hp
    puolustus=0
    for i in range(5):
        if suojanimi[i] == panssari:
            puolustus = suojaluku[i]
    taso2 = (taso/10)+1

    if olli == 0 or olli ==1:
        peikonsuoja = randint (0,1)
        peikonase = randint(0,2)
    if olli==2:
        peikonase = randint(1,4)
        peikonsuoja = randint (1,3)
    if olli==3:
        peikonase = randint(3,5)
        peikonsuoja = randint (2,4)
    if olli==4:
        peikonase = 6
        peikonsuoja = 4
    
    php=peikkohp[olli]
    
    peikkolyo = peikkovahinko[olli] + asevahinko[peikonase]
    peikkolyo2=0
    while taistelu==True:
        print(peikko[olli] + "  Aseena: " + asenimi[peikonase] + " suojana: " + suojanimi[peikonsuoja])
        print("Peikon elämäpisteet: " + str(php))
        print("")
        print("")
        hahmo()
        valinta=input("Taistele 't' tai karkuun 'k'  ")
        if valinta=="k":
            kake=randint(1,4)
            if kake < 2:
                print("Et pääse karkuun ja " + peikko[olli] + " lyö sinua aseellaan...")
                print("")
                print("")
                time.sleep(0.5)
                peikkolyo2 = peikkolyo - suoja
                if peikkolyo2 < 0:
                    peikkolyo2 = 0
                hp=hp-peikkolyo2
                if hp < 1:
                    print("Peikko löi sinua niin että sielusi karkaa ruumiistasi. Vaihdoit hiippakuntaa, tämä peli loppui tähän.")
                    kuolema(olli)
                else:
                    print("Sait osuman verenhimoisen peikon sivalluksesta. Pystyt jatkamaan taistelua")
                    hppyo=round(hp)
                    hp=hppyo

            else:
                return
        if valinta=="t":
            print("Lyöt aseellasi...")
            time.sleep(0.5)
            swing=randint(1,100)
            
            if swing < 30:
                print("")
                print("Lyöntisi on keskivertoa alempi")
            if swing > 30 and swing < 70:
                print("")
                print("Lyöntisi on keskivertoinen")
            if swing > 70 and swing < 99:
                print("")
                print("Lyöntisi hipoo täydellisyyttä")
            if swing == 100:
                print("")
                print("Täydellinen lyönti")
            time.sleep(1)
            swing=swing/100
            swing = swing +1
            swing = swing * vahinko
            pelaajalyo = (swing * taso2) - int(suojaluku[peikonsuoja])
            if pelaajalyo < 0:
                pelaajalyo=0
            php = php - pelaajalyo
            #print("SWING: " + str(swing) + " TASO2: " + str(taso2) + " SUOJALUKU: " + str(suojaluku[peikonsuoja]))
            if php < 0:
                time.sleep(1)
                xp = xp + kokemus[olli]
                raha = raha + rahalootti
                print(peikko[olli] +" lyhistyy maahan kuolleena. Sait rahaa " +str(rahalootti))
                if olli==4:
                    
                    print("Peikkojen aiheuttama vitsaus on päättynyt samassa.")
                    time.sleep(4)
                    os.system('cls')
                    print("")
                    print("")
                    print("Sinua juhlitaan monta päivää ja yötä sankarina joka pelasti kylän peikkojen kiroukselta.")
                    time.sleep(5)
                    poistuminen = input("")
                    sys.exit(0)
                taistelu=False
                return
            else:       
                time.sleep(1)
                phppyo=round(php)
                #print("PHPPYO: " + str(phppyo))
                php=phppyo
                if pelaajalyo==0:
                    print("lyöntisi ei tee vahinkoa")
                    print("")
                    time.sleep(0.5)
                if pelaajalyo > 0:
                    print("löit osuman vastustajaan, mutta peikon retale jatkaa vielä taistelua")
                    print("")
                    time.sleep(0.5)
                print("Peikko lyö sinua...")
                print("")
                time.sleep(0.5)
                peikkolyo2 = peikkolyo - suoja
                if peikkolyo2 < 0:
                    peikkolyo2=0
                hp=hp-peikkolyo2
                if hp < 1:
                    print("Peikko löi sinua niin että sielusi karkaa ruumiistasi. Vaihdoit hiippakuntaa, tämä peli loppui tähän.")
                    kuolema(olli)
                    
                else:
                    if peikkolyo2 == 0:
                        time.sleep(0.5)
                        print("Peikon lyönti ei lävistä panssariasi")
                    else:
                        time.sleep(0.5)
                        print("Sait osuman verenhimoisen peikon sivalluksesta. Pystyt jatkamaan taistelua")
                        print("")
                        
                   
         

def hahmo():
    global vahinko
    global suoja
    global hp
    global maxhp
    global taso
    global nimi
    
    for i in range (7):  
        if asenimi[i] == ase:
           vahinko= asevahinko[i]
    
    for i in range (5):
        if suojanimi[i] == panssari:
           suoja= suojaluku[i]
            
    #taso2 0-99
    #taso3 100-999
    #taso4 1000-4999
    #taso5 5000-
    if xp >100 and taso==1 or xp > 499 and taso==2 or xp >1200 and taso==3 or xp > 2000 and taso==4 or xp>3000 and taso==5 or xp>5000 and taso==6 or xp>7000 and taso==7 or xp>9000 and taso==8 or xp>11000 and taso==9:
        maxhp = maxhp + randint(3,10)
        hp=maxhp
        taso=taso+1
        if taso==10:
            print("")
            print("Olet päässyt tasolle 10. joka on tämän pelin maksimi taso.")
            print("")
        print("")
        print("")
        print("Taistelukokemuksen myötä huomaat kehittyneesi, Energiasi on nyt: " + str(maxhp))
        print("")
        print("")
    
    print("")
    print("|Nimi: " + nimi + " |" + "|Raha: " + str(raha) + "|" )
    print("|Panssari: " + panssari + "|" + " |Ase: " + ase + "|")
    print("|Suoja: " + str(suoja) + "|" + "|Vahinko: " + str(vahinko) + "|" + " |Energia: " + str(hp) + "|" + str(maxhp))
    print("")

def kyla():    
    os.system('cls')
    global alku
    print("▓" * 20)
    print("▓" + " " * 18 + "▓")
    print("▓" + " " * 3 + "⌂" + " " * 3 + "⌂" + " " * 4 + "⌂" + " " * 5 + "▓")
    print("▓" + " " * 5 + "⌂" + " " * 5 + "⌂" + " " * 6 + "▓")
    print("▓" + " " * 4 + "⌂" + " " * 7 + "⌂" + " " * 5 + "▓")
    print("▓" + " " * 18 + "▓")
    print("▓" * 10 + "│" + "▓" * 9)
    print(" " * 10 + "│")
    print(" " * 3 + "♠" + " " * 2 + "♠" + " " * 3 + "│" + "  ♠ ♠")
    print("─" * 10 + "┘" + "♠  ♠  ♠")
    print(" " * 2 + "♠" + " " * 3 + "♠" + " " * 1 + "♠  ♠   ♠")
    if alku==True:
        print("")
        print("")
        print("Olet saapunut peikkometsänkylään, kylää terrorisoi metsän peikkokansa.")
        print("Sinun tehtäväsi on päättää tämä vitsaus josta kyläiset ovat kärsineet jo kauan.")
        print("")
        print("")
        alku=False
    #Ladataan "hahmopalkki ruutuun" :)
    hahmo()
    
    #arvotaan tuopille hinta kylään tullessa
    tuoppihinta=randint(1, 3)
    
    valinta=0
    while valinta < 1:
        print("Olet Peikkometsän kylässä, mitä teet?")
        print("1. Hilpasen tavernaan, tuopinhinta on tänään " + str(tuoppihinta) + " rahaa")
        print("2. Asekauppaan")
        print("3. Panssarimarkketti")
        print("4. Peikkometsään")
        try:
            valinta = int(input("Mitä teet? "))
            if valinta == 1:
                global hp
                global raha
                global maxhp
                valinta= 0
                print("Menit tavernaan lepäämään energiat täyteen")
                kerta=0
                ##### Tavernan hp-/tuoppilaskuri
                #print("hp:" + str(hp) + "  max:" + str(maxhp))
                print("Juot huurteisen, uuh. Tekipä hyvää")
                while hp < maxhp:
                    tuoppihp=randint(5, 12)
                    hp = hp + tuoppihp
                    if tuoppihinta < raha:
                        raha=raha-tuoppihinta
                        time.sleep(1.0)
                        kerta = kerta + 1
                    else:
                        print("Sinulla ei ole rahaa tankata energioita täyteen. Rahaa jäljellä " + str(raha))
                        break
                    if hp > maxhp:
                        hp=maxhp
                        gg=kerta * tuoppihinta
                        print("Energiat on täydet, joit " + str(kerta) + " kertaa ja rahaa meni " + str(gg))
                        print("")
                        print("")
                    else:
                        print(hp)
                #####
                time.sleep(3.0)
                
            if valinta == 2:
                print("Menit asemestarin luokse")
                time.sleep(1)
                print("'Mitä laitellaan' seppä tuumaa, ja hieraisee käsiään mustasta noesta")
                time.sleep(0.5)
                print("")
                print ("Sinulla on rahaa: " + str(raha))
                print("")
                global asenimi
                global asehinta
                global ase
                ostovalinta=0
                pituus = len(asenimi)
                for i in range (pituus):
                    print (str(i+1) + ". " + asenimi[i]  + "  hinta: " + str(asehinta[i]))     
                        
                print("8. poistu kaupasta")
                while ostovalinta < 1:
                    try:
                        ostovalinta=int(input("Valitse "))
                        if ostovalinta ==1:
                            if asehinta[ostovalinta - 1] <= raha:
                                print ("Ostit aseen " + asenimi[ostovalinta -1])
                                ase = asenimi[ostovalinta - 1]
                                raha = raha - asehinta[ostovalinta - 1]
                                ostovalinta=0
                            else:
                                ostovalinta=0
                                print("Rahat eivät riitä valitsemaasi tuotteeseen.")
                        if ostovalinta ==2:
                            if asehinta[ostovalinta - 1] <= raha:
                                print ("Ostit aseen " + asenimi[ostovalinta -1])
                                ase = asenimi[ostovalinta - 1]
                                raha = raha - asehinta[ostovalinta - 1]
                                ostovalinta=0
                            else:
                                ostovalinta=0
                                print("Rahat eivät riitä valitsemaasi tuotteeseen.")
                        if ostovalinta ==3:
                            if asehinta[ostovalinta - 1] <= raha:
                                print ("Ostit aseen " + asenimi[ostovalinta -1])
                                ase = asenimi[ostovalinta - 1]
                                raha = raha - asehinta[ostovalinta - 1]
                                ostovalinta=0
                            else:
                                ostovalinta=0
                                print("Rahat eivät riitä valitsemaasi tuotteeseen.")
                        if ostovalinta ==4:
                            if asehinta[ostovalinta - 1] <= raha:
                                print ("Ostit aseen " + asenimi[ostovalinta -1])
                                ase = asenimi[ostovalinta - 1]
                                raha = raha - asehinta[ostovalinta - 1]
                                ostovalinta=0
                            else:
                                ostovalinta=0
                                print("Rahat eivät riitä valitsemaasi tuotteeseen.")
                        if ostovalinta ==5:
                            if asehinta[ostovalinta - 1] <= raha:
                                print ("Ostit aseen " + asenimi[ostovalinta -1])
                                ase = asenimi[ostovalinta - 1]
                                raha = raha - asehinta[ostovalinta - 1]
                                ostovalinta=0
                            else:
                                ostovalinta=0
                                print("Rahat eivät riitä valitsemaasi tuotteeseen.")
                        if ostovalinta ==6:
                            if asehinta[ostovalinta - 1] <= raha:
                                print ("Ostit aseen " + asenimi[ostovalinta -1])
                                ase = asenimi[ostovalinta - 1]
                                raha = raha - asehinta[ostovalinta - 1]
                                ostovalinta=0
                            else:
                                ostovalinta=0
                                print("Rahat eivät riitä valitsemaasi tuotteeseen.")
                        if ostovalinta ==7:
                            if asehinta[ostovalinta - 1] <= raha:
                                print ("Ostit aseen " + asenimi[ostovalinta -1])
                                ase = asenimi[ostovalinta - 1]
                                raha = raha - asehinta[ostovalinta - 1]
                                ostovalinta=0
                            else:
                                ostovalinta=0
                                print("Rahat eivät riitä valitsemaasi tuotteeseen.")
                        if ostovalinta ==8:
                            kyla()
                        if ostovalinta < 1 and ostovalinta > 8:
                            print("Valintasi on virheellinen")
                            ostovalinta = 0
                    except ValueError:
                        print("Valintasi on virheellinen")
                        ostovalinta=0
                        
            if valinta == 3:
                ## laitetaan panssarikaupaan rojut ja männyn koristeet
                print("Menit panssarisepän luokse")
                time.sleep(1.0)
                print("'Kappas' haarniskamestari tokaisee ja on valmiina kaupantekoon.")
                time.sleep(0.5)
                print("")
                print ("Sinulla on rahaa: " + str(raha))
                print("")
                global suojanimi
                global suojahinta
                global panssari
                ostovalinta=0
                pituus = len(suojanimi)
                for i in range (pituus):
                    print (str(i+1) + ". " + suojanimi[i]  + "  hinta: " + str(suojahinta[i]))
                    
                print(str(i+2) + ". poistu kaupasta")
                while ostovalinta < 1:
                    try:
                        ostovalinta=int(input("Valitse "))
                        if ostovalinta > 0 and ostovalinta < 6:
                            if suojahinta[ostovalinta - 1] <= raha:
                                print ("Ostit suojan " + suojanimi[ostovalinta -1])
                                panssari = suojanimi[ostovalinta - 1]
                                raha = raha - suojahinta[ostovalinta - 1]
                                ostovalinta=0
                            else:
                                ostovalinta=0
                                print("Rahat eivät riitä valitsemaasi tuotteeseen.")
                        if ostovalinta ==(i+2):
                            kyla()
                        if ostovalinta < 1 or ostovalinta > pituus +1:
                            ostovalinta = 0
                    except ValueError:
                        print("Valintasi on virheellinen")
                        ostovalinta=0
                ## panssarimarketin loppu
            if valinta == 4:
                print("Onnea matkaan")
                time.sleep(1)
                kartta()

                
            if valinta < 1 or valinta > 4:
                valinta=0
                kyla()
        except ValueError:
            kyla()
nimi=input("Anna sankarille nimi: ")

kyla()







