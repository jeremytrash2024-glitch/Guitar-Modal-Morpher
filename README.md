# Morphing modal pour guitare 🎸

Aide à la composition pour guitariste et professeur de théorie mise en pratique : une application pour composer et improviser à la guitare et à la basse. Elle part de ce qu'on entend, pas d'une théorie à apprendre par cœur.

**▶ Ouvrir l'application : https://jeremytrash2024-bug.github.io/guitar-modal-morpher**

Tout tient dans un seul fichier HTML. Rien à installer, pas de compte à créer, aucun serveur derrière. Une fois la page chargée, elle fonctionne sans connexion.

## Ce qu'on y fait

- **Voir le manche** : gammes et modes en pastilles numérotées par degré, tonique cerclée d'or, cordes à vide à gauche du sillet.
- **Jouer des grilles** : plus de 230 progressions courtes, rangées par famille (rock, jazz, fusion, progressif, cinéma…) et par leçon. Chacune est accompagnée par une basse et une batterie.
- **Changer de couleur** : on passe d'un mode à l'autre sur la même tonique pour entendre ce qui bouge et ce qui reste.
- **Suivre la gamme de chaque accord** : le manche affiche la gamme, l'arpège, ou les deux.
- **Travailler le rythme** : grooves, métriques impaires (7/8, 5/4…), feel posé ou poussé, anticipations. Certaines grilles sont des « remix » : mêmes accords, mêmes doigtés, seul le rythme change.

## Testé sur

- Android (téléphone Honor)
- iPhone

Le desktop n'a pas été testé en profondeur. Ça devrait marcher dans un navigateur récent, mais sans garantie.

> Astuce son : sur un haut-parleur de téléphone, active le réglage de basse « Basse HP tél. » pour que la basse reste audible.

## Contenu du dépôt

- `index.html` : l'application (build v872)
- `README.md` : ce fichier
- les fichiers `gmm-tests-….js` : suites de tests des versions 870 à 872

## Les tests

Les suites lisent le vrai code de `index.html` et le rejouent dans Node.js, sans aucune dépendance. Depuis la racine du dépôt :

- `node gmm-tests-870-groove-accord.js index.html`
- `node gmm-tests-871-remix-timmons.js index.html`
- `node gmm-tests-872-remix-timmons-mi.js index.html`

Chaque suite affiche `VERT — n ok, 0 ko` quand tout passe.

- **870** : un groove écrit sur un accord est bien joué en lecture normale. Le choix manuel du menu Groove garde la main, et un groove qui déborderait de sa mesure est refusé.
- **871** : le remix de « Lumière en La » garde ses huit accords et ses doigtés. La durée totale ne change pas, et l'arc ballade → rock → ballade est vérifié par le vrai moteur de groove.
- **872** : le remix du « Mi qui ne bouge pas ». Le Mi aigu reste à vide sur chaque accord, on s'attarde sur les couleurs riches (9, 11, 6) et on passe sur les simples.

**Sabotages.** Chaque suite contient de petites corruptions volontaires qui prouvent qu'un test peut vraiment rougir. Par exemple `node gmm-tests-870-groove-accord.js index.html sabotage 1` doit afficher `ROUGE`.

**Comparer avec une version d'avant.** Les suites 871 et 872 acceptent une ancienne version en second argument, pour vérifier que le remix n'a touché que le rythme. Par exemple `node gmm-tests-871-remix-timmons.js index.html ancienne-version.html`.

Ces trois suites ne couvrent que les changements des versions 870 à 872.

## Crédits

Conçu par Jérémy, guitariste et bassiste. Développé avec l'aide de Claude (Anthropic).

## Licence

Aucune licence pour l'instant : le code est visible, mais pas librement réutilisable.
