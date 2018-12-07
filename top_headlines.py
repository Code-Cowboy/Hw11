# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 20:06:53 2018

@author: 26614
"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)

if __name__ == '__main__':
    app.run(debug=True)