def encodage(phrase,decalage):
    liste=""
    for i in range(len(phrase)):
        liste+=str(chr(ord(phrase[i])+decalage))
    return liste 

def décodage(phrase,decalage):
    liste=""
    for i in range(len(phrase)):
        liste+=str(chr(ord(phrase[i])-decalage))
    return liste

def decodage_brut(phrase):
    liste=""
    fragment1=""
    decalage=0
    dico = open(r"C:\Users\gabri\OneDrive\Documents\NSI\mini projet\Français.txt")
    read = dico.read()
    while decalage <= 256:
        for i in range(len(phrase)):
            liste+=str(chr(ord(phrase[i])-decalage))
        decalage=decalage+1
        fragment1 = liste.split(" ")
        
        for mot in fragment1:
            if mot in read:
                print("La phrase décoder est :",liste,", la clé de chiffrement est :""",decalage-1)
                quit()
        liste="" 

#print(encodage("Madame, Monsieur, Cher(e)s élèves et étudiants, En complément de mon précédent mail (le lien ne fonctionne pas!) Veuillez trouver ci-joint la présentation du BAFA à Sainte-Marie BastideRappel: le stage de Base du BAFA est accessible à 16 ans. (nouvelle disposition règlementaire).En vous souhaitant bonne réception,", 8))

#print(decodage_brut("""Uilium4(Uwv{qm}z4(Kpmz0m1{(ñtð~m{(m|(ñ|}lqiv|{4(Mv(kwuxtñumv|(lm(uwv(xzñkñlmv|(uiqt(0tm(tqmv(vm(nwvk|qwvvm(xi{)1(^m}qttm(|zw}~mz(kq5rwqv|(ti(xzñ{mv|i|qwv(l}(JINI(è([iqv|m5Uizqm(Ji{|qlmZixxmtB(tm({|iom(lm(Ji{
#m(l}(JINI(m{|(ikkm{{qjtm(è(9>(iv{6(0vw}~mttm(lq{xw{q|qwv(zðotmumv|iqzm16Mv(~w}{({w}piq|iv|(jwvvm(zñkmx|qwv4"""))       

    
    

















    


