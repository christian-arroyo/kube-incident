# Project Description

KubeIncident is a Kubernetes-native incident detection and log-analysis platform that collects structured JSON logs from distributed workloads, identifies and correlates failure patterns, deduplicates alerts, and automatically creates evidence-backed incidents with severity and likely root cause. 

Built with FastAPI, Go, PostgreSQL, Redis, Prometheus, and Grafana, the platform runs on Kubernetes and includes a custom controller for monitoring and safe remediation. Infrastructure and delivery are automated using Terraform, Helm, GitHub Actions, and AWS EKS, demonstrating production-focused platform engineering, observability, asynchronous processing, and incident response.


## Objectives
- Design a small distributed system
- Write production-oriented Python services and learn Go for Kubernates-native software
- Containerize, deploy, configuure, secure, observe, scale, and troubleshoot workloads in K8s
- Collect operational telemetry and turn raw logs/metrics/events into useful incident evidence
- Use Terraform, Helm, and CI/CD to make infrastructure and deployment repeatable
- Intentionally create failures, investigate them systematically, recover the service, and write an RCA