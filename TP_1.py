"""voila notre programme de similation de travaille d'une memoire RAM"""



def stocker (variable , derniere_ligne , derniere_colonne) :
    """Fonction permetant la mise en stock d'une valeur quelconque en memoire"""
    for i in range( dernire_ligne , 5) :
        for j in range(derniere_colonne , 5) :
            memoire[i][j] = variable
            derniere_colonne = derniere_colonne+1
            if derniere_colonne == 4 :
                derniere_ligne = derniere_ligne+1
                derniere_colonne = 0
            break
        break
    if derniere_ligne > 4 :
        print("\nMemoire plaine\n")
        return 0
    return derniere_ligne , derniere_colonne

print("BIEVENU : 0S_16".center( 50 , "*"))
print("\nPROGRAMME EXECUTANT LA SIMULATION DU FONCTIONNEMENT DEE LA MEMOIRE RAM\n\n")
ligne = [] #inititation des lignes de la memoire
memoire = [] # creation de la memoire

# initiation de toute les ceases de la memoire a vide
for i in range(1,5) :
    ligne = []
    for j in range(1,5) :
        colonne="VD"
        ligne.append(colonne)
    memoire.append(ligne)


# Affichage de L'etat initiale de la memoire avec toutes les cases qui sont vide
print("Initialement avant toute execution, la memoire est vide , voici cet etat initial : \n")
print("Affichage a l'etat initial".center(50 ,"=" ))
for ligne in memoire :
    for variable in ligne :
        print(variable , end= " ")
    print("\n")

print("Apres , lorsqu'on lance l'execution d'un programme , quelques valeurs sont stocker dans la memoire\nEn voici la representation : \n")
# Remplissage de la memoire , ici on considere que le processeur envoie a la memoire des valeurs a stocker pour
# les processus qui sont en cours d'execution en son sein
# Ici l'allocation memoire est continue et non aleatoire
dernire_ligne = derniere_colonne = 0
dernire_ligne , derniere_colonne = stocker(4, dernire_ligne, derniere_colonne)
dernire_ligne , derniere_colonne = stocker(6, dernire_ligne, derniere_colonne)
dernire_ligne , derniere_colonne = stocker(7, dernire_ligne, derniere_colonne)
dernire_ligne , derniere_colonne = stocker(12, dernire_ligne, derniere_colonne)
dernire_ligne , derniere_colonne = stocker(24, dernire_ligne, derniere_colonne)


# Affichage de l'etat de la memoire apres stockage de certaines valeurs , et on montre toujours les case qui sont vides
print("Affichage apres stockage en memoire".center(50 ,"="))
for ligne in memoire :
    for variable in ligne :
        print(variable , end= " ")
    print("\n")