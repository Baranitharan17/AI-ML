Technical Proposal: Question Answering for a 60-Page Contract
1. Recommended Approach
Build a Retrieval-Augmented Generation (RAG) system to answer questions from a 60-page contract. The system will extract text from the contract, divide it into smaller sections (chunks), convert those sections into embeddings, and store them in a searchable vector database. When a user asks a question, the system retrieves the most relevant sections and provides them to a Large Language Model (LLM) to generate an answer.

Every answer should include supporting quotations and page references. If the contract does not contain enough information, the system should say that it cannot find a supported answer rather than inventing one. Human review is required for ambiguous clauses and important legal decisions.

2. Data Requirements
The contract in PDF format, with readable text or OCR for scanned pages.
Page numbers and section headings preserved during document processing.
At least 50 representative test questions with expert-reviewed reference answers and source pages.
Secure storage, access permissions, and appropriate handling of confidential contract information.
3. Evaluation Metric and Target
Evaluate the system using at least 50 expert-reviewed questions.

Answer accuracy: At least 90% of answers are judged correct and complete by a reviewer.
Citation accuracy: At least 95% of cited answers point to relevant supporting contract passages.
Unsupported claims: Target zero unsupported claims in the evaluation set; measure and investigate every failure.
These are proposed acceptance targets, not measured results. Test retrieval quality and answer quality separately, including questions whose answers are absent from the contract.

4. Estimated Build Time
Estimated 1–2 weeks for a basic prototype using one contract, assuming access to the required tools and a reviewer.

Days 1–2: Extract and inspect contract text.
Days 3–4: Chunk text, generate embeddings, and configure retrieval.
Days 5–7: Connect the LLM and implement answers with citations.
Remaining time: Evaluate test questions, fix errors, and demonstrate the prototype.
5. Key Trade-offs
Benefits: Answers are grounded in the contract, source passages can be checked, and the system can be evaluated consistently.
Costs: Embedding, storage, and LLM calls add cost; retrieval and document preparation add complexity.
Limitations: Poor OCR, ambiguous legal language, or missed relevant sections can produce incorrect answers.
Safeguards: Restrict document access, log system performance securely, require citations, and escalate high-impact questions to a qualified human reviewer.
Recommendation: Proceed with a small RAG prototype and approve wider use only after it meets the evaluation targets and passes human review.