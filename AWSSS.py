from flask import render_template
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def AWSSS_home():
    return render_template('AWSSS16_Home.html')

@app.route('/keynote/')
def AWSSS_keynote():
    return render_template('AWSSS16_Keynote.html')

@app.route('/organization/')
def AWSSS_organization():
    return render_template('AWSSS16_Organization.html')

@app.route('/program/')
def AWSSS_program():
    return render_template('AWSSS16_Program.html')

@app.route('/venue/')
def AWSSS_venue():
    return render_template('AWSSS16_Venue.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
