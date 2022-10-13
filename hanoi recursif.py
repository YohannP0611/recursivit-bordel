# Créé par 33645, le 11/10/2022 en Python 3.7
hauteur_max = 7


def deplace(depart, arrive):
    jeu[arrive].insert(0 , jeu[depart][0])
    print('deplacement du disque ')
    del jeu[depart][0]
    afficher_hanoi(jeu['A'], jeu['B'], jeu ['C'])

def afficher_hanoi(zone_a,zone_b,zone_c):
    a = [0] * (hauteur_max - len(zone_a)) + zone_a
    b = [0] * (hauteur_max - len(zone_b)) + zone_b
    c = [0] * (hauteur_max - len(zone_c)) + zone_c

    for i in range(hauteur_max):
        print(' ' * (10 - a[i]), '_' *  (2 * a[i]), ' ' * (10 - a[i]), end= '|'  )
        print(' ' * (10 - b[i]), '_' *(2* b[i]), ' ' * (10 - b[i]), end= '|'  )
        print(' ' * (10 - c[i]), '_' *(2* c[i]), ' ' * (10 - c[i]))

    print(' '*7, "Zone A", ' '*7, end='|')
    print(' '*7, "Zone B", ' '*7, end='|')
    print(' '*7, "Zone C", ' '*7)

def hanoi(nombre_disque,a,b,c):
    if nombre_disque > 0  :
        hanoi(nombre_disque -1 , a , c , b)

        deplace(a,c)
        hanoi(nombre_disque-1 , b , a , c)

jeu = {"A" :[i for i in range(1,hauteur_max + 1)], "B":[], "C":[]}



afficher_hanoi(jeu["A"], jeu ["B"], jeu["C"])
hanoi(hauteur_max, "A", "B", "C")