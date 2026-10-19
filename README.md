# Career Knowledge Portfolio

An open-source demonstration of an evidence-first, privacy-aware system for career research and technical skill development.

**Public / synthetic-only.** This repository contains reusable engineering, examples, evaluation methodology, and documentation. It must never contain personal career records, CVs, recruiter messages, private job applications, or private learning diagnostics.

## Engineering goals

- Convert job descriptions into structured, source-backed records.
- Make skill-gap and opportunity prioritisation explainable.
- Keep unknowns explicit and separate facts from inferences.
- Evaluate extraction and scoring quality on synthetic, labelled examples.
- Demonstrate typed Python, tests, reproducibility, and maintainable design.

## Current contents

- Pydantic domain models for opportunities, requirements, evidence, and skill assessments.
- Deterministic weighted scoring with a separate evidence-coverage value.
- Unit tests and GitHub Actions CI (pytest, Ruff, mypy).
- Synthetic example records under `examples/`.
- Quarto site under `site/`, with a GitHub Pages deployment workflow.
- Architecture, privacy policy, evaluation plan, and staged roadmap under `docs/`.

## Run locally

Requires Python 3.11+ and Quarto only if rendering the site.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest
ruff check src tests
mypy
python -c 'import json; print(json.load(open("examples/score-input.json")))'
```

To render the site: `quarto render site`. To enable publishing, open **Settings → Pages** and select **GitHub Actions** as the build and deployment source. The workflow publishes changes under `site/` on `main`.

## Scoring contract

Scores are prioritisation aids, not estimates of hiring probability. Dimensions use a 0–4 scale and documented weights. Unknown dimensions are excluded from the score denominator but reduce evidence coverage; an all-unknown record has no score. Hard constraints are reviewed separately.

## Next milestone

Create and label a synthetic benchmark, freeze a held-out split, then report field-level extraction metrics, provenance coverage, unsupported-guess rate, ranking stability, sample sizes, and failure analysis. No performance claim is made before that evaluation exists.
