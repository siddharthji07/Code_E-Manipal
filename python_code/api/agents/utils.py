from langchain_community.embeddings import HuggingFaceEmbeddings

def get_chatbot_response(client, model_name, messages, temperature=0):
    input_messages = []
    for message in messages:
        input_messages.append({"role": message["role"], "content": message["content"]})

    response = client.chat.completions.create(
        model=model_name,
        messages=input_messages,
        temperature=temperature,
        top_p=0.8,
        max_tokens=2000,
    ).choices[0].message.content
    
    return response

def get_embedding(embedding_client, text_input):
    return embedding_client.embed_documents([text_input])

def double_check_json_output(client, model_name, json_string):
    prompt = f"""You will check this JSON string and correct any mistakes that will make it invalid. Then you will return the corrected JSON string. Nothing else. 
    If the JSON is correct, just return it.

    Do NOT return a single letter outside of the JSON string.

    {json_string}
    """

    messages = [{"role": "user", "content": prompt}]

    response = get_chatbot_response(client, model_name, messages)

    return response
