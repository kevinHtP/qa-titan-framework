# 🛡️ The Titan Framework: Enterprise QA & DevSecOps Automation

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-E2E_Testing-2EAD33.svg)
![Pytest-BDD](https://img.shields.io/badge/Pytest_BDD-Behavior_Driven-yellow.svg)
![Security](https://img.shields.io/badge/Security-OWASP_DAST-red.svg)
![AI](https://img.shields.io/badge/AI_Integration-Google_Gemini-8A2BE2.svg)

## 📌 Project Overview
**The Titan Framework** is an advanced, enterprise-grade Automated Testing and Security (DevSecOps) framework. It bridges the gap between traditional QA and Cybersecurity by combining E2E UI testing with automated vulnerability exploitation. 

This framework is built to test complex systems (demonstrated on the OWASP Juice Shop architecture) while generating AI-powered failure analysis to accelerate debugging.

## 🚀 Key Features & Innovations
- **Behavior-Driven Development (BDD):** Test scenarios written in Gherkin syntax (Indonesian/English) bridging the gap between technical and business stakeholders.
- **Automated DAST (Dynamic Application Security Testing):** Playwright scripts engineered to act as automated threat actors, validating system resilience against critical vulnerabilities like **SQL Injection (SQLi)**.
- **Smart AI Bug Analyzer:** Integrated with **Google Gemini API** to automatically intercept Pytest failures, analyze stack traces, and provide human-readable Root Cause Analysis (RCA).
- **Container-Ready Environment:** Fully compatible with Docker for local isolated execution, bypassing unstable public staging environments.
- **Enterprise Security Standards:** Strict credential management using `.env` environment variables, ensuring zero credential leakage on public repositories.

## 🛠️ Technology Stack
- **Language:** Python
- **E2E Automation:** Playwright
- **Test Runner & BDD:** Pytest, Pytest-BDD
- **AI Integration:** Google GenAI SDK (Gemini)
- **Infrastructure:** Docker, GitHub Actions (CI/CD)

## ⚙️ How to Run Locally

### 1. Start the Target Environment (Docker)
We use a local instance of OWASP Juice Shop to avoid disrupting public servers.
```bash
docker run --rm -p 3000:3000 bkimminich/juice-shop