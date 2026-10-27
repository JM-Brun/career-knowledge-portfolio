# Contributing

## Purpose and boundary

Maintain a factual, readable public professional portfolio that helps visitors understand the career profile, demonstrated skills, selected projects, personal contribution, and evidence behind claims. This repository is the public narrative and navigation layer, not a general career-management system, a technical wiki, or the home of application code.

## Contribution modes

Choose the mode that matches the change and identify it in the PR.

1. **Profile and positioning** — revise the summary, research interests, or technical focus. Claims must match the evidence and avoid implying specialization, seniority, or mastery that has not been demonstrated.
2. **Professional experience and chronology** — add or correct roles, dates, responsibilities, or technologies. Use verified facts; distinguish employment, research, personal projects, and learning.
3. **Skills and evidence** — add or revise a skill only when a public artifact demonstrates it. Link to relevant code, tests, reports, publications, or reproducible results; documentation alone is not proof of practical mastery.
4. **Project case study** — summarize a project's problem, motivation, personal contribution, method, results/evidence, and limitations. Keep implementation details in the project's own repository and select only a small number of defensible claims.
5. **Research, publication, and source correction** — add or correct bibliographic records, research outputs, or attribution. Verify metadata against primary sources and state uncertain status explicitly.
6. **Website structure, accessibility, and presentation** — improve navigation, responsive layout, semantics, readability, bilingual content where present, or rendering. Preserve factual content and inspect the rendered site, not just source Markdown/Quarto.
7. **Links and publication review** — add or repair links to public artifacts, check that they are accessible to an unauthenticated visitor, and remove broken, private, or confidential-source dependencies.

## Required workflow

1. Create a short-lived branch from `main`.
2. Make one coherent change with a clear purpose.
3. Open a pull request to `main`; do not commit changes directly to `main`.
4. State the contribution mode, source/evidence, scope, and validation in the PR description.
5. Wait for the site-render check to pass and review the rendered result.
6. Merge only after the change is ready.

## Content standards

- Do not invent employers, titles, dates, metrics, results, publications, or skill levels.
- Distinguish professional experience, personal projects, experiments, and topics being studied.
- For each project, state the problem, goal, personal contribution, method, evidence/results, and limitations.
- Link a project only to a dedicated repository or artifact ready for public inspection.
- Do not publish confidential, personal, or otherwise non-public information.
- Never link public readers to private records or require access to private sources to verify a public claim.
- Prefer concise, concrete statements over generic claims and keyword lists.
- Do not imply that a passing CI, a planned roadmap item, or a written explanation proves scientific validity or personal mastery.

## Local validation

Install [Quarto](https://quarto.org/) and run:

```bash
quarto render site
```

Review the generated `site/_site` output before merging content or navigation changes. Check links, keyboard/readability basics, and the relevant page at narrow and wide widths when layout changes.
