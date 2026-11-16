# Projet 6 — Ordonnancement et minimisation d'énergie (YDS + Lean 4)

> Plan de travail. On coche au fur et à mesure : **on ne passe pas à l'étape suivante
> tant que le critère « ✅ Fini quand » n'est pas vrai.**

---

## 1. Le but, en clair

On a un processeur et `n` tâches. Pour chaque tâche `i` :

- `r_i` : date de disponibilité (elle ne peut pas commencer avant) ;
- `d_i` : date limite (elle doit être finie avant) ;
- `w_i` : quantité de travail à fournir.

Le processeur tourne à une **vitesse réglable** `s(t) ≥ 0`, une seule tâche à la fois, et les
tâches peuvent être **interrompues et reprises** (préemption). La puissance consommée vaut `s²`,
donc l'énergie totale est `∫ s(t)² dt`.

À vitesse constante `s`, une tâche de travail `w` met `w/s` de temps et coûte `(w/s)·s² = w·s`.
**Donc énergie = travail × vitesse : aller plus vite coûte plus cher.**

> **La question du projet :** comment choisir la vitesse à chaque instant pour que toutes les
> tâches finissent avant leurs dates limites, en dépensant le **minimum** d'énergie ?

**La réponse (YDS) :** on repère la période où la charge de travail est la plus dense, on y
tourne à vitesse = cette densité, on y ordonne les tâches par date limite croissante, puis on
recommence sur ce qui reste. Cette stratégie est **optimale**.

---

## 2. Ce qu'il faut livrer

| # | Livrable | Où |
|---|---|---|
| 1 | Programme Python (YDS + tests + expériences) | `python/` |
| 2 | Projet Lean 4 compilable (`lake build` sans erreur) | `lean/` |
| 3 | Preuves : terminaison, respect des dates limites, **optimalité** | `lean/Masterielle/` |
| 4 | Vérificateur Lean qui certifie les résultats Python | `lean/Masterielle/Checker.lean` |
| 5 | Exemples vérifiés bout en bout | `data/` |
| 6 | Rapport expliquant les preuves obtenues | `rapport/` |

---

## 3. YDS en 5 étapes (l'algorithme à implémenter)

1. **Points remarquables** : toutes les dates `r_i` et `d_i`, triées.
2. **Charge d'un intervalle** `[a, b]` : somme des `w_i` des tâches **entièrement contenues**
   dans `[a, b]`. **Densité** = charge / (b − a).
3. **Intervalle le plus chargé** `I*` : celui de densité maximale.
4. **Sur `I*`** : vitesse constante = densité(`I*`) ; les tâches contenues dans `I*` sont
   ordonnées par **EDF** (date limite croissante).
5. **Retirer** ces tâches et cet intervalle, puis **recommencer** sur le temps restant.

**Propriété clé (celle qu'on veut prouver) :** l'énergie de YDS vaut
`Σ_k densité(I_k)² × longueur(I_k)` sur les intervalles critiques, et c'est exactement une
**borne inférieure** valable pour tout ordonnancement faisable ⇒ YDS est optimal.

---

## 4. Plan par étapes

### E0 — Socle du dépôt
- Créer l'arborescence, `README.md`, `.gitignore`.
- Installer Lean via `elan`, vérifier que `lake build` passe sur le squelette.
- Créer le dépôt GitHub et faire le premier `push`.

**✅ Fini quand :** le dépôt est en ligne, `lake build` répond sans erreur et `python -c "import yds"` passe.

---

### E1 — Spec commune (le contrat des 3)
- Remplir `docs/spec.md` : définitions (tâche, ordonnancement, faisabilité, énergie).
- **Décision : temps discret** (les dates tombent sur une grille de pas entiers/rationnels) —
  sinon on tombe dans la théorie de la mesure, hors de portée.
- Fixer le **format JSON** Python ↔ Lean (voir `docs/spec.md`).
- Fixer le **critère d'optimalité** vérifiable : une famille d'intervalles critiques disjoints.

**✅ Fini quand :** `docs/spec.md` est relu et validé par les 3, et il n'y a plus de question
ouverte sur les définitions.

---

### E2 — YDS en Python (peut se faire en parallèle de E3)
- Implémenter `density`, `critical_interval`, `yds` dans `python/yds.py`.
- Tests unitaires dans `python/tests/` : cas à la main + instances aléatoires + vérification
  que les dates limites sont respectées.
- **Référence** : un brute-force (énumération / LP) sur de très petites instances pour
  confirmer l'optimalité.

**✅ Fini quand :** tous les tests passent **et** sur 100 petites instances aléatoires, l'énergie
de YDS est égale au minimum trouvé par le brute-force.

---

### E3 — Modèle Lean
- `lean/Masterielle/Basic.lean` : `Job`, `Schedule`, `Feasible`, `Energy`, `Optimal`.
- Énoncer (avec `sorry`) les 3 théorèmes finaux : `terminates`, `feasible`, `optimal`.
- Écrire la fonction YDS **comme fonction calculable** (`def yds : Instance → Schedule`).

**✅ Fini quand :** `lake build` passe (les théorèmes peuvent être en `sorry`), et la fonction
`yds` s'évalue sur un exemple à la main (`#eval`).

---

### E4 — Borne inférieure (le cœur mathématique)
- Prouver : pour tout intervalle `I` et tout ordonnancement faisable,
  `énergie(I) ≥ charge(I)² / longueur(I)`.
- Outil : Cauchy–Schwarz / Jensen sur une somme finie (`Finset.sum_sq_le` côté Mathlib).

**✅ Fini quand :** ce lemme est prouvé **sans aucun `sorry`**. C'est le point de non-retour :
si ça bloque, on simplifie le modèle (temps entier, 3–4 tâches) tout de suite.

---

### E5 — Correction de YDS
- Terminaison (la récursion retire toujours au moins une tâche).
- Faisabilité (toutes les dates limites respectées).
- Les vitesses choisies respectent la charge de l'intervalle.

**✅ Fini quand :** `terminates` et `feasible` sont prouvés sans `sorry`.

---

### E6 — Optimalité
- Montrer que les intervalles critiques sont **disjoints** et que la somme des bornes
  inférieures égale l'énergie de YDS.
- Conclure `optimal`.

**✅ Fini quand :** `optimal` est prouvé (ou, au minimum, énoncé et découpé en lemmes avec un
`sorry` unique clairement identifié et assumé dans le rapport).

---

### E7 — Vérificateur + pont Python → Lean
- `Checker.lean` : le vérificateur prend `(instance, schedule, certificat)` et rend `Bool`.
- **Prouver sa soundness** : `check ... = true → optimal`.
- Côté Python : export JSON des instances et des solutions, import dans Lean, test bout en bout.

**✅ Fini quand :** au moins 20 instances générées par Python sont acceptées par le vérificateur
Lean, et le théorème de soundness est prouvé.

---

### E8 — Nettoyage, rapport, soutenance
- Supprimer ou documenter les `sorry` restants, écrire le README final.
- Rapport : but, modèle, algorithme, preuves obtenues, résultats expérimentaux, limites.
- Slides + répétition (chacun doit savoir expliquer **les 3 lots**).

**✅ Fini quand :** `lake build` sans `sorry` non documenté, rapport relu, démo rejouée de bout en bout.

---

## 5. Ordre et parallélisme

```
E0 → E1 ─┬─→ E2 (Python) ──────────────┐
         │                             ├─→ E7
         └─→ E3 → E4 → E5 → E6 ────────┘
                        → E8
```

- **E2 est indépendant** : il peut avancer seul dès E1.
- **E4 dépend de E3** (il faut les définitions) : ne pas commencer E4 avant que le modèle compile.
- **E6 dépend de E4 et E5.**
- **E7 dépend de E2 (le JSON) et de E1 (le critère).**

---

## 6. Pièges repérés d'avance

| Piège | Parade |
|---|---|
| Modèle Lean en temps continu → intégrales et théorie de la mesure | **Temps discret** décidé en E1 |
| « Max de densité » sur tous les intervalles = exponentiel | Ne considérer que les intervalles entre deux dates remarquables |
| Preuve d'optimalité complète trop ambitieuse | Découper (E4 → E5 → E6) + **vérificateur certifiant** (E7) comme filet de sécurité |
| Python et Lean modélisent deux problèmes différents | Le JSON et `docs/spec.md` sont la **seule** référence |
| `sorry` qui traîne | Compter les `sorry` à chaque point d'étape |

---

## 7. Conventions

- Un seul dépôt, une seule branche `main` (on travaille ensemble) ; `main` doit toujours builder.
- Message de commit : `E<n>: ce qui est fait` (ex. `E2: yds.py + tests deadline`).
- Le PDF du sujet est à la racine : `sujet6.pdf`.
