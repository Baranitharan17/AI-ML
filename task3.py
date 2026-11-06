import tiktoken

# 1. Four text samples
texts = [
    "Hello, how are you?",
    "I cannot log in to my account.",
    "When will my salary be credited?",
    "Please explain the work from home policy."
]

# Use the encoding specified for this exercise
encoding = tiktoken.get_encoding("cl100k_base")

print("TOKEN COUNT REPORT")
print("-" * 55)

for i, text in enumerate(texts, start=1):
    tokens = encoding.encode(text)
    words = len(text.split())
    token_count = len(tokens)

    words_per_token = (
        words / token_count if token_count > 0 else 0
    )

    print(f"\nText {i}: {text}")
    print("Word count:", words)
    print("Token count:", token_count)
    print("Words per token:", round(words_per_token, 3))
