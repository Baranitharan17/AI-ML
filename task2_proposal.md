Technical Proposal: Auto-Categorise Support Tickets

1. Problem

Support teams receive many tickets related to issues such as login problems, password resets, leave policies, payment failures, and technical errors. Manually categorising these tickets takes time, delays responses, and can lead to inconsistent classification. The goal is to automatically assign each incoming ticket to the correct category and reduce manual effort.

2. Recommended Approach

Compare three approaches:

- Keyword-based rules: Uses predefined keywords and conditions to assign categories. It is simple and fast to build but struggles with spelling mistakes, synonyms, and complex sentences.
- ML classifier: Trains a model using previously categorised support tickets. It can learn patterns from historical data, provides consistent predictions, and is cost-effective for repeated predictions. However, it requires labelled training data.
- LLM-based classification: Uses a Large Language Model to classify tickets based on instructions. It handles varied language well but may have higher API costs, latency, and privacy concerns.

Recommendation: Start with an ML classifier such as TF-IDF with Logistic Regression. It is a practical, explainable, and cost-effective baseline for a support-ticket system. Use keyword rules for obvious cases and send low-confidence predictions for human review. Consider an LLM if labelled data is insufficient or ticket language is highly varied.

3. Data Requirements

The client must provide:

- Historical support tickets containing ticket descriptions and their correct categories.
- Ideally, 1,000–5,000 or more labelled tickets covering all major categories.
- A list of approved categories, such as Login, HR/Leave, Payments, Technical Issues, and General Queries.
- Examples of ambiguous tickets and the preferred category for each.
- Permission to use the data, with personal and sensitive information removed where possible.

4. Evaluation Metric

Evaluate the model on a separate, unseen test dataset.

- Primary metric: Macro F1-score, with a target of at least 0.85 (85%).
- Secondary metric: Overall accuracy target of at least 85%.
- Per-category metric: Aim for F1-score of at least 0.80 for each major category.

Macro F1 is important because it gives equal importance to each category, including categories with fewer tickets. Review a confusion matrix to identify categories that are frequently misclassified. These targets are initial goals and must be validated against the client's actual data.

5. Estimated Build Time

Estimated duration: 8–10 working days.

- Days 1–2: Understand requirements, categories, and data quality.
- Days 3–4: Clean data and prepare training and test datasets.
- Days 5–6: Build a baseline model and train the classifier.
- Days 7–8: Evaluate performance, tune the model, and review errors.
- Days 9–10: Integrate a prototype, test it with sample tickets, and document results.

This estimate assumes the client provides usable labelled data and timely feedback. Production deployment, security reviews, and integration with complex ticketing systems may require additional time.

6. Key Trade-offs

The ML classifier offers a balance between accuracy, speed, cost, and maintainability. Keyword rules are easier to explain but less flexible. LLMs can understand complex wording but may introduce recurring costs, unpredictable outputs, and data privacy risks. The proposed solution prioritises an affordable ML baseline with human review for uncertain predictions. Performance should be monitored after deployment, and the model should be retrained when categories or ticket patterns change.