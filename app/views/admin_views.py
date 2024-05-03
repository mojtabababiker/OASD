#!/usr/bin/env python3
"""
This module contains all the admin views
"""
import os
import os.path
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app
from models import db


@app.route('/dash_board')
@login_required
def dash_board():
    """
    admin dash board route function
    
    This function renders the admin dashboard template and passes the articles and job offers
    associated with the current admin to the template.
    
    Returns:
        The rendered template with the articles and job offers.
    """
    admin = current_user
    articles = admin.articles
    job_offers = admin.job_offers
    return render_template('admin_templates/dash_board.html',
                           articles=articles, job_offers=job_offers)

#  Login as admin
@app.route('/admin', methods=['GET', 'POST'])
def admin_page(login_message=None):
    """
    Renders the admin login page and handles the login functionality.

    Args:
        login_message (str, optional): A message to display on the login page. Defaults to None.

    Returns:
        A rendered template for the admin login page.
    """
    from datetime import timedelta  # pylint: disable=import-outside-toplevel
    from models.forms import LoginForm  # pylint: disable=import-outside-toplevel
    form = LoginForm()
    if request.method == "POST":
        from models.admins_model import Admin  # pylint: disable=import-outside-toplevel
        if form.validate_on_submit():
            admin = db.session.execute(db.select(Admin).filter_by(
                email=form.email_address.data)
                ).scalar()

            if admin and admin.check_password(form.password.data):
                login_user(admin, remember=True, duration=timedelta(seconds=10800))
                return redirect(url_for('dash_board'))
        login_message = 'Envalid Email or Password'

    return render_template('admin_templates/login.html', form=form, login_message=login_message)

#  Logout
@app.route('/admin/logout')
@login_required
def logout():
    """
    Logs out the current user and redirects to the admin page.

    Returns:
        A redirect response to the admin page.
    """
    logout_user()
    return redirect(url_for('admin_page'))

#  Creating a new admin for teh web app
@app.route('/create_admin', methods=['GET', 'POST'])
@login_required
def create_admin_page():
    """
    Renders the create admin page and handles the creation of a new admin.

    Returns:
        If the request method is GET:
            The rendered template 'admin_templates/add_admin.html' with the AddAdminForm.
        If the request method is POST:
            If the form is valid and the admin is successfully created:
                Redirects to the 'dash_board' route.
            If there are form validation errors:
                Flashes error messages and renders the template 
                'admin_templates/add_admin.html' with the AddAdminForm.
    """
    from models.forms import AddAdminForm  # pylint: disable=import-outside-toplevel
    form = AddAdminForm()
    if request.method == "POST":
        from models.admins_model import Admin  # pylint: disable=import-outside-toplevel
        # create the new Admin and add it to database
        if form.validate_on_submit():

            new_admin = Admin()
            try:
                new_admin.update(form)  # update all the admin atributes
                new_admin.save()
                return redirect(url_for('dash_board'))

            except Exception as err:
                db.session.rollback()
                print(err)
        for err, err_msq in form.errors.items():
            flash(message=err_msq)

    return render_template('admin_templates/add_admin.html', form=form)

@app.route('/admin/edite_profile', methods=['GET', 'POST'])
@login_required
def edite_profile():
    """
    View function for editing the user profile.

    This function handles both GET and POST requests. If the request method is GET,
    it renders the profile.html template with a form pre-filled with the user's current
    profile information. If the request method is POST, it updates the user's profile
    information based on the submitted form data.

    Returns:
        If the form submission is successful, it redirects the user to the dash_board
        route. If there is an error during the form submission, it rolls back the database
        session, prints the error, and renders the profile.html template with the form
        containing the user's current profile information.
    """
    from models.forms import EditProfileForm
    form = EditProfileForm()

    if request.method == 'POST':
        try:
            current_user.update(form)
            db.session.commit()
            return redirect(url_for('dash_board'))
        except Exception as err:  # pylint: disable=broad-except
            db.session.rollback()
            print(err)
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.email_address.data = current_user.email
    form.password.data = current_user.password
    form.confirm_password.data = current_user.password
    form.phone_num.data = current_user.phone_num
    form.x_account.data = current_user.acount_x
    form.facebook_account.data = current_user.acount_fb
    form.insta_account.data = current_user.acount_insta

    return render_template('admin_templates/profile.html', form=form)

@app.route('/create_article', methods=['GET', 'POST'])
@app.route('/admin/<admin_last_name>/new_article', methods=['GET', 'POST'])
@login_required
def create_article(admin_last_name=None):
    """
    Create a new article.

    Args:
        admin_last_name (str, optional): The last name of the admin. Defaults to None.

    Returns:
        Response: The response object.

    Raises:
        None
    """
    from models.forms import AddArticelForm  # pylint: disable=import-outside-toplevel
    from models.admins_model import Artical  # pylint: disable=import-outside-toplevel
    form = AddArticelForm()
    if request.method == 'POST':
        # save the article

        if form.validate_on_submit():
            new_article = Artical()
            new_article.title = form.title.data
            new_article.content_breif = form.content_breif.data
            new_article.content = form.content.data
            new_article.section = form.section.data
            new_article.priority = form.priority.data
            new_article.admin_id = current_user.id

            img = form.image.data
            image_path = secure_filename(img.filename)
            if image_path:
                dir_name = os.path.dirname(app.instance_path)
                extension = os.path.basename(image_path).split(".")[1]
                new_path = os.path.join(dir_name, 'models', 'static', 'artical_images',
                                        f"{new_article.id}.{extension}")
                img.save(new_path)
                image_path = f"{new_article.id}.{extension}"
                print(image_path)
            else:
                # if no image was provided
                image_path = "default.jpg"

            new_article.image_path = image_path
            new_article.save()

            return redirect(url_for('dash_board'), 302)

        for err, err_msq in form.errors.items():
            print(f'{err}:  {err_msq}')
    return render_template('admin_templates/create_article.html', form=form)
