# Contributing

## Goal

Maintain a factual, readable professional portfolio that helps visitors understand the career profile, demonstrated skills, projects, personal contribution, and evidence behind claims. This repository is the portfolio website, not a general career-management application or a home for unrelated project code.

## Required workflow

1. Create a short-lived branch from `main`.
2. Make one coherent change with a clear purpose.
3. Open a pull request to `main`; do not commit changes directly to `main`.
4. Explain the motivation, scope, and validation in the PR description.
5. Wait for the site-render check to pass and review the rendered result.
6. Merge only after the change is ready.

## Content standards

- Do not invent employers, titles, dates, metrics, results, or skill levels.
- Distinguish professional experience, personal projects, experiments, and topics being studied.
- For each project, state the problem, goal, personal contribution, method, evidence/results, and limitations.
- Link a project only to a dedicated repository that is ready for public inspection.
- Do not publish confidential, personal, or otherwise non-public information.
- Prefer concise, concrete statements over generic claims and keyword lists.

## Local validation

Install [Quarto](https://quarto.org/) and run:

```bash
quarto render site
```

Review the generated `site/_site` output before merging content or navigation changes.
