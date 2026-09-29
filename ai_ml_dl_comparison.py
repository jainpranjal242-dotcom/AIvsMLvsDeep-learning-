# Veda Technology - Task 10
# Submitted by: Ayush Rajput

topics = [
    ("Artificial Intelligence", "Broad field of intelligent systems",
     "Virtual assistants, expert systems"),
    ("Machine Learning", "Subset of AI that learns patterns from data",
     "Spam detection, recommendation systems"),
    ("Deep Learning", "Subset of ML using multi-layer neural networks",
     "Image recognition, speech recognition, generative AI")
]

for name, definition, examples in topics:
    print("\n" + name)
    print("Definition:", definition)
    print("Examples:", examples)

print("\nRelationship: AI -> ML -> Deep Learning")
