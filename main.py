# Import the Flask module
from flask import Flask, render_template, request, redirect, url_for
import random

is_user = {"login": 1}
# Create an instance of Flask
app = Flask(__name__)
name = "favour"
pword = "frosti"
# Define the routes and functions


@app.route('/')
def index():
    if is_user['login'] == 1:
        return redirect(url_for("login"))

    all_symptoms = ['Fever', 'Chills', 'Headache', 'Sweats', 'Fatigue', 'Muscle aches', 'Nausea and vomiting',
                    'Diarrhea', 'Abdominal pain', 'Generally feeling sick', 'Weakness and fatigue',
                    'Stomach pain', 'Diarrhea or constipation', 'Rash', 'Loss of appetite', 'Cough',
                    'Weight loss', 'Abdominal distention', 'Splenomegaly', 'Hepatosplenomegaly']

    random.shuffle(all_symptoms)
    return render_template('index.html', data=all_symptoms)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passwd = request.form["passwd"]
        if uname == name and passwd == pword:
            is_user['login'] = 0
            return redirect(url_for("index"))
        else:
            return render_template("login.html")
    return render_template("login.html")


@app.route('/result', methods=['POST'])
def result():
    if is_user == False:
        return redirect(url_for("login"))

    malaria_symptoms = ['Fever', 'Chills', 'Headache', 'Sweats', 'Fatigue', 'Muscle aches', 'Nausea and vomiting',
                        'Diarrhea', 'Abdominal pain', 'Generally feeling sick']
    typhoid_symptoms = ['Chills', 'Headache', 'Weakness and fatigue', 'Muscle aches', 'Stomach pain',
                        'Diarrhea or constipation', 'Rash', 'Loss of appetite', 'Cough', 'Weight loss',
                        'Abdominal distention', 'Splenomegaly', 'Hepatosplenomegaly']

    user_symptoms = request.form.getlist('symptoms[]')
    malaria_count = sum(
        symptom in malaria_symptoms for symptom in user_symptoms)
    typhoid_count = sum(
        symptom in typhoid_symptoms for symptom in user_symptoms)

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
