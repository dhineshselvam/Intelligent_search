import openai

def summarize(query, docs):
    context = "\n".join([d["abstract"] for d in docs])

    prompt = f"""
    Answer the question using the papers below.

    Question: {query}

    Papers:
    {context}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )

    return response["choices"][0]["message"]["content"]
