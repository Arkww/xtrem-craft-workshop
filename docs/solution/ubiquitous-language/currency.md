# Concept

Type de devise supporte par le domaine metier.

## Properties

- Valeurs enum disponibles:
- `USD`
- `EUR`
- `KRW`

## Responsibilities

- Representer de facon explicite et sure les devises autorisees.
- Fournir une valeur stable (`value`) pour composer les cles de taux de change (`USD->EUR`).

## Invariants

- Une devise est toujours l'une des valeurs de l'enumeration.
- Les codes devises sont des chaines ISO-like en majuscules (`USD`, `EUR`, `KRW`).

## Collaborators

- `Money`
- `Bank`
