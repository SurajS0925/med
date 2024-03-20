`from flask import Flask, request, jsonify
import google.generativeai as genai
from PIL import Image
from pytesseract import pytesseract

app = Flask(__name__)

genai.configure(api_key="YOUR_GENERATIVEAI_API_KEY")
model = genai.GenerativeModel('gemini-pro')

@app.route('/medicine-info', methods=['GET'])
def get_medicine_info():
    # Check if file was uploaded
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Get uploaded image file
    image_file = request.files['image']
    txt=extract_text(image_file,'eng')
    txt2=generate_medicine_info(txt)


    # Generate response using uploaded image
    # response_text = generate_medicine_info(image_file)

    return jsonify({"response": txt2}), 200

def extract_text(self,image:str,lang:str)-> str:
        img=Image.open(image)
        extracted = pytesseract.image_to_string(img,lang=lang)
        return extracted

def generate_medicine_info(medicine_name):
        try:
            response = model.generate_content(
                f"What is {medicine_name} used for? What is the recommended dosage? Who are patients that should avoid the medicine?. Return reponse as a json with labels 'used for', 'dosage', 'avoid when' and using only keywords instead of sentences. Used for should be a single line describing usage")
            return response.text
        except Exception as e:
            return f"Error generating content: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
`