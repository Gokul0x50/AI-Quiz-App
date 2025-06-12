from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

GROQ_API_KEY = "you gork api here"

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        questions = generate_questions(topic)
        if questions:
            return render_template("quiz.html", questions=questions)
        else:
            return "Failed to generate questions."
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
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

    return render_template("result.html", score=score, total=len(questions), results=results)

if __name__ == "__main__":
    app.run(debug=True, port=5050)

