from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import re
import requests
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
    response = requests.get(api_url)

    if response.status_code != 200:
        return {
            "success": False,
            "message": "Repository not found."
        }

    repo_data = response.json()

    # -----------------------------
    # Repository Contents
    # -----------------------------
    contents_url = api_url + "/contents"

    contents_response = requests.get(contents_url)

    project_structure = []

    if contents_response.status_code == 200:

        contents = contents_response.json()

        for item in contents:

            if item["type"] == "dir":
                project_structure.append(item["name"] + "/")
            else:
                project_structure.append(item["name"])

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
        "project_structure": project_structure
    }