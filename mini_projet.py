def encodage(phrase,decalage):
    liste="" #variable qui sera utilisé pour stocker les caractères encodés
    for i in range(len(phrase)): #démarre une boucle qui parcours chaque caractère de la phrase d'entrée
        liste+=str(chr(ord(phrase[i])+decalage)) #utilise la fonction ord pour obtenir le code ASCII du caractère, soustrait le décalage spécifié,onction chr pour obtenir le caractère correspondant et l'ajoute 
        #à la variable liste
    return liste 

def encodage2(phrase,decalage):
    liste="" #variable qui sera utilisé pour stocker les caractères encodés
    for i in range(len(phrase)): #démarre une boucle qui parcours chaque caractère de la phrase d'entrée
        if ord(phrase[i])==32: #vérifie si le code ASCII du caractère en cours est égal à 32 (correspondant à l'espace), si c'est le cas, l'espace est ajouté à la variable liste sans modification.
            liste+=phrase[i] 
        else:
            liste+=str(chr(ord(phrase[i])+decalage)) #utilise la fonction ord pour obtenir le code ASCII du caractère en cours, soustrait le décalage spécifié, utilise la fonction chr pour obtenir le caractère 
            #correspondant et l'ajoute à la variable liste
    return liste 

def fragment(fragment,phrase):
    if fragment in phrase: #vérifie si le fragment se trouve dans la phrase en utilisant l'opérateur in
        print("Oui le fragment est dans la phrase")#imprime "Oui le fragment est dans la phrase" si le fragment est dans la phrase.
    else:
        print("Non le fragment n'est pas dans la phrase")#imprime "Non le fragment n'est pas dans la phrase" si le fragment n'est pas dans la phrase.

def décodage(phrase,decalage):
    liste="" #variable qui sera utilisé pour stocker les caractères décodés
    for i in range(len(phrase)): ##démarre une boucle qui parcours chaque caractère de la phrase d'entrée
        liste+=str(chr(ord(phrase[i])-decalage)) #utilise la fonction ord pour obtenir le code ASCII du caractère en cours, ajoute le décalage spécifié, utilise la fonction chr pour obtenir le caractère correspondant
        #et l'ajoute à la variable liste en tant que chaine de caractere
    return liste

def decodage_brut(phrase):
    liste="" #initialise une variable chaîne vide appelée 'liste' qui sera utilisée pour stocker la phrase décodée.
    fragment1="" # initialise une variable chaîne vide appelée 'fragment1' qui sera utilisée pour stocker des parties de la phrase décodée.
    decalage=0 #initialise une variable appelée 'decalage' à 0. Cette variable sera utilisée pour contrôler le nombre de décalages appliqués à chaque caractère de la phrase encodée.
    dico = open(r"C:\Users\gabri\OneDrive\Documents\NSI\mini projet\Français.txt") #ouvre un fichier texte situé au chemin spécifié et affecte son contenu à la variable 'dico'. Ce fichier texte sera utilisé 
    #comme un dictionnaire pour vérifier si la phrase décodée contient des mots valides.
    read = dico.read() # lit le contenu du fichier 'dico' et l'affecte à la variable 'read'.
    while decalage <= 256: #démarre une boucle while qui va itérer 256 fois. La boucle continuera jusqu'à ce que la variable 'decalage' soit supérieure à 256.
        for i in range(len(phrase)): #démarre une boucle for qui va itérer sur chaque caractère de la variable 'phrase'.
            liste+=str(chr(ord(phrase[i])-decalage)) #prend la valeur ASCII du caractère courant dans la variable 'phrase', soustrait la valeur courante de 'decalage', convertit le résultat en un caractère, 
            #et l'ajoute à la variable 'liste'. Cette ligne applique le décryptage du chiffre Caesar.
        decalage=decalage+1 # incrémente la variable 'decalage' de 1.
        fragment1 = liste.split(" ") #divise la variable 'liste' en une liste de mots en utilisant le caractère espace comme délimiteur, et affecte le résultat à la variable 'fragment1'.
        
        for mot in fragment1: #démarre une boucle for qui va itérer à travers chaque mot de la liste 'fragment1'.
            if mot in read: #vérifie si le mot courant dans la liste 'fragment1' est présent dans la variable 'read' (i.e., le contenu du fichier dictionnaire).
                print("La phrase décoder est :",liste,", la clé de chiffrement est :""",decalage-1) # imprime la phrase décodée et la clé utilisée pour la déchiffrer si un mot valide est trouvé dans la phrase décodée.
                quit() #arrête l'exécution du script lorsqu'un mot valide est trouvé.
        liste="" # réinitialise la variable 'liste' à une chaîne vide afin qu'elle puisse être réutilisée à la prochaine itération de la boucle while.

  

    
    

















    


