from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

bot_personas = {
    "bot_A": "AI and crypto will solve all problems. Loves Elon Musk.",
    "bot_B": "Tech is destroying society. Hates AI and capitalism.",
    "bot_C": "Focus on money, trading, ROI and finance."
}

persona_embeddings = {
    bot: model.encode(text)
    for bot, text in bot_personas.items()
}

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def route_post_to_bots(post, threshold=0.5):
    post_emb = model.encode(post)
    matched = []

    for bot, emb in persona_embeddings.items():
        sim = cosine_similarity(post_emb, emb)
        if sim > threshold:
            matched.append((bot, round(sim, 2)))

    return matched