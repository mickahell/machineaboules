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

machine_tour = 0
machine_humain = 0

echo "Qui commence ? - Machine commence ? y/n"

while baton > 1
	if machine_tour == 1
		box_$baton = [blue, red, green]
		bill_$baton = random.box_1
		baton = baton - {3 || 2 || 1}
	if humain_tour == 1
		echo "Il reste $baton. Combien de baton veux tu retirer, 3, 2 ou 1 ?"

	if baton == 1
		if machine_tour == 1
			machine_victoire = 0
			echo "Machine loose !"
		if humain_tour == 1
			machine_victoire = 1
			echo "Machine win !"	
do

if machine_victoire == 0	
	you loose
		foreach tour[x]
			bill_$x--

if machine_victoire == 1
	you win
		foreach tour[x]
			bill_$x++
