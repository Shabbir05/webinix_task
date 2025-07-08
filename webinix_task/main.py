from flask import Flask, request, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []
task_id_counter = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data:
        abort(400, 'Missing title or description')
    task = {
        'id': task_id_counter,
        'title': data['title'],
        'description': data['description'],
        'is_completed': data.get('is_completed', False)
    }
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    is_completed = request.args.get('is_completed')
    if is_completed is not None:
        filtered_tasks = [t for t in tasks if t['is_completed'] == (is_completed.lower() == 'true')]
        return jsonify(filtered_tasks)
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        abort(404, 'Task not found')
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        abort(404, 'Task not found')
    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    task['is_completed'] = data.get('is_completed', task['is_completed'])
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        abort(404, 'Task not found')
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)
