# Versions de Genex et contenu

## Analyse lexicale

L'analyseur lexical produit une liste qui devra être interprétée par l'analyseur syntaxique. 

Chaque élément de cette liste est lui-même une liste des lexèmes d'une ligne du fichier d'entrée.

Le passage d'un élément à l'autre de la liste renvoyée par l'analyseur lexical représente donc un retour à la ligne. Le passage d'un élément à l'autre d'un élément de la liste renvoyée par l'analyseur lexical représente donc le passage d'un lexème à un autre dans une ligne.

L'analyseur lexical ne produira pas de lexème vide (`''`) ou de ligne vide, malgré les commentaires, les sauts de lignes et les espaces blancs. 

**V0.0** :

* les espaces blancs (séparateurs de lexème) peuvent être des espaces ou tabulations 
* les fins de ligne peuvent être des CR (`\r`), LF (`\n`) ou CRLF(`\r\n`)
* des espaces blancs DOIVENT se trouver AVANT et APRES les caractères suivants : 	>	|	(	)
* des espaces blancs DOIVENT se trouver AVANT et APRES l'écriture de terminaux (e.g.	 'a'	'A'	'1')



Pour cette version, les fichiers de grammaires d'entrée doivent suivre les règles suivantes :

``` gram
GRAM > DEF | DEF RET GRAM | DEF RWS RET GRAM

WS > ' ' | '\t'
RWS > WS OWS
RET > '\r' | '\n' | '\r' '\n'

IDENT > CAR | CAR IDENT
CAR > LETT | CHIFF | '_'
LETT > MAJ | MIN
MAJ > 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
MIN > 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
CHIFF > '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

DEF > IDENT RWS '>' RWS PLACE
PLACE > IDENT | TERM | IDENT RWS PLACE | PLACE RWS '|' RWS PLACE | '(' RWS PLACE RWS ')'
TERM > '''CAR'''

```

Ces règles respectent la grammaire qu'elles définissent, elles peuvent donc être utilisées pour générer des tests avec Genex.



**V0.1** :

* tous les caractères d'une ligne après	#	sont ignorés
* seuls les espaces blancs entre deux identificateurs sont requis

**V1.0** :

* `['a' - 'z']` intervalle
* `"chaine de terminaux"`
* `"\""` caractère échappé (seulement pour `"`)



**Choses à ajouter** : 

* accents
* UTF-8
* Epsilon
* codage héxa des caractères (pour bytes)







## Analyse sémantique

## Générateur et parseur



