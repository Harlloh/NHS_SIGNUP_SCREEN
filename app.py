from flask import Flask, render_template, request
import json
from datetime import datetime
import os

# Create Flask app
app = Flask(__name__)

# Route 1: Show the registration form
@app.route('/')
def index():
    return render_template('index.html')


# Route 2: Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    """
    Saves form data as JSON (array of objects)
    """
    
    # Get all form data
    form_data = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'firstName': request.form.get('first_name', ''),
        'lastName': request.form.get('last_name', ''),
        'email': request.form.get('email', ''),
        'phone': request.form.get('phone', ''),
        'address': {
            'line1': request.form.get('address1', ''),
            'line2': request.form.get('address2', ''),
            'city': request.form.get('city', ''),
            'postcode': request.form.get('postcode', '')
        },
        'eligibility': {
            'canAttend': True if request.form.get('can_attend') else False,
            'meetsRequirements': True if request.form.get('eligible') else False
        },
        'demographics': {
            'gender': request.form.get('gender', ''),
            'dateOfBirth': {
                'day': request.form.get('dob_day', ''),
                'month': request.form.get('dob_month', ''), 
                'year': request.form.get('year', '')},
            'ethnicGroup': request.form.get('ethnicity', ''),
            'healthConditions': request.form.get('health_conditions', ''),
            'nhsSatisfaction': request.form.get('nhs_satisfaction', ''),
            'educationLevel': request.form.get('education', '')
        },
        'consent': {
            'dataUsage': True if request.form.get('consent') else False,
            'futureContact': True if request.form.get('future_contact') else False
        }
    }
    
    # Read existing data or create new array
    if os.path.exists('submissions.json'):
        with open('submissions.json', 'r', encoding='utf-8') as file:
            try:
                submissions = json.load(file)
            except json.JSONDecodeError:
                submissions = []
    else:
        submissions = []
    
    # Add new submission to array
    submissions.append(form_data)
    
    # Save back to file with pretty formatting
    with open('submissions.json', 'w', encoding='utf-8') as file:
        json.dump(submissions, file, indent=2, ensure_ascii=False)
    
    # Show success page
    return render_template('success.html', name=form_data['firstName'])


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)