"""Transparent prioritisation scores; never a probability of being hired."""

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True, slots=True)
class ScoreDimension:
    value: int | None
    weight: float
    rationale: str

    def __post_init__(self) -> None:
        if self.value is not None and not 0 <= self.value <= 4:
            raise ValueError("Dimension value must be between 0 and 4, or None when unknown")
        if self.weight < 0:
            raise ValueError("Weight cannot be negative")


@dataclass(frozen=True, slots=True)
class ScoreResult:
    score: float | None
    coverage: float
    assessed_dimensions: int
    total_dimensions: int


def score_opportunity(dimensions: Mapping[str, ScoreDimension]) -> ScoreResult:
    """Return a 0–100 weighted score and weight coverage for assessed dimensions.

    Unknown dimensions are excluded from the score denominator, but their weights reduce
    coverage. An empty/all-unknown set yields score=None rather than a misleading zero.
    """
    if not dimensions:
        return ScoreResult(None, 0.0, 0, 0)
    total_weight = sum(d.weight for d in dimensions.values())
    assessed = {name: dim for name, dim in dimensions.items() if dim.value is not None}
    assessed_weight = sum(d.weight for d in assessed.values())
    coverage = assessed_weight / total_weight if total_weight > 0 else 0.0
    if assessed_weight == 0:
        return ScoreResult(None, coverage, 0, len(dimensions))
    score = sum((dim.value or 0) / 4 * dim.weight for dim in assessed.values()) / assessed_weight * 100
    return ScoreResult(round(score, 2), round(coverage, 4), len(assessed), len(dimensions))
