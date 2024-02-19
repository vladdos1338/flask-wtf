from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())

@app.route('/list_prof/<list>')
def list_prof(list):
    proffesions = ['Строитель', 'Инженер', 'Летчик', 'Врач', 'Юрист', 'Управляющий', 'Тренер', 'Стратег', 'Военный']
    return render_template('list_prof.html', list=list.lower(), proffesions=proffesions)



if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')