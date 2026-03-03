# Backlog

## What can be improved in the codebase ?

- La syntaxe du code est trop complexe. Des suites d'instructions sont concaténées pour être effectuées en une ligne, ce qui fait que le code est difficile à comprendre et est donc difficile à analyser / déboguer

- Absence totale de doc, on ne sait pas ce que le code fait, on ne sait pas quels cas sont testés

- Les tests ne couvrent que très peu de cas

- Certains paramètres ne sont pas utilisés (paramètre currency dans MoneyCalculator)

- Le message d'erreur n'est pas explicite (currency1 -> currency2 n'explique en rien le problème)

- Méthodes inutiles, les méthodes de MoneyCalculator sont des simples additions, multiplications et divisions et ne sont donc pas utiles (en tout cas pour le moment)

- Les assert dans les tests n'ont pas de messages donc on ne sait pas ce qui est testé (problématique lorsqu'il n'y a pas d'erreur)
