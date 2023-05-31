import openai

model = "gpt-3.5-turbo"

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

query = "사직서 양식을 워드로 만들어줘 글씨랑 기호만 들어가면돼"

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
    ,{"role": "user", "content":query}
]

# chatgpt 호출

response = openai.ChatCompletion.create(
    model=model
    ,messages=messages
)
answer = response['choices'][0]['message']['content']




from docx import Document

document = Document()

document.add_heading(str(answer),level=8)

document.save("new.docx")