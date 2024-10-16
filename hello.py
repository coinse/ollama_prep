import ollama

response = ollama.generate(model="llama3.2", prompt="Hello!")
print(response["response"])