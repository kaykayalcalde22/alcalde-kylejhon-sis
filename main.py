from flask import Flask,render_template,request,redirect
from users import users

app = Flask(__name__) 


@app.route('/')
def index():
    return render_template(login.html)

@app.route('/home')
def home():
    return 'This is Home'

@app.route('/login')
def login():
    return 'This is a Sample login'

if __name__== '__main__':
    app.run()

    @app.route('/Student-list')
def student_list()

        students = Students.get_all()

        return render_template ('students_list.html'), Student=students


    if__name__=='__main__':
        app.()