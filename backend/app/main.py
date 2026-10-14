
from fastapi import FastAPI

app = FastAPI(
    title="VentureLens AI API",
    description=(
        "AI-powered hackathon project evaluation, "
        "research, and shortlisting platform."
    ),
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Return the basic API health status."""
    return {"status": "healthy"}
