# Guitar Modal Morpher : passation après la v1477

Ce document fait suite à la passation v1459. Lire d'abord la v1459, puis la v1432 (sections 3, 5 et 6).

Sessions du 26 et du 27 novembre 2026 : de la v1460 à la v1477.

## 1. Où en est le projet

| Élément | Valeur |
|---|---|
| Artifact | slug `58b79e64-97a5-41f5-b199-4a0f02dc73f8`, partage **public** (`shared_live:"public"`, `artifact_title:"Guitar Modal Morpher"`) |
| Version en ligne | v1477, version d'artifact `1795810511-5b4d` |
| GitHub | branche `Guitar`. La v1474 est poussée ; les v1475 à v1477 sont commitées en local, à pousser |

Toujours publier par `edit_version`. Jamais par `publish_files`.

## 2. Ce qui a été fait

**Grilles jazz passées en ballade.** Elles ont toutes 16 mesures (A + B), sont à 72 bpm en rythme droit, utilisent la contrebasse `uprightReel` (`basseDb:12`, `basseHarmoniques:-4`), ont une mélodie de sax écrite avec des réponses de guitare, et les rôles s'échangent au tour 2.

| Grille | Version | Le principe |
|---|---|---|
| `jz-wes-quintes-fam` | v1460-1461 | deux tours de quintes, octaves à la Wes |
| `jz-so-what` | v1462 | pédale de Ré, réponse « amen » en accords écrits |
| `jz-drop2-voiceleading` | v1463 | la même cadence en drop 2 à trois hauteurs |
| `jz-cm-tour-riche` | v1464 | Lab et Sib qui montent ensemble, partie B chez Mib, CmMaj7 |
| `jz-descente-eclats` | v1465 | les éclats de La m transposés sur Ré m |
| `jz-mesure-impaire` | v1467 | 5/4 et 7/8, la basse garde son appui |
| `jz-trois-paliers` | v1468 | quatre paliers d'un demi-ton |
| `jz-paliers-quarte` (nouvelle) | v1469 | quatre paliers qui montent d'une quarte |
| `jz-tonalites-manquantes` | v1470-1471 | une porte diminuée, quatre tonalités |
| `jz-modulations-tierces-min` | v1473 | une note tenue traverse quatre tonalités |
| `jz-modulations-tierces` | v1474 | par tierces majeures, la quinte devient la septième majeure |
| `jz-substitution-triton` | v1475 | une seule tonalité ; même cadence, autre basse |
| `jz-rhythm-changes-pont` | v1476 | A en Sib, pont : la septième glisse vers la tierce suivante |
| `jz-douze-visages` | v1477 | **exercice** : trois formes, douze tonalités, 96 bpm, pas de mélodie |

**Autres changements :**
- **v1466 :** sur les gammes bebop, la fonction Simplifier, l'arpège du repère et la note caractéristique se calculent sur la gamme mère, sans la note de passage (`_gammeMere`). Avant, la bebop dorienne affichait un La 7 et perdait le Si et le Do.
- **v1472 :** frottements tenus retirés de sept ballades.

**La liste est close.** Les Échelles (35 grilles) restent telles quelles, à la demande de Jérémy. Leur intérêt est la comparaison d'une grille à sa cousine.

## 3. Ce que Jérémy a dit pendant ces sessions

- **Sur les modulations :** la quarte au-dessus sonne moins vieillot que le demi-ton qui glisse.
- **Sur la complexité :** « trop complexe, l'oreille ne se pose jamais ». Une seule tonalité, une tonique tenue deux mesures, un seul mécanisme. La substitution tritonique refaite dans ce sens lui a plu.
- **Pour les doublons :** il préfère deux grilles séparées plutôt qu'un remplacement (paliers en demi-ton et paliers à la quarte).
- **Sur la sixte :** éviter de la tenir dans la mélodie (Em6, Cm b6 remplacé par CmMaj7).

## 4. Vérifications avant publication

- `verif.py`, `play15.py`, `span.py`, `couches.py` (basse vers −23 dB en `bandeTel`).
- **Nouveau : `outils/frottements.py <html> <id>`.** Il signale toute seconde ou neuvième mineure tenue un temps ou plus, entre le sax ou la guitare et l'accord ou la basse. Pour les grilles en `fondamentale:"nom"`, ignorer les lignes « basse », qui sont calculées avec une mauvaise référence.
- **Construire une grille :** `outils/mkNNNN.py` lit `dataNNNN.txt` (accords, basse, mélodie, réponses), puis `g1468.py` sert de gabarit. Les données sont dans le dépôt.
