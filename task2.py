
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Create 12 FAQs: HR, IT, Payroll
faqs = [
    {"question": "How do I reset my password?", "category": "IT"},
    {"question": "I cannot access my company account", "category": "IT"},
    {"question": "How do I connect to the office VPN?", "category": "IT"},
    {"question": "How can I report a laptop problem?", "category": "IT"},

    {"question": "What are the work from home rules?", "category": "HR"},
    {"question": "How many casual leaves can I take?", "category": "HR"},
    {"question": "What are the office working hours?", "category": "HR"},
    {"question": "How do I apply for annual leave?", "category": "HR"},

    {"question": "When is salary credited each month?", "category": "Payroll"},
    {"question": "How can I download my payslip?", "category": "Payroll"},
    {"question": "Why is tax deducted from my salary?", "category": "Payroll"},
    {"question": "How do I report an incorrect salary payment?", "category": "Payroll"},
]

questions = [faq["question"] for faq in faqs]

# 2. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate FAQ embeddings
embeddings = model.encode(questions)

print("Embedding shape:", embeddings.shape)


# 3. Implement cosine similarity using NumPy
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)


# 4. Semantic search
def semantic_search(query, top_k=3):
    query_embedding = model.encode([query])[0]

    scores = [
        cosine_similarity(query_embedding, embedding)
        for embedding in embeddings
    ]

    ranked_indices = np.argsort(scores)[::-1][:top_k]

    return [
        {
            "question": questions[i],
            "category": faqs[i]["category"],
            "similarity": round(scores[i], 4)
        }
        for i in ranked_indices
    ]


# 5. Keyword search
def keyword_search(query):
    query_words = set(query.lower().split())
    results = []

    for faq in faqs:
        question_words = set(faq["question"].lower().split())
        common_words = query_words & question_words

        if common_words:
            results.append({
                "question": faq["question"],
                "category": faq["category"],
                "matched_words": sorted(common_words),
                "match_count": len(common_words)
            })

    return sorted(
        results,
        key=lambda item: item["match_count"],
        reverse=True
    )


# 6. Test required queries
test_queries = [
    " i cannot log in",
    "when is salary credited",
    "work from home rules"
]

for query in test_queries:
    print("\n" + "=" * 55)
    print("QUERY:", repr(query))

    print("\nSemantic search:")
    for result in semantic_search(query, top_k=3):
        print(result)

    print("\nKeyword search:")
    for result in keyword_search(query)[:3]:
        print(result)
