# Week 3 - Day 3: ML/AI Fundamentals + Decision Framework

## Task 1: Decision Template Practice

**Goal:** Choose the appropriate tool for each problem and explain why.

| Problem | Input | Output | Constraints | Recommended tool | Why |
|---|---|---|---|---|---|
| Leave balance lookup | Employee ID | Available leave balance | Accurate, low latency, current data | SQL | Retrieves the exact value from the employee database. |
| Invoice tax calculation | Invoice amount, applicable tax rate | Tax amount and total invoice amount | High accuracy, explainability, auditable rules | Python function + verified tax rules | A deterministic formula is reliable and easy to test. |
| Resume screening | Resume and job description | Job-related match indicators or a ranked shortlist for review | Fairness, explainability, privacy, human oversight | Rules + ML (decision support only) | Rules check required criteria; ML can help compare job-related patterns. A human makes the hiring decision. |
| HR policy Q&A | Employee question and approved HR policy documents | Answer with supporting source | Accuracy, explainability, up-to-date documents | RAG + LLM | Retrieves relevant policy passages and uses them to draft a grounded answer. |
| Predicting attrition | Historical employee data | Attrition-risk estimate | Privacy, fairness, explainability, careful use | ML | Learns patterns from historical data; the estimate should not be treated as certainty or used alone for employment decisions. |
| Auto-reply to emails | Incoming email and relevant context | Suggested reply | Cost, latency, tone, privacy, accuracy | LLM + rules | An LLM can draft a contextual reply; rules and review help prevent unsafe or incorrect messages. |
| Monthly payroll run | Employee records, attendance, salary, deductions, approved tax/rule data | Payroll calculations and payslips | Very high accuracy, security, auditability | SQL + Python functions + rules | SQL retrieves verified records; deterministic code applies payroll calculations and rules. Review before final release. |
| Onboarding across 4 systems | New-hire details and task status | Updated records, access requests, onboarding status | Security, reliability, permissions, audit trail | Workflow/orchestrator; agent only where useful | Coordinates steps across systems. Require approval for sensitive access or irreversible actions. |

## Human approval

- Resume screening: Yes — a human should make the final hiring decision.
- Attrition prediction: Yes — do not make employment decisions from a model score alone.
- Auto-reply to emails: Yes for sensitive, external, or high-impact emails; routine replies may be sent automatically only under approved rules.
- Monthly payroll run: Yes — review and approve before final payroll release.
- Onboarding across 4 systems: Yes for sensitive access permissions or irreversible changes.
- Leave balance lookup: Usually no for simply displaying the recorded balance; follow the organisation's access controls.
- Invoice tax calculation: Review exceptions and changes to tax rules; normal calculations should be tested and auditable.
- HR policy Q&A: Escalate uncertain or high-impact questions to HR.

## Two examples often wrongly solved with an LLM

1. **Invoice tax calculation:** An LLM may produce inconsistent arithmetic. Use tested Python calculations and verified tax rules instead.
2. **Leave balance lookup:** An LLM should not guess an employee's current balance. Query the authoritative database with SQL.

## Key mapping to remember

- Calculation → Python function
- Exact lookup → SQL
- Fixed rule → `if/else`
- Prediction from history → ML
- Answer from documents → RAG + LLM
- Multi-step process → Agent/workflow

## Trade-offs

Choose tools based on accuracy, latency, cost, explainability, privacy, and the consequences of an error. Use the simplest reliable solution, and include human approval where decisions are sensitive or high impact.
