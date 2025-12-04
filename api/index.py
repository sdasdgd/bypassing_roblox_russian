from flask import Flask, render_template, request, flash, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

# Данные для портфолио
projects = [
    {
        'id': 1,
        'title': 'Умный чат-бот',
        'description': 'ИИ-ассистент на Python с NLP',
        'image': 'project1.jpg',
        'tags': ['Python', 'AI', 'Flask']
    },
    {
        'id': 2,
        'title': 'Веб-аналитика',
        'description': 'Панель мониторинга данных в реальном времени',
        'image': 'project2.jpg',
        'tags': ['JavaScript', 'D3.js', 'API']
    },
    {
        'id': 3,
        'title': 'Мобильное приложение',
        'description': 'Кроссплатформенное приложение для iOS/Android',
        'image': 'project3.jpg',
        'tags': ['React Native', 'Firebase']
    }
]

skills = [
    {'name': 'Python', 'level': 95},
    {'name': 'Flask/Django', 'level': 90},
    {'name': 'JavaScript', 'level': 85},
    {'name': 'HTML/CSS', 'level': 95},
    {'name': 'React', 'level': 80},
    {'name': 'PostgreSQL', 'level': 85}
]

@app.route('/')
def home():
    return render_template('index.html', skills=skills, projects=projects[:3])

@app.route('/projects')
def all_projects():
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Здесь можно добавить логику отправки email
        flash(f'Спасибо, {name}! Ваше сообщение отправлено.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project is None:
        return render_template('404.html'), 404
    return render_template('project_detail.html', project=project)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
