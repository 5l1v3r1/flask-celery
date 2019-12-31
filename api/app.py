from flask import Flask, jsonify
from flask import url_for
from worker import celery
import celery.states as states

app = Flask(__name__)


@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    task = celery.send_task('tasks.add', args=[param1, param2], kwargs={})
    get_result = celery.AsyncResult(task.task_id)
    return jsonify({'status': 200, 'data': get_result.get(timeout=10)})

