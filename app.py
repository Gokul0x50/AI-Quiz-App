from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests
import json
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-this-in-production'  # Change this!

GROQ_API_KEY = "you gork api here"

# Database setup
def init_db():
    conn = sqlite3.connect('quiz_app.db')
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Quiz history table
    c.execute('''CREATE TABLE IF NOT EXISTS quiz_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        topic TEXT NOT NULL,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        quiz_data TEXT NOT NULL,
        taken_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    
    conn.commit()
    conn.close()

# Initialize database when app starts
init_db()

def generate_questions(topic):
    prompt = f"""
Generate 5 multiple choice questions on the topic "{topic}". 
Each question should have 4 options (A, B, C, D) and mention the correct answer.
Format:
1. Question?
A) ...
B) ...
C) ...
D) ...
Answer: B
"""
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "llama3-70b-8192"
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)

    try:
        result = response.json()
        print(result)  # 🔍 DEBUG
        content = result['choices'][0]['message']['content']
        return parse_questions(content)
    except Exception as e:
        print("Error:", e)
        return []

def parse_questions(text):
    questions = []
    blocks = text.strip().split("\n\n")
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 6:
            continue
        question = lines[0].split('.', 1)[1].strip()
        options = {
            "A": lines[1][3:].strip(),
            "B": lines[2][3:].strip(),
            "C": lines[3][3:].strip(),
            "D": lines[4][3:].strip()
        }
        answer = lines[5].split(":")[1].strip()
        questions.append({"question": question, "options": options, "answer": answer})
    return questions

def save_quiz_result(user_id, topic, score, total_questions, quiz_data):
    """Save quiz result to database"""
    conn = sqlite3.connect('quiz_app.db')
    c = conn.cursor()
    c.execute('''INSERT INTO quiz_history (user_id, topic, score, total_questions, quiz_data)
                 VALUES (?, ?, ?, ?, ?)''', 
              (user_id, topic, score, total_questions, json.dumps(quiz_data)))
    conn.commit()
    conn.close()

def get_user_quiz_history(user_id):
    """Get user's quiz history"""
    conn = sqlite3.connect('quiz_app.db')
    c = conn.cursor()
    c.execute('''SELECT topic, score, total_questions, taken_at 
                 FROM quiz_history WHERE user_id = ? 
                 ORDER BY taken_at DESC''', (user_id,))
    history = c.fetchall()
    conn.close()
    return history

@app.route("/")
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        
        # Basic validation
        if len(username) < 3:
            flash("Username must be at least 3 characters long")
            return render_template("register.html")
        
        if len(password) < 6:
            flash("Password must be at least 6 characters long")
            return render_template("register.html")
        
        # Check if user already exists
        conn = sqlite3.connect('quiz_app.db')
        c = conn.cursor()
        c.execute("SELECT id FROM users WHERE username = ? OR email = ?", (username, email))
        if c.fetchone():
            flash("Username or email already exists")
            conn.close()
            return render_template("register.html")
        
        # Create new user
        password_hash = generate_password_hash(password)
        c.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                 (username, email, password_hash))
        conn.commit()
        conn.close()
        
        flash("Registration successful! Please login.")
        return redirect(url_for('login'))
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        conn = sqlite3.connect('quiz_app.db')
        c = conn.cursor()
        c.execute("SELECT id, username, password_hash FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash(f"Welcome back, {user[1]}!")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password")
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('index'))

@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Get user's quiz history
    history = get_user_quiz_history(session['user_id'])
    return render_template("dashboard.html", history=history, username=session['username'])

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        topic = request.form["topic"]
        questions = generate_questions(topic)
        if questions:
            # Store topic in session for result page
            session['current_topic'] = topic
            return render_template("quiz.html", questions=questions)
        else:
            flash("Failed to generate questions. Please try again.")
            return redirect(url_for('dashboard'))
    
    return render_template("new_quiz.html")

@app.route("/result", methods=["POST"])
def result():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    questions = json.loads(request.form["questions"])
    score = 0
    results = []

    for i, q in enumerate(questions):
        selected = request.form.get(f"q{i}")
        correct = q["answer"]
        results.append({
            "question": q["question"],
            "selected": selected,
            "correct": correct,
            "is_correct": selected == correct
        })
        if selected == correct:
            score += 1

    # Save quiz result to database
    topic = session.get('current_topic', 'Unknown')
    save_quiz_result(session['user_id'], topic, score, len(questions), results)
    
    return render_template("result.html", score=score, total=len(questions), results=results)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
