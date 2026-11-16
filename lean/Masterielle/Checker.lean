import Masterielle.Basic

/-!
# Vérificateur certifiant (étape **E7**)

Idée : on ne prouve pas le code Python. On écrit en Lean un vérificateur qui, à partir d'une
instance et d'une solution proposée par Python (au format JSON de `docs/spec.md`), contrôle :

1. la solution est **faisable** (toutes les dates limites respectées, tout le travail fourni) ;
2. l'énergie annoncée est bien celle des segments ;
3. cette énergie est égale à la borne inférieure calculée sur les intervalles du certificat.

Théorème de **soundness** à prouver :

    check inst sol = true  →  Optimal inst sol

Ainsi, tout résultat accepté est certifié optimal, sans faire confiance au code Python.
-/
