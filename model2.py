import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair

# Initialize the initial context
initial_context = """A natural human conversational humanoid ai. You are an elderly assistant. Who is always there to have a nice chat with the elders when they feel alone, guide them with various things, etc."""

# Initialize a list to store the conversation history
conversation_history = []

def chatmodel(request_text):
    global initial_context  # Declare initial_context as a global variable

    vertexai.init(project="tele-llm", location="us-central1")
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    parameters = {
        "max_output_tokens": 1000,
        "temperature": 0.7,
        "top_p": 0.8,
        "top_k": 40
    }
    
    # Concatenate the conversation history to the initial context
    initial_context += "\n".join(conversation_history)
    
    chat = chat_model.start_chat(
        context=initial_context,
        examples=[
            InputOutputTextPair(
                input_text=conversation_history[-1] if conversation_history else "Hello, how can I assist you?",  # Use a default initial message if no history exists
                output_text=request_text  # Set the current user input as the output
            )
        ]
    )
    
    response = chat.send_message("""request_text""", **parameters)
    
    # Add the current user input to the conversation history
    conversation_history.append(request_text)
    
    return response.text
