from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    email = request.form['email']
    text = request.form['text']

    with open('form.txt', 'a',) as f:
            f.write(f"email: {email}")
            f.write(f"text: {text}")

    return render_template('form_result.html', 
                           email=email,
                           text=text
                           )

@app.route('/timer')
def timer():
    target_date = datetime(2050, 1, 1)
    current_date = datetime.now()
 
    time_left = target_date - current_date
 
    return render_template('timer.html', time_left=time_left)


if __name__ == '__main__':
    app.run(debug=True)