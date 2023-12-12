from flask import Flask, request, jsonify
from llama_cpp import Llama

import os
port = os.environ["SERVICE_PORT"]

app = Flask('eksy-ai-server')
model = None

@app.route('/eksy', methods=['POST'])
def response():
    global model

    try:
        data = request.get_json()

        if 'prompt' in data and 'message' in data and 'maxtokens' in data:
            prompt = data['prompt']
            message = data['message']
            maxtokens = data['maxtokens']
            rqprompt = f'''<s>[INST] <<SYS>>
            {prompt}
            <</SYS>>
            {message} [/INST]'''

            if model is None:
                model_path = './model_data/dataset.gguf'

                model = Llama(model_path=model_path, n_ctx=4096)
            
            output = model(rqprompt, max_tokens=maxtokens, echo=True)

            return jsonify(output)
        else:
            return jsonify({ 'error': 'missing parameters' })
    except Exception as e:
        return jsonify({ 'error': str(e) })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)