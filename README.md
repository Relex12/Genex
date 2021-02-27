# Genex
Genex est un générateur de générateur et de parseur orienté selon une grammaire.

Le projet est actuellement en cours de développement...

* [Genex](#genex)
    * [Présentation](#présentation)
    * [Récursivité](#récursivité)
    * [Fonctionnement](#fonctionnement)
    * [Technique](#technique)

<!-- table of contents created by Adrian Bonnet, see https://github.com/Relex12/Markdown-Table-of-Contents for more -->

## Présentation

Genex est un outil qui permet de générer des instances ou d'analyses des instances qui suivent une grammaire au sens formel.

A partir d'une grammaire sous la forme d'un fichier `.gram`, Genex sera capable à la fois de générer des dérivations possibles de l'axiome de la grammaire et d'analyser des phrases pour savoir si elles correspondent à la grammaire donnée.

## Récursivité

Les grammaires acceptées par Genex sont définies selon la grammaire de Genex.

La grammaire de Genex n'est pas encore spécifiée mais le sera prochainement.

Il sera donc de donner à Genex sa propre grammaire, de sorte que Genex génère des grammaires conformes à sa propre grammaires, puis qu'il génère des dérivations possibles de ces grammaires.

## Fonctionnement

Genex va être composé en premier lieu d'un analyseur lexical (ou lexeur) qui traduit la grammaire du fichier d'entrée sous forme de liste de lexèmes ou unités lexicales.

Ensuite, un analyseur syntaxique (ou parseur) transforme la liste en dictionnaire, dont les clés sont des lexèmes et les valeurs sont des expressions régulières sur les lexèmes.

C'est ce dictionnaire qui sera parcouru pour générer des dérivations de l'axiome ou vérifier que des phrases correspondent bien à la grammaire.

## Technique

Genex est un projet réalisé en Python. Les graphes sont représentés sous la forme de dictionnaires.

Pour la réalisation des analyses lexicales et syntaxiques, les outils PLY ou SLY seront peut-être utilisés.
