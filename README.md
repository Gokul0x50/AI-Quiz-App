# 🧠 AI Quiz App

A modern web application that generates personalized quizzes using AI technology. Built with Flask and powered by LLaMA AI models, this app creates engaging multiple-choice questions on any topic and tracks your learning progress.

## ✨ Features

- **AI-Powered Quiz Generation**: Generate custom quizzes on any topic using advanced language models
- **User Authentication**: Secure registration and login system with password hashing
- **Progress Tracking**: Complete quiz history with scores and performance analytics
- **Modern UI**: Clean, responsive design built with Tailwind CSS
- **Real-time Results**: Instant feedback with detailed answer explanations
- **Topic Flexibility**: Create quizzes on any subject from programming to history

## 🚀 Demo

![Quiz Dashboard](https://via.placeholder.com/800x400/4F46E5/FFFFFF?text=AI+Quiz+Dashboard)

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with SQL schema
- **AI API**: LLaMA API (Large Language Model Meta AI)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Security**: Werkzeug password hashing
- **Session Management**: Flask sessions

## 📋 Prerequisites

- Python 3.7+
- LLaMA API key (get one from your LLaMA service provider)
- pip (Python package installer)

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-quiz-app.git
cd ai-quiz-app
```

### 2. Install Dependencies

```bash
pip install flask requests werkzeug
```

### 3. Set Up Environment

1. Get your LLaMA API key from your service provider
2. Open `app.py` and replace the API key:

```python
LLAMA_API_KEY = "your_actual_llama_api_key_here"
```

3. Change the secret key for production:

```python
app.secret_key = 'your-super-secret-production-key-here'
```

### 4. Run the Application

```bash
python app.py
```

The app will start on `http://localhost:5050`

## 📁 Project Structure

```
ai-quiz-app/
├── app.py                 # Main Flask application
├── quiz_app.db           # SQLite database (auto-created)
├── static/
│   └── css/
│       └── style.css     # Custom styles
└── templates/
    ├── index.html        # Landing page
    ├── login.html        # User login
    ├── register.html     # User registration
    ├── dashboard.html    # User dashboard
    ├── new_quiz.html     # Quiz topic input
    ├── quiz.html         # Quiz taking interface
    └── result.html       # Quiz results display
```

## 🎯 How It Works

1. **Register/Login**: Create an account or log in to start taking quizzes
2. **Choose Topic**: Enter any topic you want to be quizzed on
3. **AI Generation**: The app uses Groq's AI to generate 5 relevant multiple-choice questions
4. **Take Quiz**: Answer the questions in an intuitive interface
5. **View Results**: Get instant feedback and detailed explanations
6. **Track Progress**: View your quiz history and performance trends

## 🔧 Configuration

### Database Schema

The app automatically creates two tables:

- **users**: Stores user accounts with hashed passwords
- **quiz_history**: Tracks all quiz attempts with scores and timestamps

### API Configuration

Currently configured to use:
- **Model**: LLaMA (Large Language Model Meta AI)
- **Endpoint**: LLaMA API endpoint
- **Questions per quiz**: 5 (customizable in the code)

## 🎨 Customization

### Adding New Features

1. **Different Question Types**: Modify the `generate_questions()` function
2. **More Questions**: Change the prompt in `generate_questions()`
3. **Difficulty Levels**: Add difficulty selection in the topic input form
4. **Categories**: Implement predefined topic categories

### Styling

The app uses Tailwind CSS for styling. You can:
- Modify existing classes in the HTML templates
- Add custom CSS in `static/css/style.css`
- Change the color scheme by updating Tailwind classes

## 🔒 Security Features

- Password hashing using Werkzeug's security functions
- SQL injection protection through parameterized queries
- Session-based authentication
- Input validation for user registration

## 🚀 Deployment

### Local Development

```bash
# Run in debug mode
python app.py
```

### Production Deployment

1. **Update Configuration**:
   ```python
   app.secret_key = 'your-production-secret-key'
   app.debug = False
   ```

2. **Use Production WSGI Server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

3. **Environment Variables** (recommended):
   ```bash
   export LLAMA_API_KEY="your_api_key"
   export SECRET_KEY="your_secret_key"
   ```

## 📊 Database Management

### View Quiz History

```sql
sqlite3 quiz_app.db
SELECT * FROM quiz_history WHERE user_id = 1;
```

### Reset Database

```bash
rm quiz_app.db
# Restart the app to recreate tables
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

**API Key Error**:
- Make sure your LLaMA API key is valid and has proper access
- Check the API key format in `app.py`

**Database Issues**:
- Delete `quiz_app.db` and restart the app to recreate tables
- Check file permissions in the project directory

**Quiz Generation Fails**:
- Verify your internet connection
- Check LLaMA API service status
- Try a different topic (some topics may have content restrictions)

**Styling Issues**:
- Ensure Tailwind CSS is loading from the CDN
- Check browser console for any CSS errors

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LLaMA](https://ai.meta.com/llama/) for providing the AI language model
- [Tailwind CSS](https://tailwindcss.com) for the styling framework
- [Flask](https://flask.palletsprojects.com) for the web framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing [GitHub Issues](https://github.com/yourusername/ai-quiz-app/issues)
3. Create a new issue with detailed information about the problem

---

**Happy Learning! 🎓**

Made with ❤️ and AI
