from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key=""  # substitua xxx por sua chave
)


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")

    response = client.chat.completions.create(
        model="deepseek-r1:7b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
        stream=False
    )

    # Retornar a resposta do modelo
    assistant_response = response.choices[0].message["content"]
    return jsonify({"response": assistant_response})


if __name__ == '__main__':
    app.run(debug=True)