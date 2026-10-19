from datetime import date

import pytest
from pydantic import ValidationError

from career_knowledge.models import Evidence, Opportunity, OpportunityStatus, WorkMode


def test_opportunity_defaults_to_captured_and_unknown_work_mode() -> None:
    opportunity = Opportunity(
        opportunity_id="synthetic-001",
        company="Example Analytics (synthetic)",
        role_title="Machine Learning Engineer",
        source_url="https://example.com/jobs/ml-engineer",
        created_at=date(2026, 1, 2),
    )
    assert opportunity.status is OpportunityStatus.CAPTURED
    assert opportunity.work_mode is WorkMode.UNKNOWN
    assert opportunity.requirements == []


def test_extra_fields_are_rejected() -> None:
    with pytest.raises(ValidationError):
        Opportunity.model_validate({
            "opportunity_id": "synthetic-002", "company": "Example",
            "role_title": "DS", "source_url": "https://example.com/job",
            "created_at": "2026-01-02", "hiring_probability": 0.8,
        })


def test_evidence_requires_a_source_url() -> None:
    with pytest.raises(ValidationError):
        Evidence(claim="Remote role", source="not-a-url")
