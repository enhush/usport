# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, url_for
from .forms import AddClub

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
def index():
    return render_template('admin/index.html')


@blueprint.route('/add-club', methods=["GET", "POST"])
def add_club():
    form = AddClub()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('admin/add-club.html', form=form)
