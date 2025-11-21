# NHS Signup Screen – Technical Test Submission

This project is my submission for the technical task for the Front-end Developer role application at Sortition Foundation.  
It includes:

- A redesigned version of the provided sign-up screen
- A fully working Flask application that serves the form and the whole application
- A backend that stores the submitted data in a JSON text file
- A written summary of the design recommendations implemented.
- An exported copy of my LLM conversation as required by the brief

---

## 🔧 Project Structure

```
project/
│
├── app.py
├── submissions.json
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── success.html
│
└── static/
    ├── css/style.css
    └── img/...
```

---

## ▶️ How to Run the Application

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Flask server
```bash
python app.py
```

### 3. Visit the app in your browser
```
http://127.0.0.1:5000/
```

---

## 💾 Data Storage

All submitted form entries are appended to **submissions.json**.

This file is treated as a **text file**, as specified in the task requirements.

This README was drafted by me and formatted  with LLM support.

---

## ✔️ Task Requirements Checklist

- [x] Reviewed original page and provided improvement recommendations  
- [x] Implemented an improved and more accessible UI  
- [x] Built a Flask app that serves the form  
- [x] Implemented form submission handling  
- [x] Stored submissions in a text file  
- [x] Ensured page works on small screens and low-tech contexts  
- [x] Included LLM conversation history  
- [x] Final solution emailed as required  

---

## Additional Notes

- The design uses modern semantic HTML5 elements, responsive layout techniques, and accessible input patterns.
- The UI is intentionally simplified to reduce cognitive load and improve conversion rates for users with low digital literacy.
- The form labels, fields, and eligibility checkboxes follow best practices from GOV.UK / NHS design systems.

If you have any questions, I’ll be happy to discuss the work during the interview.
