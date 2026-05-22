# AutoPilot-SRE

An agentic Site Reliability Engineering platform that autonomously monitors, detects, and remediates incidents across a microservices environment.

## What This Project Does

- Monitors three microservices using Prometheus and Grafana
- Injects failures to simulate real incidents
- Uses an AI agent to detect anomalies, diagnose root causes, and execute remediation runbooks
- Generates postmortem reports after each incident

## Tech Stack

- Docker and Docker Compose
- Python and Flask
- Prometheus and Grafana
- Terraform
- Claude AI (Anthropic) for agentic tool use

## Project Phases

| Phase | Focus | Status |
|-------|-------|--------|
| 1 | Containers and Microservices | Done |
| 2 | Observability with Prometheus and Grafana | Done |
| 3 | Chaos Engineering | Upcoming |
| 4 | AI Agent | Upcoming |
| 5 | Terraform and IaC | Upcoming |

## Blog Series

Follow the full build on Medium:

- Day 1 — Understanding Docker: https://medium.com/@fehzanvayani/understanding-docker-3830d7e13fcd
- Day 2 — Docker Compose: https://medium.com/@fehzanvayani/docker-compose-e6fcaa1e5825
- Day 3 — Prometheus for Observability: https://medium.com/@fehzanvayani/prometheus-for-observability-e1db1260f811

## Author

[Fehzz](https://github.com/Fehzz)
