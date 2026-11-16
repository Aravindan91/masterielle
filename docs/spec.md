# Spec commune (E1)

> **À remplir à l'étape E1.** Ce fichier est la seule référence commune entre le Python et le
> Lean : si les deux ne sont pas d'accord avec ce document, c'est le document qui a raison.

## 1. Définitions

| Objet | Définition |
|---|---|
| Tâche `i` | `(r_i, d_i, w_i)` avec `r_i ≤ d_i` et `w_i ≥ 0` |
| Instance | liste finie de tâches |
| Temps | **discret** : tous les `r_i`, `d_i` sont des entiers (ou des rationnels sur une grille fixe) — décision à valider ici |
| Vitesse | `s(t) ≥ 0`, une seule tâche à la fois |
| Préemption | autorisée : une tâche peut être coupée et reprise |
| Faisable | chaque tâche `i` reçoit `w_i` unités de travail, uniquement dans `[r_i, d_i]` |
| Énergie | `∫ s(t)² dt`, soit `travail × vitesse` par morceau à vitesse constante |

## 2. Format JSON

### Instance (`data/instances/*.json`)

```json
{
  "name": "exemple_01",
  "horizon": 10,
  "jobs": [
    {"id": 0, "release": 0, "deadline": 4, "work": 2},
    {"id": 1, "release": 2, "deadline": 6, "work": 3}
  ]
}
```

### Solution (`data/solutions/*.json`)

```json
{
  "instance": "exemple_01",
  "energy": 9,
  "segments": [
    {"start": 0, "end": 2, "speed": 1, "job": 0},
    {"start": 2, "end": 6, "speed": 1, "job": 1}
  ],
  "certificate": {
    "intervals": [
      {"start": 0, "end": 6,
       "load": 5, "density": 0.8333333333333334}
    ]
  }
}
```

- `segments` : liste de morceaux `[start, end)` à vitesse constante, avec la tâche exécutée
  (`job: null` si processeur au repos).
- `energy` : énergie totale annoncée, que le vérificateur Lean recalcule.
- `certificate.intervals` : famille d'intervalles **disjoints** servant de borne inférieure.

## 3. Critère d'optimalité vérifié par Lean

Pour une famille d'intervalles disjoints `I_1, …, I_k` :

```
énergie(ordonnancement)  ≥  Σ_j  charge(I_j)² / longueur(I_j)
```

Si l'ordonnancement proposé est faisable **et** que son énergie est égale à cette somme, alors
il est optimal. C'est ce que le vérificateur (`lean/Masterielle/Checker.lean`) doit contrôler, et
ce que la preuve de soundness doit établir.

## 4. Questions ouvertes à trancher

- [ ] Grille de temps : entiers ou rationnels ?
- [ ] Que fait-on d'un processeur au repos dans un segment (`job: null`) ?
- [ ] Le certificat doit-il être produit par Python ou reconstruit par Lean ?
