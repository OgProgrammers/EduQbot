from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

MODEL_PATH = 'C:\\Users\\Dell\\OneDrive\\Documents\\LLM_project\\app\model'

def load_model():
    try:
        print("Loading model...")
        model = AutoModelForQuestionAnswering.from_pretrained(MODEL_PATH)
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
        print("Model loaded successfully.")
        return qa_pipeline
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def get_answer(question: str, context: str):
    model = load_model()
    if model:
        try:
            result = model(question=question, context=context)
            return result['answer']
        except Exception as e:
            print(f"Error during inference: {e}")
            return "Error during model inference."
    else:
        return "Model could not be loaded."
