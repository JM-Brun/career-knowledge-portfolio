# Portfolio professionnel — JM-Brun

Ce dépôt héberge mon **portfolio professionnel personnel** : parcours, expériences, compétences techniques, connaissances et projets sélectionnés.

Il ne s'agit pas d'un produit logiciel autonome. Chaque projet technique conséquent doit disposer de son propre dépôt, avec son code, ses tests, sa documentation et ses décisions d'architecture. Ce portfolio en donne la synthèse et explique le rôle que j'y ai joué.

## Contenu du site

- **Profil** — positionnement professionnel et domaines d'intérêt.
- **Parcours** — expériences et contributions, avec dates et périmètres vérifiés.
- **Compétences** — technologies et méthodes, avec un niveau de maîtrise étayé.
- **Projets** — problèmes traités, rôle personnel, approche, résultats et liens vers les dépôts dédiés.
- **Connaissances** — sujets techniques étudiés et approfondis.

## Principes éditoriaux

- Ne pas inventer de poste, d'employeur, de date, de résultat ou de niveau de maîtrise.
- Distinguer expérience professionnelle, projet personnel, expérimentation et apprentissage.
- Décrire précisément ma contribution personnelle à chaque réalisation.
- Relier les affirmations importantes à des livrables, dépôts, démonstrations ou éléments vérifiables lorsque c'est possible.
- Ne publier aucune information confidentielle provenant d'un employeur, d'un client ou d'un projet privé.

## Site

Le site est construit avec [Quarto](https://quarto.org/) et publié sur GitHub Pages via GitHub Actions. Les pages sont dans `site/`.

Pour prévisualiser localement :

```bash
quarto render site
```

Pour activer la publication, ouvrir **Settings → Pages** dans ce dépôt et choisir **GitHub Actions** comme source de déploiement.

## Structure des dépôts

- Ce dépôt : portfolio, récit professionnel et liens vers les réalisations.
- Dépôts de projets : code, données partageables, tests, documentation et démonstrations propres à chaque projet.
- Dépôt privé `career-knowledge` : notes personnelles de carrière et de progression, jamais copiées automatiquement dans ce dépôt public.
