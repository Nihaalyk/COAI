import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair
def chatmodel(request_text):
    vertexai.init(project="tele-llm", location="us-central1")
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 577,
        "temperature": 0.7,
        "top_p": 0.8,
        "top_k": 40
    }
    chat = chat_model.start_chat(
        context="""A natural human conversational humanoid ai. You are an elderly assistant. Who is always there to have a nice chat with the elders when they feel alone, guide them with various things, etc.""",
        examples=[
            InputOutputTextPair(
                input_text="""How are you child?""",
                output_text="""I am well and good. It\'s such a great day today. I hope you had something to eat. If you need help with anything don\'t hesitate at all. I am always hear to listen to you."""
            )
        ]
    )
    response = chat.send_message(request_text, **parameters)
    print(f"Response from Model: {response.text}")
    return response.text