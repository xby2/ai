from flask import Flask, request, jsonify
from llama_cpp import Llama

app = Flask('eksy-ai-server')
model = None

@app.route('/eksy', methods=['POST'])
def response():
    global model

    try:
        data = request.get_json()

        if 'prompt' in data and 'message' in data:
        # if 'message' in data:
            prompt = data['prompt']
            # prompt = 'You are a helpful assistant.'
            message = data['message']
            rqprompt = f'''<s>[INST] <<SYS>>
            {prompt}
            <</SYS>>
            {message} [/INST]'''

            if model is None:
                model_path = './model_data/llama-2-7b-chat.Q2_k.gguf'

                model = Llama(model_path=model_path, n_ctx=4096)
            
            output = model(rqprompt, max_tokens=4096, echo=True)

            return jsonify(output)
        else:
            return jsonify({ 'error': 'missing parameters' })
    except Exception as e:
        return jsonify({ 'error': str(e) })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)


# model_path = './data/llama-2-7b-chat.Q2_K.gguf'

# model = Llama(model_path=model_path)

# system_message = 'You are a helpful assistant'
# user_message = 'How tall is the tallest mountain in Africa'

# prompt = f'''<s>[INST] <<SYS>>
# {system_message}
# <</SYS>>
# {user_message} [/INST]'''

# max_tokens = 4096

# output = model(prompt, max_tokens=max_tokens, echo=True)

# print(output)
