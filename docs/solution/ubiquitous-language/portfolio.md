# Concept

Aggregateur de plusieurs montants (`Money`) potentiellement dans des devises differentes.

## Properties

- `monies: List[Money]` : collection des montants detenus dans le portefeuille.

## Responsibilities

- Ajouter un montant au portefeuille (`add_money`).
- Evaluer la valeur totale du portefeuille dans une devise cible (`evaluate_money`).
- Deleguer chaque conversion au `Bank` fourni.
- Retourner le resultat sous forme d'un `Money` dans la devise demandee.

## Invariants

- Le portefeuille contient uniquement des objets `Money`.
- L'evaluation commence a `0.0` dans la devise cible puis additionne les montants convertis.
- Si une conversion requise n'a pas de taux dans la banque, l'evaluation echoue via l'erreur du `Bank`.

## Collaborators

- `Money`
- `Bank`
- `Currency`
