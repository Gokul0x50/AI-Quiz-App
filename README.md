# 🧠 AI Quiz Generator

A dynamic web application that generates personalized quizzes on any topic using AI. Built with Flask and powered by LLaMA model, this application creates engaging multiple-choice questions instantly.

## 📸 Screenshots

### Quiz Generation Interface
![Quiz Generator Interface](screenshot1.png)
*Clean and intuitive interface for entering quiz topics*

### Interactive Quiz Taking
![Quiz Interface](screenshot2.png)
*Dynamic quiz interface with multiple choice questions*

### Detailed Results & Analytics
![Results Page](screenshot3.png)
*Comprehensive score breakdown with correct/incorrect answer analysis*

## ✨ Features

- **🤖 AI-Powered Question Generation**: Leverages LLaMA model for intelligent question creation
- **📱 Responsive Design**: Beautiful, mobile-friendly interface using Tailwind CSS
- **⚡ Real-time Quiz Generation**: Instant quiz creation on any topic
- **📊 Detailed Results**: Comprehensive scoring with answer breakdowns
- **🎯 Multiple Choice Format**: Standard A, B, C, D question format
- **🔄 Unlimited Topics**: Generate quizzes on virtually any subject

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, Tailwind CSS, Jinja2 Templates
- **API**: LLaMA Model API
- **Styling**: Tailwind CSS for modern, responsive design

## 📋 Prerequisites

- Python 3.7+
- Flask
- Requests library
- LLaMA API access

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-quiz-generator.git
   cd ai-quiz-generator
   ```

2. **Install dependencies**
   ```bash
   pip install flask requests
   ```

3. **Configure API Key**
   - Get your LLaMA API key
   - Replace the API key in `app.py`:
   ```python
   API_KEY = "your_actual_api_key_here"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the app**
   - Open your browser and navigate to `http://localhost:5050`

## 📁 Project Structure

```
ai-quiz-generator/
│
├── app.py                 # Main Flask application
├── static/
│   └── css/
│       └── style.css     # Custom CSS styles
├── templates/
│   ├── index.html        # Home page template
│   ├── quiz.html         # Quiz interface template
│   └── result.html       # Results page template
└── README.md
```

## 🎮 How to Use

1. **Enter a Topic**: Type any subject you want to be quizzed on
2. **Generate Quiz**: Click "Generate Quiz" to create 5 AI-powered questions
3. **Take the Quiz**: Answer all multiple-choice questions
4. **View Results**: See your score and detailed answer breakdown

## 🔧 Configuration

### API Settings
```python
# Modify these settings in app.py
API_KEY = "your_api_key"
MODEL = "llama-model"      # Change model if needed
PORT = 5050                # Modify port as required
```

## 🚀 Future Enhancements

- **🔐 User Authentication**: User registration, login, and profile management
- **📊 Progress Tracking**: Track quiz history and performance analytics over time
- **🎯 Difficulty Levels**: Easy, Medium, Hard question generation options
- **⏱️ Timed Quizzes**: Add countdown timers for competitive quiz experience
- **📱 Mobile App**: Native mobile application for iOS and Android
- **🌐 Quiz Sharing**: Share custom quizzes with friends via unique links
- **🏆 Leaderboards**: Compare scores with other users globally
- **🌙 Dark Mode**: Toggle between light and dark theme options
- **🔒 Enhanced Security**: JWT authentication and input validation
- **💾 Database Integration**: PostgreSQL/MongoDB for data persistence
- **📈 Advanced Analytics**: Detailed performance insights and learning recommendations
- **🎨 Custom Themes**: Multiple UI themes and customization options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Report bugs or request features via GitHub Issues
- **Documentation**: Check the wiki for detailed documentation
- **Contact**: Reach out for support or collaboration opportunities

---

Made with ❤️ by Gokul P | ⭐ Star this repo if you found it helpful!
