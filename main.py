# Import the Flask module
from flask import Flask, render_template, request
import random

# Create an instance of Flask
app = Flask(__name__)

# Define the routes and functions
@app.route('/')
def index():
    all_symptoms = ['Fever', 'Chills', 'Headache', 'Sweats', 'Fatigue', 'Muscle aches', 'Nausea and vomiting',
                    'Diarrhea', 'Abdominal pain', 'Generally feeling sick', 'Weakness and fatigue',
                    'Stomach pain', 'Diarrhea or constipation', 'Rash', 'Loss of appetite', 'Cough',
                    'Weight loss', 'Abdominal distention', 'Splenomegaly', 'Hepatosplenomegaly']

    random.shuffle(all_symptoms)
    return render_template('index.html', data=all_symptoms)


@app.route('/result', methods=['POST'])
def result():
    malaria_symptoms = ['Fever', 'Chills', 'Headache', 'Sweats', 'Fatigue', 'Muscle aches', 'Nausea and vomiting',
                        'Diarrhea', 'Abdominal pain', 'Generally feeling sick']
    typhoid_symptoms = ['Chills', 'Headache', 'Weakness and fatigue', 'Muscle aches', 'Stomach pain',
                        'Diarrhea or constipation', 'Rash', 'Loss of appetite', 'Cough', 'Weight loss',
                        'Abdominal distention', 'Splenomegaly', 'Hepatosplenomegaly']

    user_symptoms = request.form.getlist('symptoms[]')
    malaria_count = sum(symptom in malaria_symptoms for symptom in user_symptoms)
    typhoid_count = sum(symptom in typhoid_symptoms for symptom in user_symptoms)

    if malaria_count >= 4:
        result = "You may have Malaria."
    elif typhoid_count >= 4:
        result = "You may have Typhoid."
    elif not user_symptoms:
        result = "No Symptom was selected: Please Select a Symptom"
    elif len(user_symptoms) < 4:
        result = "Please select at least four (4) Symptoms"
    else:
        result = "The illness is unknown. Please consult a doctor."

    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
