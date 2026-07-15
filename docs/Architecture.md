# MOLTA - System Architecture

## Overview

MOLTA follows a simple client-server architecture designed for the OpenAI Build Week MVP.

The frontend is built with React and communicates with a FastAPI backend through REST APIs. The backend is responsible for processing repository data, interacting with GPT-5.6 for AI-assisted analysis, and managing project information.

This architecture is modular, easy to understand, and can be expanded as the project grows.

---

# System Components

## 1. Frontend

**Technology**

- React
- TypeScript
- Tailwind CSS

**Responsibilities**

- Allow users to enter a GitHub repository
- Display repository analysis
- Show the modernization report
- Present the project dashboard

> User authentication is planned for a future version.

---

## 2. Backend

**Technology**

- Python
- FastAPI

**Responsibilities**

- Receive API requests
- Validate repository information
- Coordinate the analysis process
- Connect with AI services
- Return results to the frontend

---

## 3. AI Analysis Engine

**Technology**

- OpenAI GPT-5.6

**Responsibilities**

- Understand legacy code
- Explain important files and modules
- Identify technical debt
- Generate modernization recommendations

---

## 4. Repository Analyzer

**Responsibilities**

- Read the repository structure
- Detect programming languages
- Identify frameworks
- Collect basic project information

---

## 5. Security Analysis

**Responsibilities**

- Highlight possible security issues
- Detect outdated dependencies
- Suggest security improvements

---

## 6. Performance Analysis

**Responsibilities**

- Identify possible performance bottlenecks
- Suggest optimization opportunities
- Improve maintainability

---

## 7. Database

**Technology**

- SQLite

**Responsibilities**

- Store project information
- Save analysis history
- Store generated reports

---

# Planned System Workflow

1. The user provides a GitHub repository.
2. The frontend sends the request to the FastAPI backend.
3. The backend prepares the repository for analysis.
4. The Repository Analyzer collects project information.
5. GPT-5.6 generates AI-assisted insights.
6. Security and Performance Analysis modules add additional recommendations.
7. Results are stored in SQLite.
8. The frontend displays the complete report.

> This workflow represents the planned MVP architecture and will be implemented during OpenAI Build Week.

---

# Architecture Goals

The architecture is designed to be:

- Simple
- Modular
- Easy to maintain
- Easy to extend
- Suitable for AI-powered analysis

---

# Technology Stack

| Component | Technology |
|----------|------------|
| Frontend | React + TypeScript + Tailwind CSS |
| Backend | FastAPI + Python |
| AI | GPT-5.6 |
| Database | SQLite |
| Version Control | Git + GitHub |
| Development Tools | VS Code, Codex, GitHub Copilot, Postman |

---

# Future Improvements

As MOLTA continues to grow, future versions may include:

- Multi-agent collaboration
- Automatic pull request generation
- CI/CD integration
- Jira integration
- Slack integration
- PostgreSQL
- Docker
- Redis
- Kubernetes
- Cloud deployment (AWS or Azure)