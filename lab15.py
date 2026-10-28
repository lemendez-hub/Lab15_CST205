# Lab 15 - Flask, Part 1

# Task 1 - Completed

# Task 2

# Was sick for this class (10/26/2026)

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def task_two():
    return (
        '''
            Hello World!

            <p>ClassmateOne: LOL (Laugh Out Loud)</p>
            <p>ClassmateTwo: LASER (Light Amplification by Stimulated Emission of Radiation)</p>
            <p>ClassmateThree: BRB (Be Right Back)</p>
        '''
    )

# Task 3

@app.route('/florencio')
def template():
    acronym = 'ASAP'
    return render_template('template.html', message = acronym)