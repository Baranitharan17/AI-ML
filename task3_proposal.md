Technical Proposal: Answer HR Policy Questions Using RAG + LLM

1. Problem

Employees frequently ask HR questions about leave policies, holidays, attendance, benefits, and company rules. Answering these questions manually takes time and may lead to inconsistent responses. The goal is to build an AI assistant that provides accurate answers based on official HR policy documents while respecting employee access permissions.

2. Recommended Approach

Recommend Retrieval-Augmented Generation (RAG) with a Large Language Model (LLM). The system retrieves relevant sections from approved HR documents and uses them as context for generating an answer. Responses should include source references so employees can verify the information.

- Why not fine-tuning? Fine-tuning requires additional training data and effort, and policy updates may require repeated model updates. It is less suitable as the primary method for frequently changing policy facts.
- Why not plain keyword search? Keyword search can find matching terms but may miss questions expressed in different words and cannot naturally combine relevant information into a clear answer.

RAG is recommended because policies can be updated in the document store without retraining the LLM. Access controls must be applied during retrieval so employees only receive information they are authorised to view.

3. Data Requirements

The client must provide:

- Current, approved HR policy PDFs covering leave, attendance, holidays, benefits, and related topics.
- Policy owners, effective dates, version numbers, and an update frequency, such as monthly reviews or updates whenever policies change.
- An employee access-control matrix based on employee grade or role, identifying which policies each group may access.
- A set of representative HR questions and verified answers for testing.

Documents should be parsed, divided into searchable sections, and indexed in a vector database. Outdated policies must be removed from active retrieval or clearly marked as superseded. Access permissions must be enforced before retrieved content reaches the LLM.

4. Evaluation Metric

Evaluate the assistant using a representative set of HR questions with answers verified by HR.

- Faithfulness: Target ≥ 95% of answers supported by the retrieved policy content.
- Answer relevancy: Target ≥ 90% of answers directly addressing the employee's question.
- Retrieval precision@5: Target ≥ 85% of the top five retrieved passages should be relevant to the question.

Also test permission boundaries, source citations, and questions that cannot be answered from available policies. The system should clearly say when information is unavailable rather than inventing a policy. Targets are initial goals that must be validated during testing.

5. Estimated Build Time

Estimated duration: 10–15 working days, assuming policy documents and access rules are available.

- Days 1–3: Collect documents, review permissions, and prepare test questions.
- Days 4–6: Extract text, split documents, create embeddings, and build the retrieval index.
- Days 7–9: Integrate the LLM, source citations, and access controls.
- Days 10–12: Evaluate retrieval and answer quality, then improve prompts and indexing.
- Days 13–15: Conduct HR review, security testing, and prototype demonstration.

Complex integrations, scanned PDFs, or extensive access-control requirements may increase the estimate.

6. Key Trade-offs

The main trade-off is hallucination risk versus response speed. A fast answer with insufficient evidence may provide incorrect HR guidance, while additional retrieval, validation, and human review can increase response time. RAG reduces risk by grounding answers in approved documents but does not eliminate hallucinations.

The assistant should abstain when evidence is insufficient. HR staff should review sensitive or ambiguous cases, policy conflicts, exceptions, and questions involving legal or employment consequences. This approach balances efficiency, accuracy, employee privacy, and trust.