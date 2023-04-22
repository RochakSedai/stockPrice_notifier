from flask import Blueprint
from controllers.views import index, getstock, subscribe, searchStock

blueprint = Blueprint('home', __name__, template_folder='/templates')
blueprint.route('/', methods=['GET'])(index)
blueprint.route('/stock/', defaults={'stock_symbol': None}, methods=['GET'])(getstock)
blueprint.route('/stock/<stock_symbol>', methods=['GET'])(getstock)
blueprint.route('/search', methods=['POST'])(searchStock)
blueprint.route('/subscribe', methods=['POST'])(subscribe)