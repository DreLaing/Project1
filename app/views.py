"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import myForm
from app.models import userProfile
from datetime import date
from base64 import b64encode
import os
from werkzeug.utils import secure_filename





@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    form = myForm()
    return render_template('profile.html', form=form)


@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    users = userProfile.query.all()
    return render_template('profiles.html', users=users)

@app.route('/profile/<int:userid>', methods=['GET'])
def user_profile(userid):
    user = userProfile.query.filter_by(userid=userid)
    return render_template('user_profile.html', user=user)



@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = myForm()
    error = 'Make sure to fill in each field with correct data'
    if request.method == 'POST' and form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        data = userProfile(
            firstname = form.fname.data,
            lastname = form.lname.data,
            email = form.email.data,
            gender = form.gender.data,
            location = form.location.data,
            bio = form.bio.data,
            image = filename,
            date_created = date.today())

        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        
        db.session.add(data)
        db.session.commit()

        flash('New profile successfully created.', 'success')
        return redirect(url_for('profiles'))
    return render_template('profile.html')
    
    
    




@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
