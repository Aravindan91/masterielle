import Masterielle.Basic

/-!
# Borne inférieure (étape **E4**)

C'est le cœur mathématique du projet.

Pour tout intervalle `I = [a, b]` et tout ordonnancement faisable :

    énergie dépensée sur I  ≥  charge(I)^2 / (b - a)

C'est une conséquence de Cauchy–Schwarz (ou de Jensen) sur une somme finie :
`(∑ s_t)^2 ≤ (b - a) * ∑ s_t^2`.

Conséquences :

* si l'énergie de YDS atteint cette borne sur une famille d'intervalles **disjoints**, alors
  YDS est optimal ;
* c'est aussi le critère que le vérificateur (`Checker.lean`) contrôle.

Candidats Mathlib : `Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul` ou une preuve directe avec
`Finset.sum_mul_sq_le_sq_mul_sq`.
-/
