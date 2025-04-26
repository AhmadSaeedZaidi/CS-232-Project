from flask import Blueprint, render_template, request, redirect, url_for
from queries.menu_queries import get_menu_data

menu_bp = Blueprint('menu_bp', __name__, url_prefix='/menus')

@menu_bp.route('/view')
def view_menus():
    menu_data = get_menu_data()
    return render_template("menu.html", menu_data=menu_data)

@menu_bp.route("/suggestions")
def suggestions():
    return render_template("suggestions.html")

