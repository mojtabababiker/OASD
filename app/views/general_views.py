"""
Application routes module
"""
from flask import render_template
from app import app
from models import db
# from models.forms import LoginForm, AddAdminForm, AddArticelForm


@app.route('/')
@app.route('/home')
def home_page():
    """
    Renders the home page with the latest articles.

    Retrieves the latest articles from the database and renders the home page
    template with the retrieved articles.

    Returns:
        The rendered home page template with the latest articles.
    """
    from models.articals_model import Artical  # pylint: disable=import-outside-toplevel
    articals = db.session.execute(db.select(Artical).order_by(Artical.priority.desc()).limit(3)).scalars()
    return render_template('home_2.html', articals=articals)

@app.route('/about')
@app.route('/about/<id>')
def about_page(id=None):
    """
    Render the about page.

    Args:
        id (str, optional): The ID parameter for the about page. Defaults to None.

    Returns:
        str: The rendered about page HTML.
    """
    return render_template('about.html', id=id)

@app.route('/contacts')
def contacts_page():
    """
    Renders the contact us page.

    Returns:
        The rendered contact us page.
    """
    return render_template('contact_us.html')

@app.route('/causes')
@app.route('/causes/<section>')
def articles(section=None):
    """
    Render the articles page based on the specified section.

    Args:
        section (str, optional): The section of the articles. Defaults to None.

    Returns:
        flask.Response: The rendered template for the articles page.
    """
    from models.articals_model import Artical  # pylint: disable=import-outside-toplevel

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
    Render the article page for the given article ID.

    Args:
        article_id (int): The ID of the article.

    Returns:
        str: The rendered HTML template for the article page.

    Raises:
        NotFound: If the article with the given ID does not exist in the database.
    """
    from models.articals_model import Artical  # pylint: disable=import-outside-toplevel

    article = db.get_or_404(Artical, article_id)
    return render_template('article.html', artical=article)
