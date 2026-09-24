import tiktoken

enc = tiktoken.get_encoding("gpt2")

tokens = enc.encode("Hello, I am learning GPT-2!")
print(tokens)

text = enc.decode(tokens)
print(text)