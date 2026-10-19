# Architecture

## Pipeline

1. **Capture** source text and URL, timestamp, and retrieval context.
2. **Extract** a draft record. Any LLM is an optional adapter, never the authority.
3. **Validate** types, required fields, URL shape, and lifecycle invariants.
4. **Review** evidence for consequential claims; keep unsupported fields unknown.
5. **Score** only reviewed dimensions, with visible weights and coverage.
6. **Report** the shortlist with citations, uncertainty, and source freshness.

## Boundaries

- Domain models do not perform network calls.
- Parsing does not silently make business decisions.
- Scoring is deterministic and explainable.
- External model calls are optional and must be separately tested.
- The public demo uses synthetic examples only.

## Why not a vector database yet?

The initial dataset is small and relational: filtering by company, role, date, and workflow status is more valuable than approximate semantic retrieval. Add embeddings only after a measured retrieval benchmark demonstrates a material improvement.
