from flask import Blueprint, request, jsonify, make_response

jestor_bp = Blueprint('jestor', __name__)


@jestor_bp.route('/api/v1/jestor')
def get_jestor_nf():
    return jsonify({"nome":"teste"})




