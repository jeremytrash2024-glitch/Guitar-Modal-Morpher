# Guitar Modal Morpher : passation après la v1459

Ce document complète la passation v1432 (`docs/passation-v1432.md`). Il ne répète pas tout. Pour la façon d'écrire une grille (champs, référence de la basse, pièges) et la liste des outils de base, lire d'abord la v1432, sections 5 et 6. Ici, on trouve ce qui a changé et ce qui reste à faire.

Session du 26 novembre 2026 : de la v1433 à la v1459.

---

## 1. Où en est le projet

| Élément | Valeur |
|---|---|
| Artifact (claude.ai) | slug `58b79e64-97a5-41f5-b199-4a0f02dc73f8`, https://claude.ai/artifact/BxQFAdNEXNLyPzQoihGfhR |
| Partage de l'artifact | **public**. Toute republication demande `shared_live:"public"` et `artifact_title:"Guitar Modal Morpher"` |
| Version en ligne | v1459, version d'artifact `1795707942-e15f` |
| GitHub | `jeremytrash2024-glitch/Guitar-Modal-Morpher`, branche **`Guitar`** |
| Poussé sur GitHub | tout, jusqu'à la v1459 et ce document |

**Pousser sur GitHub**, seulement quand Jérémy le demande. Cette commande marche après un `add_repo` (accès push) :
```
git -c push.negotiate=true push https://github.com/jeremytrash2024-glitch/Guitar-Modal-Morpher.git Guitar
```

Toujours republier par `edit_version`, avec des remplacements exacts et uniques. **Jamais par `publish_files`.**

**Une édition par grille.** Les générateurs produisent un seul remplacement par grille, qui couvre de la première à la dernière différence. Plusieurs petites éditions dans le même bloc se chevauchaient, ce qui a fait échouer la v1451 au premier essai.

---

## 2. Ce qui a été fait pendant la session

### 2.1 Grilles jazz réécrites en ballade
Toutes ces grilles ont 16 mesures, une partie A et une partie B, la contrebasse `uprightReel`, une mélodie et des réponses écrites, avec les rôles qui s'échangent au tour 2.

| Grille | Version | Le principe |
|---|---|---|
| `jz-ligne-qui-descend` | v1433–1435 | En Sol. La partie B descend par demi-tons. Retour vers Gmaj9 par demi-ton (D7b9 avec Sib en haut, basse Fa# → Sol). Les réponses sont prolongées pour qu'il n'y ait plus de silence dans les deux voix à la fois. |
| `jz-ligne-qui-monte` | v1436 | Partie B par demi-tons, basse par quartes. |
| `jz-carlton-broderie-aigues` | v1437–1438 | En partie B, le Sol reste tenu sur la Mi aiguë, case 3, sous six accords. |
| `jz-carlton-quartes-sans-fonda` (« Quartes et ligne bebop ») | v1441 | Le F13 était un casse-doigt : il est devenu F9. La partie B est une ligne bebop en croches sur de longues septièmes. |
| `jz-diminue-quatre-sorties` | v1442–1445 | Partie A : quatre diminués qui sortent chacun sur un maj7. Partie B : une montée chromatique Cmaj7 → G7. Contrebasse à `basseDb:13`. |
| `jz-triades-superieures` | v1446 | Des triades qui glissent sur une pédale (C9, D/C, F#/C…). |

En v1439–1440, les descriptions des 30 grilles jazz écrites ont été raccourcies au format « Le geste : … Pour improviser : … » (script `c1440.py`). Jérémy : « Le but c'est de jouer ».

### 2.2 La famille de gammes Bebop (v1449–1450)
Elle est ajoutée dans `SCALES` après `japanese`, et `MEM_FAMS` contient maintenant `"bebop"`. Les menus, la mémoire et les quiz fonctionnent avec ces gammes de 8 notes.

| idx | Nom | Formule |
|---|---|---|
| 0 | Bebop dominante | 0 2 4 5 7 9 10 11 |
| 1 | Bebop majeure | 0 2 4 5 7 8 9 11 |
| 2 | Bebop dorienne | 0 2 3 4 5 7 9 10 |
| 3 | Bebop mineure mélodique | 0 2 3 5 7 8 9 11 |

Pour l'utiliser dans un accord : `scale:"G:bebop:0"`.

### 2.3 Les gammes bebop posées sur les grilles (v1449, v1451–1456)
**Règle :** on ne remplace que les gammes « mères » par leur version bebop : dorien → bebop dorienne, mixolydien → bebop dominante, majeur → bebop majeure, mineur mélodique → bebop mineure mélodique. Chaque gamme bebop contient toutes les notes de la gamme qu'elle remplace : une mélodie écrite ne peut donc jamais sortir de la gamme.

**On garde :**
- la gamme diminuée sur les accords dim7 et 7b9 ;
- l'altéré, le locrien et le locrien #2 ;
- les modes de passage dans une tonalité : Sol m7 éolien, Mib maj7 lydien et Ré m7 phrygien dans Anatole ;
- le mineur harmonique, qui n'a pas de version bebop.

| Grille | Version | Gammes bebop |
|---|---|---|
| Quartes et ligne bebop | v1449 | dominante sur Bb9, Eb9 et A7 |
| Barry Harris, sixte diminuée | v1451 | majeure de Do partout, diminués compris |
| Barry Harris, version mineure | v1451 | mineure mélodique de Do partout |
| ii-V-I majeur | v1451 | dorienne sur Dm7 et Fm7, dominante sur G7 et A7, majeure sur Cmaj7 |
| Bird blues | v1452 | dorienne sur les m7, dominante sur les 7 (les b9 et Em7b5 ne changent pas) |
| Blues jazz en Fa | v1453 | dominante sur F9, F7 et Bb7, dorienne sur Cm7 et Gm7 (C7b9 garde la diminuée) |
| Anatole | v1454 | majeure sur Bbmaj7, dorienne sur Cm7, dominante sur F7 et Bb7 |
| Les feuilles mortes | v1455 | partie majeure seulement : Cm7, F7, Bbmaj7 |
| ii-V altéré | v1456 | mineure mélodique sur Do m maj7 |

**Outil :** `outils/g1452.py <base> <sortie> <id> <cNNNN.json>`. Le fichier JSON contient `{"subs":[[noms d'accords en regex, gamme d'origine en regex, nouvelle gamme]], "desc":[ancien texte, nouveau texte]}`. L'outil produit une seule édition. Exemples : `c1452.json` à `c1456.json`.

### 2.4 Le taiko (v1447–1448, v1457–1459)
- **Quatre motifs**, choisis par `_taikoMotifPour(chord, barBeats, grImpose)` :
  - **ternaire** : mesure à 3 ou 6 temps, ou ressenti shuffle ;
  - **moteur** : groove metal, ou tempo ≥ 140 ;
  - **lent** : ballade, ou tempo < 90 ;
  - **fête** : tous les autres cas.
- **Appel et réponse :** les mesures impaires jouent `TAIKO_REPONSES`.
- **Le son *ka*** (v1457) : le cercle du tambour, un clic boisé à peu près moitié moins fort qu'un *ten*. Il est calculé à l'avance avec les autres coups (`_taikoRendre`, trois variantes), joué par `_taikoKa`, et tous les coups passent par `_taikoCoup(type, t, vel)`.
  - Fête : sur les contretemps.
  - Ballade, moteur et ternaire : dans les réponses.
  - Il annonce aussi chaque fin de phrase, sauf si un *don* tombe déjà à cet endroit.
- **Le roulement** (v1458) : Jérémy le trouvait encore « trop ».
  - Il ne joue plus que toutes les 8 mesures et en fin de grille, et il est court : « tere-don », 2 *ten* puis un *don*.
  - Les autres fins de 4 mesures jouent seulement un *ka* puis un *don* de relance.
  - La ballade n'a jamais de roulement.
- **L'*oroshi*** (v1459) : `_taikoOroshi(gr, t0)` est appelé dans `_lancer` de `toggleGridPlay`, seulement si le taiko est allumé et que la grille part du début (`_depuisDebut`).
  - Il dure 2 mesures : des *don* qui accélèrent et montent en force, avec quelques *ten* dans la fin rapide. Le dernier coup tombe un quart de temps avant l'entrée de la grille.
  - En ballade : une mesure, 5 *don* doux.
  - Les coups partent par `setTimeout` rangés dans `_gridPlayTimers`, ce qui permet à l'arrêt de les annuler.
  - Jérémy : « c'est pas mal fait ».

---

## 3. Ce que Jérémy aime : les nouveautés
Les règles de la passation v1432, section 3, valent toujours. Voici ce qui s'y ajoute :

- **Travailler par petites étapes** : « fractionne pour ne pas s'emmêler les pinceaux ». Une grille, ou une étape du taiko, à la fois, publiée et commitée avant de passer à la suivante.
- **Un tableau avant de coder**, et ça vaut aussi pour les changements de son (taiko).
- **Des descriptions courtes, tournées vers le jeu.**
- **Il se sert souvent de la gamme bebop** : la mettre là où une ligne bebop a du sens.
- **Pas de partie B qui tourne en rond.** Le B répétitif du diminué : « ça tourne en rond ». La montée chromatique a plu.
- **Pas de chaîne de dominantes sans relief** : elle est « ennuyante ». La texture bebop a plu.
- **Pas d'accord casse-doigt** (F13). Proposer tout de suite une forme plus simple.
- **Le retour en haut de grille doit se digérer :** préparer la boucle par un mouvement d'un demi-ton.
- **Une grille trop aiguë** se transpose plus bas.
- **Le taiko doit rester sobre :** peu de roulements, des fins de phrase légères.

---

## 4. La basse sur téléphone : nouvelle cible
**La cible passe d'environ −28,5 dB à environ −24 dB en `bandeTel`** (mesuré par `couches.py`). Jérémy trouvait −27,6 dB trop faible, et −23,5 dB lui convient.

Sur le diminué, il a fallu `basseDb:13` avec `basseHarmoniques:-4` (contrebasse `uprightReel`). Une guitare qui double les fondamentales masque la basse : on le compense par `rythmeDb` ou en allégeant le doigté.

---

## 5. Outils ajoutés (dossier `outils/`)

| Outil | Usage |
|---|---|
| `g1452.py` + `cNNNN.json` | remplacer des gammes dans une grille et réécrire la ligne « Pour improviser », en une seule édition (section 2.3) |
| `taikotest3.py` | `python3 taikotest3.py <html>` : liste les coups (D = *don*, t = *ten*, K = *ka*) de chaque motif sur 16 mesures |
| `katest.py` | vérifie que les échantillons *don*, *ten* et *ka* sont calculés, avec leur crête |
| `orotest.py`, `orotest2.py` | positions des coups de l'*oroshi* ; lecture réelle d'une grille japonaise : la grille attend la fin de l'*oroshi*, et la reprise après pause se fait sans *oroshi* |
| `env.py` | enveloppe du mix |
| `bebopui.py`, `bebopui2.py` | contrôle des menus avec la famille Bebop |
| `c1440.py` | les descriptions courtes |
| `g1433.py` à `g1459.py` | les générateurs de chaque version, à prendre comme modèles |

Les chemins `/tmp/t/` sont écrits en dur : recopier `outils/*` dans `/tmp/t/` avant de s'en servir.

---

## 6. Ce qui reste à faire

### 6.1 Grilles jazz pas encore écrites
C'est la liste v1432, section 7.1, sans les six grilles faites pendant cette session :

`jz-so-what`, `jz-constant-varie` (sautée exprès), `jz-drop2-voiceleading`, `jz-cm-tour-riche`, `jz-descente-eclats`, `jz-mesure-impaire`, `jz-wes-quintes-fam` (le Fm7 4-6-6-8-6-x, avec 4 cases d'écart, est à refaire avant tout), `jz-trois-paliers`, `jz-tonalites-manquantes`, `jz-modulations-tierces-min`, `jz-modulations-tierces`, `jz-substitution-triton`, `jz-rhythm-changes-pont`, `jz-douze-visages`, `jz-echmel-melodique`, `jz-echmel-altere`, `jz-echhmaj-dorien-b5`.

Pour chacune, se demander si une gamme bebop a sa place sur certains accords.

### 6.2 Taiko
- **Réglage par grille :** forcer un motif ou couper l'*oroshi*. C'est mis de côté : à faire seulement si une grille sonne mal avec le motif choisi automatiquement.

### 6.3 Pistes ouvertes
Ce sont celles de la v1432, section 7.2 :
- substitutions tritoniques à retravailler ;
- allonger et ralentir les anciennes grilles écrites, puis remesurer leur basse avec la nouvelle cible de −24 dB ;
- baisser ou non le Solo à +5 dB.

---

## 7. Mémo pour démarrer la prochaine conversation
1. `add_repo` (accès push), puis cloner la branche `Guitar` : son `index.html` est la v1459 exacte.
2. Recopier `outils/*` dans `/tmp/t/`. Installer Playwright si besoin.
3. `get_artifact` pour obtenir la `base_version` (la v1459 est `1795707942-e15f`, ou une version plus récente).
4. Lire la section 3 de ce document et la section 3 de la passation v1432.
5. Pour chaque changement : tableau, accord de Jérémy, générateur, vérifications (`verif.py`, `play15.py`, `couches.py` pour la basse), publication par `edit_version` (une édition par grille), commit local.
