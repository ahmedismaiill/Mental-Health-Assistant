from .rag_core import setup_rag_chain

#####################################################################################################
### This is your entry point. You run this file to start chatting. It imports the setup from rag_core
#####################################################################################################

def main():
    print("Initializing Llama-3.2 with Memory...")

    # Load the configured RAG chain from rag_core.py
    chat_chain = setup_rag_chain()
    
    print("\nSystem ready! Type 'exit' to quit.\n")

    # Set session ID for memory tracking
    session_id = "user_session_1" 

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye! Take care.")
            break
        
        print("\nAssistant is typing...")
        
        try:
            # Invoke the chain
            response = chat_chain.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}}
            )
            
            # Print the AI's response
            print(f"\nAssistant: {response['answer']}\n")
            print("-" * 50)
            
        except Exception as e:
            print(f"\n[Error]: {e}\nPlease check your local Ollama instance.")

if __name__ == "__main__":
    main()