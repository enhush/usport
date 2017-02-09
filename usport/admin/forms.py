# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea


class AddClub(FlaskForm):
    creator = StringField('creator', validators=[DataRequired(message=u'Энэ талбарыг зөв бөглөнө үү!')])
    createdDate = DateField('createdDate', validators=[DataRequired(message=u'Энэ талбарыг зөв бөглөнө үү!')])
    name = StringField('name', validators=[DataRequired(message=u'Энэ талбарыг зөв бөглөнө үү!')])
    email = EmailField('email', validators=[Email(message=u'Энэ талбарыг зөв бөглөнө үү!')])
    website = StringField('website', validators=[DataRequired(message=u'Энэ талбарыг зөв бөглөнө үү!')])
    address = StringField('address', widget=TextArea(), validators=[DataRequired(message=u'Энэ талбарыг зөв бөглөнө үү!')])
    phone = StringField('phone', validators=[DataRequired(message=u'Энэ талбарыг зөв бөглөнө үү!')])
    organizerName = StringField('organizerName', validators=[DataRequired(message=u'Энэ талбарыг зөв бөглөнө үү!')])
    organizerPhone = StringField('organizerPhone', validators=[DataRequired(message=u'Энэ талбарыг зөв бөглөнө үү!')])
    organizerEmail = EmailField('organizerEmail', validators=[Email(message=u'Энэ талбарыг зөв бөглөнө үү!')])
