from flask import (
    Blueprint, flash, g, redirect, request, url_for, jsonify
)


from flaskr.log import get_post
from flaskr.db import get_db

bp = Blueprint('api', __name__)


@bp.route('/workouts')
def index():
    data = []
    if request.content_length is not None:
        data = request.get_json(force=True)
    db = get_db()
    workouts = db.execute(
        'SELECT l.id, date_time, duration, distance, route_nickname, average_heart_rate, max_heart_rate'
        ' FROM workout_log l '
        ' ORDER BY date_time DESC'
    ).fetchall()
    workout_list = []
    for workout in workouts:
        filter = False
        workout_dict = {
            'id': workout['id'],
            'date_time': workout['date_time'],
            'duration': workout['duration'],
            'distance': workout['distance'],
            'route_nickname': workout['route_nickname'],
            'average_heart_rate': workout['average_heart_rate'],
            'max_heart_rate': workout['max_heart_rate']
        }
        for key in data:
            if workout_dict[key] != data[key]:
                filter = True
        if not filter:
            workout_list.append(workout_dict)
    return jsonify(workout_list)


@bp.route('/create', methods=('POST',))
def create():
    data = request.get_json()
    duration = data['duration']
    distance = data['distance']
    route_nickname = data['route_nickname']
    average_heart_rate = data['average_heart_rate']
    max_heart_rate = data['max_heart_rate']
    error = None

    if not duration:
        error = 'Duration is required.'
    elif not distance:
        error = 'Distance is required.'

    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute(
            'INSERT INTO workout_log (duration, distance, route_nickname, average_heart_rate, max_heart_rate)'
            ' VALUES (?, ?, ?, ?, ?)',
            (duration, distance, route_nickname, average_heart_rate, max_heart_rate)
        )
        db.commit()
        print(data)
        return redirect(url_for('api.index'))


@bp.route('/<int:id>/update', methods=('PUT',))
def update(id):
    post = get_post(id)
    data = request.get_json()
    datetime = data['date_time']
    duration = data['duration']
    distance = data['distance']
    route_nickname = data['route_nickname']
    average_heart_rate = data['average_heart_rate']
    max_heart_rate = data['max_heart_rate']
    error = None

    if not duration:
        error = 'Duration is required.'

    if error is not None:
        flash(error)
    else:
        db = get_db()
        db.execute(
            'UPDATE workout_log SET date_time = ?, duration = ?, distance = ?, route_nickname = ?, '
            'average_heart_rate = ?, max_heart_rate =? '
            ' WHERE id = ?',
            (datetime, duration, distance, route_nickname, average_heart_rate, max_heart_rate, id)
        )
        db.commit()
        return redirect(url_for('api.index'))


@bp.route('/<int:id>/delete', methods=('DELETE',))
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM workout_log WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('api.index'))
