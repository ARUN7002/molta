from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import re

from github_utils import get_repository_metadata, get_repository_contents


class RepositoryRequest(BaseModel):
    repository: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to MOLTA API"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }


@app.post("/analyze")
def analyze(data: RepositoryRequest):

    repo = data.repository.strip()

    github_pattern = r"^https://github\.com/[\w.-]+/[\w.-]+/?$"

    if not re.match(github_pattern, repo):
        return {
            "success": False,
            "message": "Invalid GitHub repository URL."
        }

    # Remove trailing slash
    repo = repo.rstrip("/")

    # Convert GitHub URL into GitHub API URL
    api_url = repo.replace(
        "https://github.com/",
        "https://api.github.com/repos/"
    )

    # -----------------------------
    # Repository Metadata
    # -----------------------------
    repo_data = get_repository_metadata(api_url)

    if repo_data is None:
        return {
            "success": False,
            "message": "Repository not found."
        }

    # -----------------------------
    # Repository Contents
    # -----------------------------
    contents = get_repository_contents(api_url)

    project_structure = []
    frameworks = []

    if contents:

        # Build project structure
        for item in contents:
            if item["type"] == "dir":
                project_structure.append(f'{item["name"]}/')
            else:
                project_structure.append(item["name"])

        # Detect technologies from filenames
        filenames = [item["name"] for item in contents]

        if "package.json" in filenames:
            frameworks.append("Node.js")

        if "vite.config.ts" in filenames or "vite.config.js" in filenames:
            frameworks.append("Vite")

        if "requirements.txt" in filenames:
            frameworks.append("Python")

        if "Dockerfile" in filenames:
            frameworks.append("Docker")

        if "docker-compose.yml" in filenames:
            frameworks.append("Docker Compose")

        if "README.md" in filenames:
            frameworks.append("README Available")

        if "pom.xml" in filenames:
            frameworks.append("Maven / Spring Boot")

        if "Cargo.toml" in filenames:
            frameworks.append("Rust")

        if "build.gradle" in filenames:
            frameworks.append("Gradle")

        if "composer.json" in filenames:
            frameworks.append("Laravel / PHP")

    # -----------------------------
    # Return Result
    # -----------------------------
    return {
        "success": True,
        "message": "Repository found!",
        "name": repo_data["name"],
        "owner": repo_data["owner"]["login"],
        "stars": repo_data["stargazers_count"],
        "language": repo_data["language"],
        "project_structure": project_structure,
        "frameworks": frameworks
    }