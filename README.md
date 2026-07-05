# Policy Analysis Agent

[![CI](https://github.com/kogunlowo123/policy-analysis-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/policy-analysis-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Legal | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Policy analysis agent that reviews corporate policies for legal compliance, identifies policy gaps, compares against industry standards, recommends updates, and tracks policy lifecycle.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `review_policy` | Review a corporate policy for legal compliance and completeness |
| `identify_gaps` | Identify gaps between current policies and legal requirements |
| `benchmark_industry` | Compare policies against industry standards and best practices |
| `recommend_updates` | Generate recommended policy updates with rationale |
| `track_lifecycle` | Track policy lifecycle (draft, review, approved, retired) |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/policy-analysis/analyze` | Analyze |
| `POST` | `/api/v1/policy-analysis/search` | Search |
| `POST` | `/api/v1/policy-analysis/generate` | Generate document |
| `GET` | `/api/v1/policy-analysis/track` | Track status |
| `POST` | `/api/v1/policy-analysis/report` | Generate report |

## Features

- Policy
- Analysis
- Compliance
- Audit Trail

## Integrations

- Relativity
- Logikcull
- Ironclad
- Docusign Clm
- Westlaw

## Architecture

```
policy-analysis-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── policy_analysis_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Legal Tech Platform + LLM + Document Management**

---

Built as part of the Enterprise AI Agent Platform.
