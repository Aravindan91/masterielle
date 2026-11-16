import Mathlib

/-!
# Modèle : tâches, ordonnancements, énergie

Squelette à compléter à l'étape **E3** (voir `plan.md`).

Décision de modélisation : le temps est **discret** (grille finie). On évite ainsi les
intégrales et la théorie de la mesure, et l'énergie devient une somme finie :

    énergie = ∑_t s(t)^2 * Δt        (et sur un segment à vitesse constante : travail * vitesse)
-/

/-- Une tâche : disponibilité `release`, date limite `deadline`, quantité de travail `work`. -/
structure Job where
  release : ℚ
  deadline : ℚ
  work : ℚ
  work_nonneg : 0 ≤ work
  release_le_deadline : release ≤ deadline

/-- Une instance est une liste finie de tâches. -/
abbrev Instance := List Job

/-! ## À définir (E3)

* `Schedule` — vitesse `s(t) ≥ 0` et tâche exécutée à chaque pas de temps ;
* `Feasible` — chaque tâche reçoit exactement `work` unités de travail, uniquement dans
  `[release, deadline]`, et une seule tâche tourne à la fois ;
* `energy`   — `∑ s(t)^2 * Δt` ;
* `Optimal`  — `∀ s, Feasible s → energy (yds inst) ≤ energy s`.

Ne pas écrire les théorèmes finaux avant que ce fichier compile.
-/
