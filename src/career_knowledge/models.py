"""Typed domain models; no network access or hidden inference."""

from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class WorkMode(StrEnum):
    ONSITE = "onsite"
    HYBRID = "hybrid"
    REMOTE = "remote"
    UNKNOWN = "unknown"


class OpportunityStatus(StrEnum):
    CAPTURED = "captured"
    REVIEWED = "reviewed"
    SHORTLISTED = "shortlisted"
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"
    CLOSED = "closed"


class Evidence(StrictModel):
    claim: str = Field(min_length=1)
    source: HttpUrl
    quote: str | None = None
    captured_at: date | None = None


class Requirement(StrictModel):
    requirement: str = Field(min_length=1)
    importance: str = Field(pattern="^(must_have|important|nice_to_have|unknown)$")
    evidence: str | None = None


class Opportunity(StrictModel):
    opportunity_id: str = Field(min_length=1)
    company: str = Field(min_length=1)
    role_title: str = Field(min_length=1)
    source_url: HttpUrl
    created_at: date
    status: OpportunityStatus = OpportunityStatus.CAPTURED
    location: str | None = None
    work_mode: WorkMode = WorkMode.UNKNOWN
    deadline: date | None = None
    evidence: list[Evidence] = Field(default_factory=list)
    requirements: list[Requirement] = Field(default_factory=list)
    notes: str = ""


class SkillAssessment(StrictModel):
    skill: str = Field(min_length=1)
    level: str = Field(pattern="^(not_assessed|beginner|developing|intermediate|advanced|expert)$")
    confidence: str = Field(pattern="^(low|medium|high)$")
    evidence: list[str] = Field(default_factory=list)
    assessed_at: date
    next_action: str | None = None
