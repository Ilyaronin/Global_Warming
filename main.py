from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('contact.html', button_python=button_python)

@app.route('/submit', methods=['POST'])
def submit_form():
    email = request.form['email']
    text = request.form['text']
    with open('form.txt', 'a',) as f:
            f.write(f"email: {email}/n")
            f.write(f"text: {text}/n")
    return render_template('form_result.html', 
                           email=email,
                           text=text)

@app.route('/timer')
def timer():
    # Устанавливаем целевую дату (2050 год)
    target_date = datetime(2050, 1, 1)
    current_date = datetime.now()

    # Вычисляем разницу во времени
    time_left = target_date - current_date

    # Передаем данные в шаблон
    return render_template('timer.html', time_left=time_left)


if __name__ == '__main__':
    app.run(debug=True)