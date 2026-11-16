import Masterielle.Basic

/-!
# L'algorithme YDS

À compléter aux étapes **E3** (fonction calculable) et **E5** (correction).

Étapes de l'algorithme :

1. points remarquables = dates `release` et `deadline`, triées ;
2. charge d'un intervalle `[a, b]` = travail des tâches entièrement contenues dans `[a, b]` ;
   densité = charge / (b - a) ;
3. choisir l'intervalle `I*` de densité maximale ;
4. sur `I*` : vitesse constante = densité(`I*`), tâches ordonnées par date limite croissante ;
5. retirer ces tâches et recommencer sur le temps restant.

Le résultat devra être un `Schedule` (voir `Basic.lean`) **calculable**, pas une simple
relation, pour pouvoir être évalué avec `#eval` et comparé au Python.

Théorèmes à énoncer puis prouver :

* `yds_terminates` — la récursion s'arrête ;
* `yds_feasible`   — l'ordonnancement produit respecte toutes les dates limites ;
* `yds_optimal`    — son énergie est minimale parmi les ordonnancements faisables.
-/
