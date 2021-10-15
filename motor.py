from flask import Flask, render_template
motor = Flask(__name__)



@motor.route('/')
def index():
    return render_template("index.html")

@motor.route('/mayor')
def mayor():
    return render_template('mayor.html')

@motor.route('/sanMiguel')
def sanMiguel():
    return render_template('SanMiguel.html')

@motor.route('/enlaces')
def enlaces():
    return render_template('Enlaces.html')


if __name__ == '__main__':
   motor.run(debug=True,port=5000)
