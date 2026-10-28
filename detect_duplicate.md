Technical Proposal: Detect Duplicate Customer Records
1. Problem
Businesses may store the same customer multiple times because of spelling differences, outdated contact details, or data entry errors. Duplicate records can cause inaccurate reports, repeated communications, and fragmented customer histories. The goal is to identify likely duplicate customer records and help the business consolidate them without accidentally merging different customers.

2. Recommended Approach
Compare three approaches:

Exact SQL matching: Matches identical values such as email addresses or phone numbers. It is fast, simple, and precise, but misses differences in spelling, formatting, and outdated details.
Fuzzy string matching: Uses similarity measures to compare names and addresses despite small differences, such as “Arun Kumar” and “Arun K.” It handles variations but may produce false matches when different customers have similar details.
Embeddings: Converts customer text into numerical vectors to identify semantic similarity. It can help compare varied address descriptions, but similarity alone cannot reliably establish that two records belong to the same person.
Recommendation: Use a layered approach. First normalise fields and apply exact SQL matching to email and phone. Next, use fuzzy matching on names and addresses to generate candidate pairs. Use embeddings as an additional signal for difficult cases, not as the sole decision-maker. Assign confidence scores and send uncertain matches for human review.

3. Data Requirements
The client must provide:

Customer name, phone number, email address, and postal address.
A labelled sample of record pairs identifying true duplicates and non-duplicates.
Existing customer IDs and, where available, trusted reference identifiers.
Business rules for handling missing, shared, or outdated contact details.
Clean and standardise phone numbers, email addresses, names, and addresses before matching. Remove exact duplicate rows, assess missing values, and check the consistency of labels. The labelled sample should include difficult cases, such as similar names belonging to different people. Protect personal information and restrict access to customer data.

4. Evaluation Metric
Evaluate the system using a labelled test set of duplicate and non-duplicate record pairs.

Precision target: ≥ 98% — Of all pairs predicted as duplicates, at least 98% should be genuine duplicates.
Recall target: ≥ 85% — The system should identify at least 85% of the true duplicate pairs.
Precision is especially important because incorrectly merging two different customers can corrupt records, expose information to the wrong person, and be difficult to reverse. Recall is also important because missed duplicates leave data quality problems unresolved. Measure both metrics and review errors before deployment.

5. Estimated Build Time
Estimated duration: 8–12 working days, assuming the client provides accessible records and labelled examples.

Days 1–2: Review data, requirements, and duplicate definitions.
Days 3–4: Clean and normalise customer fields; prepare labelled pairs.
Days 5–7: Implement exact SQL and fuzzy matching.
Days 8–9: Add embedding-based candidate matching where useful.
Days 10–12: Evaluate precision and recall, configure confidence thresholds, and test the review workflow.
Large datasets, complex integrations, or insufficient labelled data may increase the timeline.

6. Key Trade-offs
Automatic merging is faster and reduces manual effort, but a false match can combine different customers and damage data integrity. Human review is safer for uncertain cases but takes more time. The recommended approach automatically links or merges only highly confident matches after validation, routes medium-confidence pairs to a human review queue, and keeps low-confidence pairs separate. Maintain an audit log and provide a way to reverse approved merges. Prioritise precision over recall when deciding whether to merge records automatically.