# Projet 6 — Ordonnancement avec minimisation d'énergie : YDS et Lean 4

Implémentation de l'algorithme **YDS** (Yao–Demers–Shenker, FOCS 1995) et preuve de sa
correction en **Lean 4**.

Le sujet complet est dans [`sujet6.pdf`](sujet6.pdf). Le plan de travail et les critères de
chaque étape sont dans [`plan.md`](plan.md).

## Le problème

Un processeur à vitesse réglable `s(t)` exécute des tâches préemptives (`r_i`, `d_i`, `w_i`).
La puissance vaut `s²`, donc l'énergie est `∫ s² dt`. Il faut respecter toutes les dates
limites en minimisant l'énergie.

## Contenu du dépôt

```
.
├── plan.md              plan de travail, étape par étape
├── sujet6.pdf           énoncé
├── docs/
│   └── spec.md          définitions communes, format JSON, critère d'optimalité
├── python/
│   ├── yds.py           algorithme YDS
│   ├── json_io.py       entrée / sortie JSON (contrat avec Lean)
│   ├── tests/           tests unitaires
│   └── experiments/     script d'expériences
├── lean/                projet Lake (Lean 4 + Mathlib)
│   ├── lakefile.lean
│   ├── lean-toolchain
│   └── Masterielle/
│       ├── Basic.lean      tâches, ordonnancements, énergie, faisabilité
│       ├── YDS.lean        l'algorithme, en fonction calculable
│       ├── LowerBound.lean borne inférieure (Cauchy–Schwarz)
│       └── Checker.lean    vérificateur certifiant
├── data/
│   ├── instances/       instances générées (JSON)
│   └── solutions/       solutions proposées par Python (JSON)
└── rapport/             rapport final
```

## Utilisation

### Python

```bash
cd python
python3 -m pytest tests/ -v        # tests
python3 experiments/run_bench.py   # expériences
```

### Lean

```bash
cd lean
lake build
```

## État d'avancement

- [ ] E0 — socle du dépôt
- [ ] E1 — spec commune
- [ ] E2 — YDS en Python
- [ ] E3 — modèle Lean
- [ ] E4 — borne inférieure
- [ ] E5 — correction de YDS (terminaison + faisabilité)
- [ ] E6 — optimalité
- [ ] E7 — vérificateur + pont JSON
- [ ] E8 — rapport et soutenance

## Références

1. F. Yao, A. Demers, S. Shenker, *A Scheduling Model for Reduced CPU Energy*, FOCS 1995.
2. L. de Moura, S. Ullrich, *The Lean 4 Theorem Prover and Programming Language*, CADE 2021.
3. M. Eilers, P. Müller, *Nagini: A Static Verifier for Python*, CAV 2018.
