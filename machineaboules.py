#Faire le jeu des 3 batons, entre humain et machine
#Règle, chaque joueur retire à son tour 3, 2 ou 1 baton. Celui qui prend le dernier baton à perdu

##La machine doit apprendre : 
##	Si elle perd retirer chaque billes qu'elle à joué de chacune de ses listes
##	Si elle gagne ajouter une bille qu'elle a joué à chacunes de ses listes

##Creer un graphe de son avancement de ses victoires/défaites


baton = 11
blue = 3
red = 5
green = 7

machine_tour = True
humain_tour = False

print("Qui commence ? - Machine commence ? y/n")

while baton > 1:
        if machine_tour == True:
                print("Tour de la machine")
#               box_$baton = [blue, red, green]
#               bill_$baton = random.box_baton
                baton = baton - random.randrange(1, 4)
                print(baton)
        if humain_tour == True:
                print("Tour de l'humain")
#               print("Il reste " baton ". Combien de baton veux tu retirer, 3, 2 ou 1 ?")
                print(baton, "il reste")

        if baton <= 1:
                if machine_tour == True:
                        machine_victoire = 0
                        print("Machine loose !")
                if humain_tour == True:
                        machine_victoire = 1
                        print("Machine win !")
        else:
                machine_tour = not machine_tour
                humain_tour = not humain_tour


if machine_victoire == 0
	you loose
		foreach tour[x]
			bill_$x--

if machine_victoire == 1
	you win
		foreach tour[x]
			bill_$x++
