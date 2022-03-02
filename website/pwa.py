""" contains routes for PWA setup """

from flask import Blueprint, make_response, send_from_directory

bp = Blueprint('pwa', __name__, url_prefix='')

@bp.route('/manifest.json')
def manifest():
    """ return manifest """
    return send_from_directory('static', 'static/manifest.json')

@bp.route('/service-worker.js')
def service_worker():
    """ return service worker """
    response = make_response(send_from_directory('static', 'static/service-worker.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response
