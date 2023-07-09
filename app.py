from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

openai.api_key = 'YOUR_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json['prompt']

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100
    )
    generated_text = response.choices[0].text.strip()

    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run()
