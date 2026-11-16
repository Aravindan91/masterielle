"""Algorithme YDS (Yao-Demers-Shenker, FOCS 1995).

Squelette à compléter à l'étape E2 du plan (voir ../plan.md).

Rappel du problème
------------------
Une instance est une liste de tâches ``(release, deadline, work)``. Le processeur tourne à une
vitesse ``s(t) >= 0`` réglable, exécute une seule tâche à la fois, et les tâches sont
préemptives. La puissance vaut ``s**2``, donc l'énergie est ``∫ s(t)² dt``.

À vitesse constante ``s``, exécuter ``w`` unités de travail coûte ``w / s`` de temps et
``w * s`` d'énergie : **énergie = travail × vitesse**.

YDS en 5 étapes
---------------
1. Points remarquables : toutes les dates ``release`` et ``deadline``, triées.
2. Charge d'un intervalle ``[a, b]`` : travail des tâches **entièrement contenues** dans
   ``[a, b]``. Densité = charge / (b - a).
3. Intervalle le plus chargé ``I*`` : densité maximale.
4. Sur ``I*`` : vitesse constante = densité de ``I*``, tâches ordonnées par date limite
   croissante (EDF).
5. Retirer ces tâches, recommencer sur le temps restant.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Job:
    """Une tâche : disponibilité, date limite, quantité de travail."""

    id: int
    release: int
    deadline: int
    work: int

    def __post_init__(self) -> None:
        if self.release > self.deadline:
            raise ValueError(f"tâche {self.id} : release > deadline")
        if self.work < 0:
            raise ValueError(f"tâche {self.id} : work < 0")


@dataclass(frozen=True)
class Segment:
    """Un morceau d'ordonnancement : [start, end) à vitesse constante."""

    start: int
    end: int
    speed: float
    job: int | None

    @property
    def energy(self) -> float:
        return (self.end - self.start) * self.speed**2


def total_work(jobs: list[Job]) -> float:
    """Travail total d'une liste de tâches."""
    return sum(job.work for job in jobs)


def contained(jobs: list[Job], a: float, b: float) -> list[Job]:
    """Tâches entièrement contenues dans l'intervalle [a, b]."""
    return [job for job in jobs if a <= job.release and job.deadline <= b]


def load(jobs: list[Job], a: float, b: float) -> float:
    """Charge de [a, b] : travail des tâches entièrement contenues dans [a, b]."""
    return total_work(contained(jobs, a, b))


def density(jobs: list[Job], a: float, b: float) -> float:
    """Densité de [a, b] : charge / longueur. Vaut 0 pour un intervalle vide."""
    if b <= a:
        return 0.0
    return load(jobs, a, b) / (b - a)


def critical_interval(jobs: list[Job]) -> tuple[float, float]:
    """Intervalle [a, b] de densité maximale.

    TODO (E2) : ne parcourir que les intervalles dont les bornes sont des dates remarquables,
    et renvoyer aussi la densité. En cas d'égalité, prendre l'intervalle le plus à gauche.
    """
    raise NotImplementedError("E2 : à implémenter")


def yds(jobs: list[Job]) -> list[Segment]:
    """Ordonnancement optimal au sens YDS.

    TODO (E2) :
      - boucle : tant qu'il reste des tâches non ordonnancées,
      - trouver l'intervalle critique,
      - répartir les tâches de cet intervalle en EDF à vitesse = densité,
      - marquer ces tâches comme faites.
    """
    raise NotImplementedError("E2 : à implémenter")


def energy(segments: list[Segment]) -> float:
    """Énergie totale d'un ordonnancement."""
    return sum(seg.energy for seg in segments)


def is_feasible(jobs: list[Job], segments: list[Segment]) -> bool:
    """Vérifie que chaque tâche est exécutée, dans sa fenêtre, et sans chevauchement.

    TODO (E2) : contrôle à écrire avant même l'algorithme, c'est le test de référence.
    """
    raise NotImplementedError("E2 : à implémenter")


if __name__ == "__main__":
    # Exemple jouet de la spec (docs/spec.md).
    exemple = [
        Job(id=0, release=0, deadline=4, work=2),
        Job(id=1, release=2, deadline=6, work=3),
    ]
    print("charge [0,6] =", load(exemple, 0, 6))
    print("densité [0,6] =", density(exemple, 0, 6))
    print("total travail =", total_work(exemple))
