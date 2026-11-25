# Guitar Modal Morpher : passation après la v1432

Ce document reprend tout ce qu'il faut savoir pour continuer le travail dans une nouvelle conversation : l'état de l'app, la façon d'écrire une grille, les outils de vérification, les réglages de volume, les erreurs déjà rencontrées et ce qui reste à faire.

Session du 25 novembre 2026 : de la v1386 à la v1432.

---

## 1. Où en est le projet

| Élément | Valeur |
|---|---|
| Artifact (claude.ai) | slug `58b79e64-97a5-41f5-b199-4a0f02dc73f8`, https://claude.ai/artifact/BxQFAdNEXNLyPzQoihGfhR |
| Partage de l'artifact | **public**. Toute republication demande `shared_live:"public"` et `artifact_title:"Guitar Modal Morpher"` |
| Version en ligne | v1432, version d'artifact `1795627731-4bbb` |
| GitHub | `jeremytrash2024-glitch/Guitar-Modal-Morpher`, branche **`Guitar`**, fichier `index.html` |
| Dernier commit | `2848512` (v1432) |
| Taille | environ 14,5 Mo, en un seul fichier HTML |

**Pousser sur GitHub :**
```
git push -q https://github.com/jeremytrash2024-glitch/Guitar-Modal-Morpher.git Guitar
```
On ne pousse **que quand Jérémy le demande**.

**Attention à la taille du fichier.** La taille que l'artifact annonce diffère de quelques milliers d'octets de la copie locale, même quand le contenu est identique. Ne jamais republier le fichier entier par `publish_files` pour cette raison : on ne pourrait pas savoir ce que la copie locale écraserait. Toujours republier par `edit_version`, avec des remplacements exacts et uniques. La copie de GitHub, elle, correspond octet pour octet à la copie locale.

---

## 2. Ce qui a été fait pendant la session

### 2.1 Le shuffle (v1386 à v1388)
- **4 nouveaux grooves**, tous avec `shuffle:true` :
  - `shuffleBlues` : kit rock, en strum ;
  - `shuffleHalf` : ghost notes de caisse claire à .333, en arpège ;
  - `boogieShuffle` : guitare boogie ;
  - `swingLent` : kit jazz, le woodblock sert de ride, en comping.
- **Nouvelles lignes de basse :** `boogie_shuffle` et `half_shuffle`.
- **Un ressenti « Shuffle »** qui swingue n'importe quelle grille, Solo et Phrase compris. Il est calculé par `_swingLag(beat, beatSec, chord)` :
  - x.5 passe à x.667, x.25 à x.333, x.75 à x.833 ;
  - le ratio s'allège au-dessus de 120 bpm ;
  - les positions de triolet (x.333) restent telles quelles.
- **Bug corrigé :** la basse était décalée au démarrage. On attend maintenant, 2 s au plus, que les banques de basse et de guitare enregistrées soient décodées (`st.fini`). Un jeton `_gridLanceJeton` ignore les démarrages périmés.

### 2.2 Les listes en tête de l'onglet Grilles
- **`NOUVEAUTES` :** les grilles retouchées, côte à côte, **la plus récente d'abord**.
- **`SHUFFLE_ESSAI` :** la liste éphémère « 🎷 Passées en shuffle ». Chaque entrée est `[id, {props}]`, appliquée par `Object.assign` au chargement. Le groupe est construit par `_groupeShuffle()`, qui tient aussi une table `versions[id]` pour les étiquettes.
- Retirer une grille de `SHUFFLE_ESSAI` la remet en rythme droit.

### 2.3 Les réglages de volume

| Réglage | Valeur | Remarque |
|---|---|---|
| `SAX_DB_MESURE` | 20.3 | sax +4 dB pour toutes les grilles (v1399) |
| `phraseDb` des grilles écrites | **−1** | il était à +5, puis à +2 (v1416), puis à −1 (v1418) : Jérémy l'a trouvé trop fort deux fois |
| `soloDb` | 5 | la guitare solo |
| `rythmeDb` | 5 | la guitare rythmique (9 sur Bird blues et Wes, jugée trop faible) |
| `basseDb` | −3 par défaut | voir la section 4 pour la basse |

### 2.4 Les grilles jazz avec sax écrit
Toutes ont `soloAuto:true` (le Solo s'allume tout seul), `phraseAuto:true`, deux tours écrits (`phrase` et `phrase2`, `soloEcrit` et `soloEcrit2`), et la version notée dans `NOUVEAUTES`.

| Grille | Version | bpm | Mesures | Le mécanisme | Ce qui reste immobile |
|---|---|---|---|---|---|
| `jz-ii-v-i-maj` ii-V-I majeur, le socle | v1432 | 72 | 16 | les chutes Do → Si et Fa → Mi ; en partie B, le Mi devient Mib sur Fa m7 puis redevient Mi | le Sol, vers lequel l'autre voix revient toujours |
| `jz-anatole` Anatole en ballade | v1429 | 70 | 8 | une mélodie lente qui revient se poser sur le Ré | le Ré tenu (Réb sur Mi dim7) |
| `jz-drop2` Drop-2 en montée | v1426 | 92 | 8 | Mi Sol Si en renversements qui montent, puis une forme qui recule d'un degré | le Mi |
| `jz-hongrois` Mineur hongrois | v1422 | 144 | 8 | les deux secondes augmentées, Mib–Fa# et Lab–Si, vers le haut puis vers le bas | la voix lente Mib, Fa |
| `jz-tritone-chain` Substitutions tritoniques | v1419 | 138 | 4 | les deux notes-guides descendent chacune leur tour | l'autre note-guide. Jérémy l'a trouvée **moyenne** |
| `jz-constant-lydien` Constant structure lydienne | v1427 | 96 | 8 | à l'aller, la #11 tombe sur la fondamentale suivante ; au retour, la fondamentale monte sur la #11 | le Ré |
| `jz-ii-v-altere` ii-V altéré | v1427 | 126 | 8 | le Si, tierce du Sol 7 alt, ne monte pas : il devient la 7e majeure du Do m maj7 ; pont sur Lab maj7 | le Si |
| `jz-quartal-dorien` Quartal dorien | v1427 | 96 | 8 | Mi La Ré à la même hauteur, recolorés par 8 accords ; le motif est à l'envers en partie B | le motif lui-même |
| `jz-wes-solmineur` esprit Wes | v1412 | 152 | 8 | un riff en octaves, puis la ligne des notes-guides | les notes-guides tenues |
| `jz-bird-blues` Bird blues en Fa | v1412 | 148 | 12 | une cellule de ii-V transposée, par tons puis par demi-tons | — |
| `jz-blues-mineur-do` Blues mineur | v1411 | 104 | 12 | la forme AAB, la même phrase sur Do m puis sur Fa m | le Mib |
| `jz-cycle-tierces` Cycle par tierces | v1410 | 65 | 4 | un motif transposé d'une tierce majeure (Do → Lab → Mi) | la note commune |

Grilles écrites plus tôt dans la session : `jz-m7b5-tiroirs-la`, `jz-pivot-do-sol`, `jz-basse-descend`, `jz-deux-noms-un-accord`, `jz-harris-sixte-min`, `jz-harris-sixte-dim`, `jz-so-what-deplace`, `jz-ballade-double-time`, `jz-notes-qui-frottent`, `jz-blues-gamme-mineure`, `jz-ballade-mib`, `jz-autumn`, `jz-bobby-timmons-soul-fam`, `jz-blues-fa`.

**Grilles supprimées :**
- `jz-fa-diese-tenace` (v1406) : doigtés trop écartés, « tendinite garantie » ;
- `jz-polytonal` (v1424) : Jérémy ne l'aimait pas.

**Doigtés refaits :**
- **Mineur hongrois :** l'ancien Sol 7b9 3-x-3-1-0-1 était injouable. Les deux diminués utilisent maintenant la même forme, x-x-1-2-1-2 puis x-x-3-4-3-4, avec `fondamentale:"nom"` pour que la basse joue le Sol.
- **Drop-2 :** le premier Do maj7 x-x-2-4-1-3 était dur à jouer. Il est remplacé par le Do maj7 ouvert x-3-2-0-0-0.

**Erreurs de gamme corrigées** dans les grilles d'origine : Do m7 dans Anatole, et Ré m7 dans le ii-V-I, qui affichaient la gamme d'une autre fondamentale.

---

## 3. Ce que Jérémy aime, et ce qu'il n'aime pas

Les retours de la session, à appliquer dès la prochaine grille.

**Ce qui marche :**
- **Les ballades lentes, de 65 à 75 bpm.** Les mêmes accords lui parlent beaucoup plus quand ils ont le temps de sonner. Anatole à 150 bpm : « j'aime pas du tout » ; à 70 bpm : « beaucoup mieux ».
- **8 mesures au minimum, 16 c'est encore mieux.** En dessous, même une bonne idée tourne en boucle trop vite (« beaucoup trop court »).
- **Une partie B qui part ailleurs et revient.** Le ii-V-I avec sa partie B : « Excellent : le solo est sorti tout seul ».
- **Un motif reconnaissable qu'on transpose.** Il a mieux aimé le cycle par tierces une fois le motif transposé.
- **La forme AAB** du blues mineur : « J'aime beaucoup ».
- **Un dialogue entre les deux voix :** l'une répond pendant les notes tenues de l'autre, plutôt que de tenir une nappe.
- **Une mélodie qui respire :** des silences d'un demi-temps après les notes tenues.

**Ce qui ne marche pas :**
- **Le bebop rapide et bavard** (riff à 150 bpm, deux accords par mesure).
- **Les mécanismes plus intéressants à comprendre qu'à écouter** : les substitutions tritoniques étaient « moyennes ».
- **Ce qui est trop répétitif** : une grille de 2 mesures, la même phrase toutes les 3 s.
- **Le shuffle sur des grilles modales ou non blues** : ça « sonne même faux ». Le shuffle ne va qu'au langage blues. Le hongrois, le drop-2, le ii-V-I et Anatole sont en rythme droit.
- **Le sax trop fort.**
- **La basse qu'on n'entend pas sur le téléphone** (voir la section 4).

**Règles de doigtés :**
- 4 doigts au plus.
- **Pas d'écart de 4 cases ou plus.** Vérifier avec `span.py` avant de proposer une grille.
- Pas les mêmes cordes à vide sous tous les accords ; de vrais accords où la main bouge.
- Quand Jérémy dit qu'un accord est dur, proposer un remplacement plus simple, de préférence la même forme déplacée.

**Façon de travailler :**
- **Avant de coder, montrer un tableau** des accords et doigtés, avec le mécanisme et ce qui reste immobile, et attendre son accord.
- Mesurer dans le code avant d'affirmer quoi que ce soit.
- Noms de notes avec une majuscule : La, Ré, Fa#.
- Pas de reggae.
- Firecrawl pour les recherches.
- Il écoute sur son téléphone, un Honor 90 Smart.

---

## 4. La basse sur téléphone : la règle à retenir

Un haut-parleur de téléphone ne restitue presque rien sous 300 Hz. La mesure de référence est donc le niveau de la couche basse **dans la bande 300–3000 Hz**, calculé par `couches.py`, champ `bandeTel`.

- **Cible : environ −28,5 dB en `bandeTel`.** C'est le niveau du Blues mineur, que Jérémy trouve équilibré.
- La guitare rythmique est autour de −33 dB et le sax autour de −25 dB.

**Ce qui a été appris :**
- **La basse de synthèse par défaut ignore `basseDb`.** Pour régler le volume, il faut une basse enregistrée : `basseSon:"fingerReel"`, `"fretlessReel"` ou `"uprightReel"`.
- **`basseHarmoniques`** (−16 par exemple, −4 pour beaucoup d'harmoniques) ajoute des harmoniques qui rendent la basse audible sur téléphone.
- **Une note grave tenue toute une mesure en tempo lent s'éteint** et mesure très bas. Il vaut mieux la rejouer deux fois par mesure, en pédale pulsée.
- **Réglages qui marchent :**

| Basse | Réglage | `bandeTel` |
|---|---|---|
| contrebasse `uprightReel` | `basseDb:7, basseHarmoniques:-4` | −28,6 dB |
| `fingerReel` | `basseDb:5, basseHarmoniques:-16` | −28,5 dB |
| `fretlessReel` | `basseDb:-3, basseHarmoniques:-16` | −27 dB |

- Pour une ballade jazz, la contrebasse enregistrée (`uprightReel`) est le bon son.

**Toujours mesurer la basse après avoir écrit une grille**, et ajuster si elle est à plus de 2 dB de la cible.

---

## 5. Comment une grille écrite est construite

### 5.1 Les champs d'une grille
```js
{id:"jz-xxx", soloAuto:true,
 phrase:[["Note",temps,durée],...],    // sax au tour 1, temps global en temps (beats)
 phrase2:[...],                         // sax au tour 2
 /* commentaire de version */
 phraseAuto:true, phraseDb:-1, soloDb:5,
 basseSon:"uprightReel", basseDb:7, basseHarmoniques:-4,   // si basse enregistrée
 rythmeDb:5, preset:"ballade",          // preset pour les ballades
 fondamentale:"nom",                    // si les doigtés n'ont pas leur fondamentale à la basse
 lecons:{...}, root:"C", scale:"C:0", name:"…", tempo:72, groove:"jazz",
 desc:"Le geste : … À écouter : … Pour improviser : … Tout est écrit : …",
 chords:[
  {name:"Dm7", beats:4, voicing:"x-5-3-5-3-x", scale:"D:1",
   basseLigne:[[temps,demi-tons depuis la référence,durée],...],
   soloEcrit:[[temps local,"Note",durée,"vib"?],...],   // guitare au tour 1
   soloEcrit2:[...]},                                     // guitare au tour 2
  ...]}
```

### 5.2 Règles de fonctionnement
- **Chaque accord doit avoir `soloEcrit` et `soloEcrit2`**, même vides (`[]`).
- Dans une grille écrite, un accord sans `soloEcrit` reste muet.
- `phrase2` et `soloEcrit2` sont joués aux tours impairs.
- **Le format de `scale` est « fondamentale de l'accord : mode ».** Par exemple `"D:1"` pour Ré dorien, `"G:melodicMinor:6"` pour Sol altéré, `"A#:melodicMinor:3"` pour Sib lydien dominant. Ne pas confondre avec la tonalité de la grille.
- **La référence de la basse (`basseLigne`) :**
  - grille normale : `ref = note la plus grave du doigté − 12`, ramenée sous 45 (`while(m>45) m-=12`) ;
  - grille avec `fondamentale:"nom"` : `ref = 28 + ((classe de la fondamentale − 4) mod 12)`.
  - `lib.py` fournit `low()`, et les générateurs définissent `reg()` / `bl()` (cas normal) ou `refnom()` (cas `"nom"`).

### 5.3 Méthode qui a marché
1. Lire la grille d'origine, avec ses doigtés et sa gamme.
2. Proposer à Jérémy un tableau : accords, doigtés, écarts, le mécanisme audible, ce qui reste immobile, les deux tours. Attendre son accord.
3. Écrire un générateur Python `gXXXX.py`, en partant de la copie locale de la version précédente. Il remplace le bloc de la grille et met à jour `NOUVEAUTES`, `SHUFFLE_ESSAI` et la table `versions`.
4. Lancer toutes les vérifications (section 6).
5. Publier par `edit_version` avec les remplacements produits par le générateur (`eXXXX.json`).
6. Expliquer brièvement : la phrase, ce qui est tenu, la basse mesurée, et les frottements restants avec leur raison.

### 5.4 Pièges déjà rencontrés
- **La fin du bloc d'une grille :** chercher `]}]},` (ou `\n]},` si les accords sont sur plusieurs lignes), et pas `]},`, qui apparaît déjà dans `soloEcrit:[...]]},` au premier accord. En v1421, cette erreur a cassé le JS.
- **Une description ajoutée avant le dernier `",\n`** peut tomber dans le champ `degrees` au lieu de `desc`. Viser `'",\ndegrees:'` quand il existe.
- **Un commentaire `//` dans une liste d'accords jointe** casse le JS : utiliser `/* */`.
- **`J()` (JSON compact) remplaçait `0.5` par `.5` dans `10.5`.** Il est corrigé avec un lookbehind négatif.
- **L'ancre de suppression dans `SHUFFLE_ESSAI`** doit être la ligne *précédente d'origine*. Vérifier par `grep` qu'il ne reste qu'une entrée.
- **La basse de synthèse et `basseDb`** : voir la section 4.
- Une note en dehors des temps de la grille (riff trop long sur le dernier accord) déborde : vérifier que les temps tiennent dans `beats`.

---

## 6. Les outils de vérification (dossier `outils/`)

Ils tournent avec Playwright (Chromium) sur la copie locale. Ils étaient dans `/tmp/t/` pendant la session : les recopier là, car certains chemins sont écrits en dur, comme `t2.py` qui écrit `/tmp/t/tour2.html` et les générateurs qui importent depuis `/tmp/t`.

| Outil | Usage | Ce qu'il vérifie |
|---|---|---|
| `verif.py` | `python3 verif.py <html> <id>` | notes hors gamme, demi-tons entre le Solo et la basse, au tour 1 |
| `t2.py` | `python3 t2.py <html> <id>`, puis `verif.py /tmp/t/tour2.html <id>` | fabrique une copie où `phrase2` et `soloEcrit2` remplacent le tour 1, pour vérifier le tour 2 |
| `ph.py` | `python3 ph.py <html> <id>` | la Phrase contre le Solo et contre les notes des accords |
| `pb2.py` | `python3 pb2.py <html> <id>` | la Phrase contre la basse, sur les deux tours |
| `play15.py` | `python3 play15.py <html> <id>` | lecture pendant 15 s : position du curseur et erreurs JS |
| `span.py` | `python3 span.py <html>` | écart de cases de tous les doigtés des grilles jazz, et lesquelles sont déjà écrites |
| `couches.py` | `python3 couches.py <html> <id> basse,guitare,solo,phrase` | niveau de chaque couche, en total et en bande téléphone (`bandeTel`) |
| `lib.py` | importé par les générateurs | `midi()`, `low()`, `J()` (JSON compact), lignes de basse |
| `g1432.py`, `g1427.py` | exemples | générateur d'une grille de 16 mesures, et générateur qui allonge trois grilles d'un coup |

**Frottements acceptés**, à ne pas « corriger » :
- la 7e majeure contre la fondamentale (Si sur Do maj7) : c'est la couleur de l'accord ;
- la b9 d'un accord 7b9 ou altéré contre la basse, quand cette note est dans l'accord ;
- un frottement 9e / tierce mineure qui fait partie du doigté (Cm9) ;
- une blue note de passage.

---

## 7. Ce qui reste à faire

### 7.1 Grilles jazz pas encore écrites
D'après `span.py` en v1432, avec le tempo, le nombre d'accords et l'écart maximal :

| id | bpm | accords | écart |
|---|---|---|---|
| jz-ligne-qui-descend | 92 | 4 | 3 |
| jz-ligne-qui-monte | 88 | 4 | 3 |
| jz-carlton-broderie-aigues | 96 | 6 | 3 |
| jz-carlton-quartes-sans-fonda | 92 | 6 | 3 |
| jz-so-what | 136 | 8 | 1 |
| jz-constant-varie | 96 | 4 | 2 |
| jz-drop2-voiceleading | 100 | 3 | 3 |
| jz-cm-tour-riche | 92 | 6 | 3 |
| jz-descente-eclats | 92 | 4 | 3 |
| jz-mesure-impaire | 132 | 16 | 3 |
| jz-wes-quintes-fam | 120 | 16 | **4**, Fm7 4-6-6-8-6-x à refaire |
| jz-trois-paliers | 104 | 9 | 2 |
| jz-tonalites-manquantes | 96 | 8 | 2 |
| jz-diminue-quatre-sorties | 100 | 8 | 2 |
| jz-modulations-tierces-min | 126 | 9 | 2 |
| jz-modulations-tierces | 132 | 9 | 2 |
| jz-triades-superieures | 88 | 5 | 2 |
| jz-substitution-triton | 92 | 4 | 2 |
| jz-rhythm-changes-pont | 192 | 12 | 2 |
| jz-douze-visages | 120 | 36 | 3 |
| jz-echmel-melodique | 96 | 4 | 2 |
| jz-echmel-altere | 80 | 4 | 3 |
| jz-echhmaj-dorien-b5 | 92 | 4 | 3 |

Remarques :
- `jz-constant-varie` a les mêmes accords que la Constant structure lydienne ; on l'a sautée exprès.
- Les grilles rapides (So What à 136, rhythm changes pont à 192, modulations à 126–132) sont probablement à ralentir en ballade, au vu des goûts de Jérémy.
- Wes en quintes a un doigté de 4 cases d'écart, à remplacer avant tout.

### 7.2 Pistes ouvertes
- **Substitutions tritoniques** (« moyenne ») : à retravailler si Jérémy le demande, avec une vraie mélodie et une partie B, à un tempo plus lent.
- **Appliquer les leçons aux grilles écrites plus tôt :**
  - les allonger à 16 mesures avec une partie B ;
  - passer en ballade celles qui sont rapides (Bird blues à 148, Wes à 152, Hongrois à 144) ;
  - mettre une contrebasse audible.

  Le ii-V-I en v1432 est le modèle de ce qui plaît le plus.
- **Le Solo à +5 dB :** la question de le baisser partout reste ouverte, Jérémy n'a pas encore tranché.
- Le shuffle reste sur les grilles de la liste `SHUFFLE_ESSAI`. Penser à en sortir une grille si elle n'est pas blues.

---

## 8. Mémo pour démarrer la prochaine conversation

1. Cloner la branche `Guitar` : son `index.html` est la v1432 exacte.
2. Recopier `outils/*` dans `/tmp/t/` et `outils/verif.py` dans `/tmp/verif.py`. Installer Playwright si besoin.
3. Récupérer la version live de l'artifact avec `get_artifact` (elle doit être `1795627731-4bbb` ou plus récente) pour `base_version`.
4. Lire la section 3 avant de proposer quoi que ce soit.
5. Pour chaque grille : tableau, accord de Jérémy, générateur, vérifications, mesure de la basse, publication par `edit_version`.
