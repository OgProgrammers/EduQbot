from flask import Flask, request, jsonify
from flask_cors import CORS
from app.model.model import get_answer  # Import the get_answer function

app = Flask(__name__)

CORS(app, resources={r"/answer": {"origins": "http://127.0.0.1:3000"}})

@app.route('/answer', methods=['POST'])
def answer_question():
    try:
        data = request.get_json()
        question = data.get('question')
        context = data.get('context')

        if not question or not context:
            return jsonify({"error": "Both question and context are required."}), 400

        # Get the answer from the model
        answer = get_answer(question, context)
        return jsonify({"answer": answer})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

