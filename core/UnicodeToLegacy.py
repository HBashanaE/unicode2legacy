from flask import Blueprint, jsonify, request

unicodeToLegacyBP = Blueprint('unicodeToLegacyBP', __name__)

@unicodeToLegacyBP.route('/uni2leg', methods=['POST'])
def unitoleg():
    request_data = request.form
    print(request_data)
    return jsonify({"message":"success"})