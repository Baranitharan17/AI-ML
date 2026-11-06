Good morning everyone.

Today, I am presenting my proposal for a question-answering system for a 60-page contract.

The problem is that manually searching a long contract takes time. Users may also misunderstand clauses or miss important information.

My recommended approach is Retrieval-Augmented Generation, or RAG.

First, the system extracts the contract text and divides it into smaller sections. Next, it converts those sections into embeddings and stores them in a searchable database.

When a user asks a question, the system retrieves relevant sections and gives them to a Large Language Model. The model generates an answer using the retrieved information and provides page references and supporting quotations.

The data requirements include the contract PDF, preserved page numbers, secure document storage, and at least 50 test questions with answers reviewed by a domain expert.

For evaluation, my target is at least 90% answer accuracy and 95% citation accuracy on the test set. These are proposed targets that must be validated. Questions that cannot be answered from the contract should not receive invented answers.

The estimated build time is one to two weeks for a basic prototype, assuming the document and tools are available.

The main trade-offs are additional implementation cost, embedding and LLM usage, and the possibility of retrieval errors. To reduce risk, we will use citations, access controls, testing, and human review for ambiguous or important legal questions.

Finally, why not just ask ChatGPT?

ChatGPT can be useful for a one-time question about an uploaded contract. However, a dedicated RAG system can provide a repeatable workflow with controlled document access, consistent source references, measurable performance, and monitoring. We should evaluate whether these extra capabilities justify the additional cost for our use case.

My recommendation is to build a prototype, test it against expert-reviewed questions, and expand its use only if it meets the agreed targets.

Thank you.