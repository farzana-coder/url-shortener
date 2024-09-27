from flask import Blueprint, request, redirect, abort, jsonify
from core.compute import generate_short_url
from core.crud import save_url, get_long_url, exists

api_routes = Blueprint('api', __name__)


@api_routes.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()

    if 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400

    long_url = data['url']

    existing_short_url = exists(long_url)

    if existing_short_url:
        return jsonify({'short_url': existing_short_url}), 200

    short_url = generate_short_url()

    save_url(short_url, long_url)

    return jsonify({'short_url': short_url}), 200


@api_routes.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    long_url = get_long_url(short_url)

    if long_url:
        return redirect(long_url)
    else:
        abort(404)
