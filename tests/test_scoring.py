import pytest

from career_knowledge.scoring import ScoreDimension, score_opportunity


def test_weighted_score_and_coverage_are_separate() -> None:
    result = score_opportunity({
        "technical": ScoreDimension(4, 0.7, "Strong demonstrated match"),
        "location": ScoreDimension(2, 0.3, "Partial match"),
    })
    assert result.score == 85.0
    assert result.coverage == 1.0


def test_unknown_dimensions_reduce_coverage_not_score_denominator() -> None:
    result = score_opportunity({
        "technical": ScoreDimension(4, 0.5, "Evidence reviewed"),
        "salary": ScoreDimension(None, 0.5, "Not disclosed"),
    })
    assert result.score == 100.0
    assert result.coverage == 0.5


def test_all_unknown_returns_no_score() -> None:
    result = score_opportunity({"unknown": ScoreDimension(None, 1.0, "Not assessed")})
    assert result.score is None
    assert result.coverage == 0.0


def test_invalid_dimension_is_rejected() -> None:
    with pytest.raises(ValueError):
        ScoreDimension(5, 1.0, "out of range")
