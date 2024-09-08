from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('log', __name__)


@bp.route('/')
def index():
    db = get_db()
    workouts = db.execute(
        'SELECT l.id, date_time, duration, distance, route_nickname, average_heart_rate, max_heart_rate'
        ' FROM workout_log l '
        ' ORDER BY date_time DESC'
    ).fetchall()
    return render_template('log/index.html', posts=workouts)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        duration = request.form['duration']
        distance = request.form['distance']
        route_nickname = request.form['route_nickname']
        average_heart_rate = request.form['average_heart_rate']
        max_heart_rate = request.form['max_heart_rate']
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
            return redirect(url_for('log.index'))

    return render_template('log/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT l.id, date_time, duration, distance, route_nickname, average_heart_rate, max_heart_rate'
        ' FROM workout_log l '
        ' WHERE l.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        datetime = request.form['date_time']
        duration = request.form['duration']
        distance = request.form['distance']
        route_nickname = request.form['route_nickname']
        average_heart_rate = request.form['average_heart_rate']
        max_heart_rate = request.form['max_heart_rate']
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
            return redirect(url_for('log.index'))

    return render_template('log/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM workout_log WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('log.index'))