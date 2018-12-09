from flask import render_template
from flask_wtf import FlaskForm 
from wtforms import fields
from wtforms import SelectField
from wtforms.validators import Required
import numpy as np
from . import app, estimator
from sklearn.externals import joblib


class PredictForm(FlaskForm):
    """Fields for Predict"""

    latitude = fields.DecimalField('Latitude:', places=2, validators=[Required()])
    longitude = fields.DecimalField('Longitude:', places=2, validators=[Required()])
    
    accommodates = SelectField(
        'Accommodates:',
        choices=[('0', '0'),('1', '1'), ('2', '2'),
        ('3', '3'),('4', '4'), ('5', '5'),
        ('6', '6'),('7', '7'), ('8', '8'),('9', '9'),('10', '10'), ('11', '11'),('12', '12'),('13', '13')
        , ('14', '14'),('15', '15'),('16', '16')]
    )
    
    bathrooms = SelectField(
        'Bathrooms:',
        choices=[('0', '0'),('1', '1'), ('2', '2'),
        ('3', '3'),('4', '4'), ('5', '5'),
        ('6', '6'),('7', '7'), ('8', '8'),('9', '9'),('10', '10'), ('11', '11'),('12', '12'),('13', '13')
        , ('14', '14'),('15', '15'),('16', '16')]
    )

    bedrooms = SelectField(
        'Bedrooms:',
        choices=[('0', '0'),('1', '1'), ('2', '2'),
        ('3', '3'),('4', '4'), ('5', '5'),
        ('6', '6'),('7', '7'), ('8', '8'),('9', '9'),('10', '10'), ('11', '11'),('12', '12'),('13', '13')
        , ('14', '14')]
    )
    
    beds = SelectField(
        'Beds:',
        choices=[('0', '0'),('1', '1'), ('2', '2'),
        ('3', '3'),('4', '4'), ('5', '5'),
        ('6', '6'),('7', '7'), ('8', '8'),('9', '9'),('10', '10'), ('11', '11'),('12', '12'),('13', '13')
        , ('14', '14'),('15', '15'),('16', '16')]
    )

    review_scores_mean = SelectField(
        'Review Scores Mean:',
        choices=[('0', '0'),('1', '1'), ('2', '2'),
        ('3', '3'),('4', '4'), ('5', '5'),
        ('6', '6'),('7', '7'), ('8', '8'),('9', '9'),('10', '10')]
    )

    room_type = SelectField(
        'Review Scores Mean:',
        choices=[('1', 'Private room'), ('0', 'Entire home/apt'), ('2', 'Shared room')]
    )

    property_type = SelectField(
        'Property type:',
        choices=[('0', 'Aparthotel'), ('1', 'Apartment'), ('2', 'Bed and breakfast'),
        ('3', 'Boat'), ('4', 'Boutique hotel'), ('5', 'Bungalow'),
        ('6', 'Cabin'), ('7', 'Camper/RV'), ('8', 'Casa particular (Cuba)'),
        ('9', 'Castle'), ('10', 'Cave'), ('11', 'Chalet'),
        ('12', 'Condominium'), ('13', 'Cottage'), ('14', 'Earth house'),
        ('15', 'Guest suite'), ('16', 'Guesthouse'), ('17', 'Hostel'),
        ('18', 'Hotel'), ('19', 'House'), ('20', 'Houseboat'),
        ('21', 'Island'), ('22', 'Loft'), ('23', 'Nature lodge'),
        ('24', 'Other'), ('25', 'Resort'), ('26', 'Serviced apartment'),
        ('27', 'Tent'), ('28', 'Timeshare'), ('29', 'Tiny house'),
        ('30', 'Townhouse'), ('31', 'Train'), ('32', 'Villa')]
    ) 



    submit = fields.SubmitField('Submit')


@app.route('/', methods=('GET', 'POST'))
def index():
    """Index page"""
    form = PredictForm()
    prediction = None

    if form.validate_on_submit():
        # store the submitted values
        submitted_data = form.data
        print(submitted_data)

        # Retrieve values from form
        latitude = submitted_data['latitude']
        longitude = submitted_data['longitude']
        property_type = submitted_data['property_type']
        room_type = submitted_data['room_type']
        accommodates = submitted_data['accommodates']
        bathrooms = submitted_data['bathrooms']
        bedrooms = submitted_data['bedrooms']
        beds = submitted_data['beds']
        review_scores_mean = submitted_data['review_scores_mean']

        


        # Create array from values
        instance = [latitude,longitude,property_type,room_type,accommodates,bathrooms,bedrooms,beds,review_scores_mean]

        instance=[instance]
        
        prediction = estimator.predict(instance)
        
        my_prediction=np.exp(int(prediction[0]))
        
        prediction=my_prediction
    
    
    
        
 
    return render_template('index.html', form=form, prediction=prediction)
