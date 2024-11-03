from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user




app = Flask(__name__)
app.secret_key = 'nexusloveyou' 

# Routes
@app.route('/')
def ghar():
    return render_template('index.html')

@app.route('/oneshotwebdev')
def oneshotwebdev():
    return render_template('oneshot.html')







if __name__ == '__main__':
    app.run()