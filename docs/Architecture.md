# MOLTA Architecture

## Overview

MOLTA follows a simple client-server architecture.

The user interacts with a web application built using React. The frontend communicates with a FastAPI backend through REST APIs. The backend analyzes repositories, interacts with OpenAI GPT-5.6 for AI-powered insights, and stores project information in a SQLite database.

This architecture keeps the system modular, scalable, and easy to maintain.

---

# System Components

## 1. Frontend

Technology:
- React
- TypeScript
- Tailwind CSS

Responsibilities:
- User authentication (future)
- Repository upload
- Display analysis results
- Show modernization report
- Display project dashboard

---

## 2. Backend

Technology:
- FastAPI
- Python

Responsibilities:
- Receive repository information
- Process uploaded repositories
- Manage API requests
- Connect with AI services
- Generate analysis results

---

## 3. AI Analysis Engine

Technology:
- OpenAI GPT-5.6 API

Responsibilities:
- Understand legacy code
- Detect technical debt
- Explain code structure
- Suggest modernization strategies
- Generate documentation

---

## 4. Repository Analyzer

Responsibilities:
- Read project files
- Detect programming languages
- Analyze folder structure
- Identify important components
- Collect project statistics

---

## 5. Security Analysis Module

Responsibilities:
- Detect common security risks
- Identify outdated dependencies
- Report potential vulnerabilities
- Suggest security improvements

---

## 6. Performance Analysis Module

Responsibilities:
- Identify inefficient code
- Detect unnecessary complexity
- Recommend optimization opportunities
- Improve maintainability

---

## 7. Database

Technology:
- SQLite

Responsibilities:
- Store project information
- Save analysis history
- Store generated reports
- Manage application data

---

# System Workflow

Step 1
User uploads a GitHub repository.

↓

Step 2
Frontend sends the request to the FastAPI backend.

↓

Step 3
Backend downloads and analyzes the repository.

↓

Step 4
Repository Analyzer scans the project structure.

↓

Step 5
AI Analysis Engine generates insights using GPT-5.6.

↓

Step 6
Security and Performance modules perform additional analysis.

↓

Step 7
Results are stored in the SQLite database.

↓

Step 8
Frontend displays the complete modernization report.

---

# Architecture Goals

The architecture is designed to be:

- Modular
- Scalable
- Maintainable
- Easy to extend
- AI-first
- Suitable for future enterprise deployment

---

# Future Expansion

The architecture can later support:

- Multi-agent collaboration
- Pull request generation
- CI/CD integration
- Jira integration
- Slack integration
- Cloud deployment
- Team collaboration