"""Entrée / sortie JSON : le contrat d'échange entre Python et Lean.

Le format exact est décrit dans ``docs/spec.md``, section 2. Toute évolution du format doit
être répercutée dans ce fichier **et** dans ``lean/Masterielle/Checker.lean``.
"""

from __future__ import annotations

import json
from pathlib import Path

from yds import Job, Segment


def load_instance(path: str | Path) -> tuple[str, list[Job]]:
    """Lit une instance depuis un fichier JSON.

    TODO (E2) : valider le schéma (champs obligatoires, types, r <= d, w >= 0).
    """
    raise NotImplementedError("E2 : à implémenter")


def dump_instance(path: str | Path, name: str, jobs: list[Job]) -> None:
    """Écrit une instance au format JSON."""
    raise NotImplementedError("E2 : à implémenter")


def dump_solution(
    path: str | Path,
    instance_name: str,
    segments: list[Segment],
    certificate: dict,
) -> None:
    """Écrit une solution + son certificat au format JSON."""
    raise NotImplementedError("E2 : à implémenter")


def load_solution(path: str | Path) -> dict:
    """Lit une solution JSON et renvoie le dictionnaire brut."""
    return json.loads(Path(path).read_text(encoding="utf-8"))
