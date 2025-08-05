from flask import Blueprint, render_template
from pathlib import Path

error_bp = Blueprint(
    name="errors",
    import_name=__name__,
    template_folder=Path(__file__).parents[0].joinpath('templates').as_posix(),

)


@error_bp.app_errorhandler(code=401)
def unauthorized(error):
    return render_template('errors/401.html')


@error_bp.app_errorhandler(code=403)
def forbidder(error):
    return render_template('errors/403.html')


@error_bp.app_errorhandler(code=404)
def page_not_found(error):
    return render_template('errors/404.html')


@error_bp.app_errorhandler(code=500)
def internal_error(error):
    return render_template('errors/500.html')