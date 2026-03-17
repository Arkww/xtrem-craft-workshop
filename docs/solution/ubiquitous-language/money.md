# Concept

Objet valeur representant un montant dans une devise donnee.

## Properties

- `amount: float` : montant monetaire.
- `currency: Currency` : devise du montant.

## Responsibilities

- Valider qu'un montant est non negatif a la creation.
- Supporter les operations arithmetiques dans la meme devise:
- addition (`+`) avec `Money`, `int`, `float`
- multiplication (`*`) par `int` ou `float`
- division (`/`) par `int` ou `float` strictement positif
- Fournir l'egalite metier (`amount` et `currency`).
- Fournir une representation texte et debug (`__str__`, `__repr__`).

## Invariants

- `amount >= 0` pour toute instance.
- L'addition de deux `Money` exige la meme devise.
- L'addition/multiplication avec un nombre negatif est interdite (`ValueError`).
- La division par 0 ou par un nombre negatif est interdite (`ValueError`).

## Collaborators

- `Currency`
- `Bank` (pour la conversion inter-devises)
- `Portfolio` (aggregation de montants)
