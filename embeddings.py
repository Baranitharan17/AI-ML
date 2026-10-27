from sentence_transformers import SentenceTransformer
import numpy as np

#Create embeddings for these 6 sentences: 'How do I reset my password?', 'I forgot my login
#credentials', 'What is the leave policy?', 'How many casual leaves do I get?', 'The weather in
#Chennai is hot', 'Office timings are 9 to 6'

# #load the embedding model
model=SentenceTransformer("all-MiniLM-L6-v2")

# #define the 6 sentences
sentences=[
    "How do i reset my password?",
    "I forgot my login credentials",
    "What is the leave policy?",
    "How many casual leaves do i get?",
    "The weather in Chennai is hot",
    "Office timings are 9 to 6"
]

#create embeddings
embeddings=model.encode(sentences)

# #print each sentence and its embedding
# for sentence, embedding in zip(sentences, embeddings):
#     print("\nSentence:",sentence)
#     print("Embedding:",embedding)
#     print("Embedding dimensions:",len(embedding))
#     print("\nAll embeddings shape:",embeddings.shape)

# #Print the shape of one embedding vector
# print("Embedding shape:",embeddings[0].shape)

def cosine_similarity(a,b):
    dot_product=np.sum(a*b)
    magnitude_a=np.sqrt(np.sum(a*b))
    magnitude_b=np.sqrt(np.sum(b*b))

    similarity=dot_product/(magnitude_a*magnitude_b)

    return similarity

# a=np.array([1,2,3])
# b=np.array([4,5,6])
# result=cosine_similarity(a,b)
# print("Cosine Similarity:",result)

#Print the 6x6 similarity matrix and the 3 most similar pairs

#create 6*6 similarity matrix
n=len(embeddings)
similarity_matrix=np.zeros((n,n))

for i in range(n):
    for j in range(n):
        similarity_matrix[i,j]=cosine_similarity(
            embeddings[i],embeddings[j]
        )

#print the similarity matrix
np.set_printoptions(precision=3,suppress=True)
print("6*6 cosine similarity matrix:")
print(similarity_matrix)

#find the 3 most similar unique pairs
pairs=[]

for i in range(n):
    for j in range(i+1,n):
        pairs.append((
            similarity_matrix[i,j],
            sentences[i],
            sentences[j]
        ))
pairs.sort(key=lambda x:x[0],reverse=True)

print("\nTop 3 Most Similar sentence pairs:")
for score,sentence1,sentence2 in pairs[:3]:
    print(f"\nSimilarity:{score:4f}")
    print(f"Sentence 1:{sentence1}")
    print(f"Sentence 2:{sentence2}")