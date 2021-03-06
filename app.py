import datetime
import os

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'APP_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy()
db.init_app(app)

class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    client = db.Column(db.String(), nullable=False)
    client_priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.Date, nullable=False)
    product_area = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Description %r>' % self.description

class RequestForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    client = StringField('client', validators=[DataRequired()])
    client_priority = IntegerField('priority', validators=[DataRequired()])
    target_date = DateField('date')
    product_area = StringField('product area')


@app.route("/", methods=('GET', 'POST'))
def feature_request():
    db.create_all()
    form = RequestForm()
    if form.validate_on_submit():
        feat_request = FeatureRequest(
            title=form.title.data,
            description=form.description.data,
            client=form.client.data,
            client_priority=form.client_priority.data,
            target_date=form.target_date.data,
            product_area=form.product_area.data
        )
        db.session.add(feat_request)
        db.session.commit()
        return redirect(url_for('success'))
    else:
        return render_template('404.html'), 404
    return render_template('request.html', form=form)

@app.route("/list")
def get_list():
    all_reqs = FeatureRequest.query.all()
    return render_template('request_list.html', items=all_reqs)

@app.route("/success")
def success():
    return "Request noted!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

