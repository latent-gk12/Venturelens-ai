# VentureLens AI

**Evidence-Driven Evaluation. Fairer Decisions. Human-Led Selection.**

VentureLens AI is an AI-assisted hackathon project evaluation, research, and shortlisting platform. It helps organizers and judges evaluate project submissions using structured rubrics, external research, evidence-linked scoring, and transparent human review.

## Problem Statement

Hackathon organizers often evaluate many project presentations under time constraints. Inconsistent scoring, limited research time, and unclear evidence can make comparisons difficult.

VentureLens AI aims to make evaluation more structured, traceable, and consistent while keeping final decisions under human control.

## Key Features — Planned

- Event creation and participant registration through shareable event links.
- Configurable scoring rubrics with weights totaling 100%.
- PowerPoint submission processing and evidence extraction.
- External research with source references and uncertainty reporting.
- AI-assisted criterion-level scoring and explanations.
- Judge reviews, disagreement resolution, and documented overrides.
- Eligibility checks, audit trails, and controlled result publication.

*These features are planned; they are not yet implemented or verified.*

## Technology Stack

- **Frontend:** React and TypeScript
- **Backend:** Python and FastAPI
- **Database:** PostgreSQL
- **Object storage:** Amazon S3
- **Background processing:** Amazon SQS and Python workers
- **Authentication:** Amazon Cognito
- **AI inference:** Local Ollama with an open-weight model, subject to hardware compatibility
- **Deployment target:** AWS

Cloud services and external research providers will be selected and configured with cost controls. No paid AI inference fallback is planned by default.

## Architecture

The platform is designed around a frontend, backend API, PostgreSQL database, private object storage, and asynchronous evaluation workers.

Detailed architecture documentation will live in `docs/architecture/`.

## Project Structure

```text
frontend/       React application
backend/        FastAPI application, services, workers, and tests
evaluation/     Prompts, rubrics, and benchmark datasets
infrastructure/ Deployment and infrastructure configuration
docs/           Architecture, API, database, and decisions
scripts/        Development and maintenance scripts
```

## Local Development

Python 3.12 is the current backend development target.

The virtual environment is created locally in `.venv/`. Environment variables and secrets must not be committed to Git.

Setup and execution instructions will be documented as the backend foundation is implemented.

## Quality and Safety Principles

- AI scores are provisional; authorized humans make final decisions.
- Scores should be supported by identifiable evidence and explicit reasoning.
- Incomplete research must not be treated as negative evidence.
- Untrusted uploaded files and repositories must not be executed on the application server.
- Evaluation behavior must be tested against human-reviewed benchmark examples.
- Sensitive operations must be permission-checked and audited.

## Roadmap

1. Development environment and repository foundation.
2. Architecture documentation and database design.
3. Core event, registration, and submission workflows.
4. Evidence extraction, external research, and AI evaluation.
5. Judge review, disagreement resolution, and finalization.
6. Testing, security hardening, and cost-conscious deployment.

## Project Status

**Phase:** Foundation setup  
**Implementation status:** In progress

This repository is under active development. Planned features should not be interpreted as implemented functionality.

## License

License to be determined before public release.
