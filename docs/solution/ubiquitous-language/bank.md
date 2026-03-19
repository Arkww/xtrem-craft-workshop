# Concept

Service de conversion monetaire base sur des taux de change entre paires de devises basé sur une devise pivot.

## Properties

- `_exchange_rate: Dict[str, float]` : dictionnaire des taux, indexe par cle `FROM->TO` (ex: `USD->EUR`).

## Responsibilities

- Définir une devise pivot
- Enregistrer un taux de change avec une devise (`add_exchange_rate`).
- Creer une banque preconfiguree avec un taux initial (`create`).
- Convertir un `Money` vers une devise cible (`convert`).
- Lever une erreur explicite si aucun taux n'existe pour la conversion demandee.

## Invariants

- Si la devise source et la devise cible sont identiques, le montant est conserve.
- Une conversion entre devises differentes exige la presence d'un taux `devise->cible`.
- En absence de taux, une `MissingExchangeRateError` est levee.

## Collaborators

- `Money`
- `Currency`
- `MissingExchangeRateError`
