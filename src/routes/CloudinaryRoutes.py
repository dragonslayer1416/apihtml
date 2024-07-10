from flask import Blueprint, request, jsonify
import cloudinary
import cloudinary.uploader
from cloudinary import api
from decouple import config

cloudinary.config(
    cloud_name=config('CLOUD_NAME'),
    api_key=config('API_KEY'),
    api_secret=config('API_SECRET')
)

cloudinary_blueprint = Blueprint('cloudinary_blueprint', __name__)

@cloudinary_blueprint.route('/subir', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'no file'}), 400
    
    file = request.files['file']

    try:
        response = cloudinary.uploader.upload(file, folder='uploads')
        return jsonify({'message': 'file uploaded', 'url': response['secure_url']}), 200
    except Exception as error:
        return jsonify({'error': str(error)}), 500

@cloudinary_blueprint.route('/images', methods=['GET'])
def get_images():
    try:
        response = api.resources(type='upload', prefix='uploads/')
        return jsonify({'message': 'images retrieved', 'images': response['resources']}), 200
    except Exception as error:
        return jsonify({'error': str(error)}), 500
