from flask import Blueprint, render_template

error_bp = Blueprint(
    name="erros",
    import_name=__name__,
    template_folder=path(__file__).parents[0].joinpath('templates').as_posix(),

)


@error_bp.app_errorhandler(code=404)
def page_not_found():
    return render_template('erros/404.html')