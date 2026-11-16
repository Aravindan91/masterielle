"""Tests de l'algorithme YDS.

Lancer depuis ``python/`` :

    python3 -m pytest tests/ -v

À écrire à l'étape E2 :
  - cas jouets résolus à la main (énergie connue d'avance) ;
  - instances aléatoires : vérifier la faisabilité (``is_feasible``) ;
  - comparaison avec un brute-force sur de très petites instances (optimalité).
"""

from yds import Job, density, load


def test_load_intervalle_total() -> None:
    jobs = [
        Job(id=0, release=0, deadline=4, work=2),
        Job(id=1, release=2, deadline=6, work=3),
    ]
    assert load(jobs, 0, 6) == 5


def test_density_intervalle_vide() -> None:
    jobs = [Job(id=0, release=0, deadline=4, work=2)]
    assert density(jobs, 2, 2) == 0.0


# TODO (E2) : tests de yds(), de is_feasible() et du brute-force.
