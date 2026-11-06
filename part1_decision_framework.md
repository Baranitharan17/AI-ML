Part 1: Decision framework for 5 problems
Input type → Output type Constraints Recommended tool
1. GST calculation on invoices Invoice amount, GST rate, item details → GST amount, total invoice value High accuracy, low latency, explainable calculations Python calculation logic or a rules-based system
2. Current leave balance of an employee Employee ID, leave records, approved leave requests → Available leave balance Must be current, secure, fast, auditable HRMS/database query with business rules
3. Ranking resumes for a role Resume text, job description, required skills → Ranked candidate list with matching reasons Fairness, explainability, privacy, reasonable processing time NLP/ML ranking system with human review
4. Answering questions from a 60-page contract Contract PDF + user question → Answer with page references and supporting quotations Grounded answers, low hallucination, document privacy, traceability RAG (Retrieval-Augmented Generation) + LLM
5. Forecasting next month's sales Historical sales, dates, product/seasonality data → Next-month sales forecast Forecast accuracy, data quality, cost, explainability Time-series forecasting model, with a baseline comparison

Human review and AI restrictions
Problem Human must review? Where AI should not be used
GST calculation Yes, for exceptions, disputed invoices, and tax-rule changes Don't let an LLM independently determine or approve tax liability
Leave balance Yes, for disputes, policy exceptions, and corrections Don't let AI invent balances or access employee records without authorization
Resume ranking Yes, before shortlisting or rejecting candidates Don't use AI as the sole decision-maker or rank based on protected characteristics
Contract Q&A Yes, for legal interpretation, ambiguous clauses, and high-impact decisions Don't treat generated answers as final legal advice or accept unsupported answers
Sales forecasting Yes, before major purchasing, staffing, or financial commitments Don't rely on a forecast alone for high-impact business decisions