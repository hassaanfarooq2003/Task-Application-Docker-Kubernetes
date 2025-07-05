import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'fallback-secret-key')

mongo_username = os.environ.get('MONGO_USERNAME')
mongo_password = os.environ.get('MONGO_PASSWORD')
mongo_host = os.environ.get('MONGO_HOST', 'mongodb-service')
mongo_port = os.environ.get('MONGO_PORT', '27017')

mongo_uri = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/?authSource=admin"

MONGO_INITDB_ROOT_USERNAME = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
MONGO_INITDB_ROOT_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')

if MONGO_INITDB_ROOT_USERNAME and MONGO_INITDB_ROOT_PASSWORD:
    mongo_uri = os.environ.get('MONGO_URI', f"mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@localhost:27017/")

client = MongoClient(mongo_uri)
db = client[os.environ.get('MONGO_DB', 'taskmanager')]
tasks_collection = db.tasks


@app.route('/')
def index():
    tasks = list(tasks_collection.find())
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    tasks_collection.insert_one({
        'description': task,
        'completed': False
    })
    return redirect(url_for('index'))

@app.route('/complete/<task_id>')
def complete_task(task_id):
    tasks_collection.update_one(
        {'_id': ObjectId(task_id)},
        {'$set': {'completed': True}}
    )
    return redirect(url_for('index'))

@app.route('/delete/<task_id>')
def delete_task(task_id):
    tasks_collection.delete_one({'_id': ObjectId(task_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)