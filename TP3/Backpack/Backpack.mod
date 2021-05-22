/*********************************************
 * OPL 12.8.0.0 Model
 * Author: Belkacem
 * Creation Date: 22 mai 2021 at 17:21:05
 *********************************************/
int nbObjet = ...; 
int poidsMax = ...; 
range objets = 1..nbObjet; 


int poids[objets] = ...;
int utilites[objets] = ...;

dvar boolean x[objets]; // D�clarer les variables de d�cisions

// function objectif

maximize sum(i in objets) utilites[i] * x[i];
// contraintes
subject to
{
sum( i in objets ) poids[i] * x[i] <= poidsMax;
} 