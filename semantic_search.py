import numpy as np
from sentence_transformers import SentenceTransformer

#load the embedding model
model=SentenceTransformer("all-MiniLM-L6-v2")

#create 10 FAQ questions about HR, IT and payroll
faqs=[
    "How do i reset my password?",
    "What should i do if i cannot access my account?",
    "what is the work from home policy?",
    "how many casual leaves can employees take?",
    "what is the company's leave policy?",
    "when will my salary is credited?",
    "how can i download my payslip?",
    "how do i apply for sick leave?",
    "what are the office working hours?",
    "how can i contact the IT Support team?"
]
#create embeddings for all FAQS
faq_embeddings=model.encode(faqs)

#cosine similarity function using numpy
def cosine_similarity(a,b):
    dot_product=np.sum(a*b)
    magnitude_a=np.sqrt(np.sum(a*b))
    magnitude_b=np.sqrt(np.sum(b*b))

    if magnitude_a==0 or magnitude_b==0:
        return 0.0
    return dot_product/(magnitude_a*magnitude_b)
#semantic search function
def semantic_search(query,top_k=3):
    query_embedding=model.encode([query])[0]
    scores=[]
    for i,faq_embedding in enumerate(faq_embeddings):
        score=cosine_similarity(query_embedding,faq_embedding)
        scores.append((faqs[i],score))
        #sort by similarity score,highest first
        scores.sort(key=lambda x:x[1],reverse=True)
        return scores[:top_k]
#keyword search function
def keyword_search(query):
    query_words=set(query.lower().split())
    results=[]
    for faq in faqs:
        faq_words=set(faq.lower().split())
        #count matching words
        matching_words=query_words.intersection(faq_words)
        if matching_words:
            results.append((faq, len(matching_words)))
    #sort by number of matching words
    results.sort(key=lambda x:x[1],reverse=True)
    return results
#Test the required queries
queries=[
    "i cannot log in",
    "salary credit date",
    "work from here rules"
]
for query in queries:
    print("\n" +"="*60)
    print("QUERY:", query)
    print("\nKeywords search Results:")
    keyword_results=keyword_search(query)
    if keyword_results:
        for faq,score in keyword_results:
            print(f"-{faq}| Matching words:{score}")
        else:
            print("No Matching FAQS found")
    print("\nSemantic Search TOP 3:")
    semantic_results=semantic_search(query,top_k=3)
    for faq,score in semantic_results:
        print(f"-{faq}| Similarity:{score:4f}")
