"""
Application routes module
"""
import os.path
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import app, db
# from models.forms import LoginForm, AddAdminForm, AddArticelForm
from werkzeug.utils import secure_filename


@app.route('/')
@app.route('/home')
def home_page():
    from models.articals_model import Artical
    articals = db.session.execute(db.select(Artical).order_by(Artical.priority.desc()).limit(3)).scalars()
    return render_template('home_2.html', articals=articals)

@app.route('/about')
@app.route('/about/<id>')
def about_page(id=None):
    return render_template('about.html', id=id)

@app.route('/contacts')
def contacts_page():
    return render_template('contact_us.html')

@app.route('/causes')
@app.route('/causes/<section>')
def articles(section=None):
    from models.articals_model import Artical

    causes = {'education': 'education.html', 'health-care': 'health_care.html',
             'culture': 'culture.html', 'emergency-relief':'crisis.html'}

    if section:
        articals = db.session.execute(db.select(Artical).
                                        filter_by(section=section).
                                        order_by(Artical.priority.desc()).
                                        limit(9)).scalars()
        return render_template(causes[section], articals=articals)
    return render_template('causes.html')

@app.route('/articles/<article_id>')
def article_page(article_id):
    """
    article page route
    """
    from models.articals_model import Artical

    article = db.get_or_404(Artical, article_id)
    return render_template('article.html', artical=article)


#==========================================================================
#                         Admin Routes
#                 ===========================
@app.route('/dash_board')
@login_required
def dash_board():
    """
    admin dash board route functoin
    """
    admin = current_user
    articals = admin.articals
    job_offers = admin.job_offers
    return render_template('admin_templates/dash_board.html', articles=articals, job_offers=job_offers)

#  Login as admin
@app.route('/admin', methods=['GET', 'POST'])
def admin_page(login_message=None):
    from datetime import timedelta
    from models.forms import LoginForm
    form = LoginForm()
    if request.method == "POST":
        from models.admins_model import Admin
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
    logout_user()
    return redirect(url_for('admin_page'))

#  Creating a new admin for teh web app
@app.route('/create_admin', methods=['GET', 'POST'])
@login_required
def create_admin_page():
    from models.forms import AddAdminForm
    form = AddAdminForm()
    if request.method == "POST":
        from models.admins_model import Admin
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
    from models.forms import EditProfileForm
    form = EditProfileForm()

    if request.method == 'POST':
        try:
            current_user.update(form)
            db.session.commit()
            return redirect(url_for('dash_board'))
        except Exception as err:
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
    from models.forms import AddArticelForm
    from models.admins_model import Artical
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