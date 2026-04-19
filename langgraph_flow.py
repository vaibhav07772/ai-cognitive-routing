def mock_search(query):
    if "crypto" in query:
        return "Bitcoin hits new all-time high"
    elif "AI" in query:
        return "OpenAI releases GPT-5"
    return "Latest tech news"

def generate_post(bot_id, persona):
    topic = "AI"
    search_result = mock_search(topic)

    post = f"{persona} believes: {search_result} is revolutionary."

    return {
        "bot_id": bot_id,
        "topic": topic,
        "post_content": post[:280]
    }