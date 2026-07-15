# MOLTA

> An AI-powered platform that helps developers understand, analyze, and modernize legacy software systems.

---

## Project Overview

MOLTA is a project built for OpenAI Build Week 2026. The goal is to make working with legacy software easier by helping developers understand old codebases, identify technical debt, detect possible security and performance issues, and generate a clear modernization plan with the help of GPT-5.6.

**Current Status:** 🚧 MVP under development.

---

## Problem Statement

Many companies still use legacy software that has grown over many years. Understanding these codebases takes a lot of time because documentation is often outdated or missing. Developers usually spend days exploring the project before they can confidently make changes.

---

## Solution

MOLTA is being built to reduce that effort. Instead of manually exploring an entire codebase, developers can upload a repository and receive an AI-assisted analysis with useful insights, potential issues, and practical recommendations for modernization. The goal is to support developers in making better decisions, not replace them.

---

## Current MVP Features

- Upload a GitHub repository
- Analyze the repository structure
- Detect legacy code and technical debt
- Highlight possible security concerns
- Identify performance improvement opportunities
- Generate an AI-assisted modernization plan

> **Note:** These features are part of the current MVP and are being developed during OpenAI Build Week 2026.

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | React + TypeScript |
| Backend | FastAPI |
| AI | GPT-5.6 |
| AI Coding Assistant | Codex |
| Database | SQLite |
| Version Control | Git & GitHub |

---

## Project Structure

```text
MOLTA/
├── frontend/
├── backend/
├── docs/
├── assets/
├── demo/
├── scripts/
├── tests/
├── README.md
└── LICENSE
```