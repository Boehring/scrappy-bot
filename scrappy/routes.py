import time

from flask import current_app as app

from scrappy import db
from scrappy.models import Store
from scrappy.stores import motoblouz


@app.route('/start', methods=['GET'])
def start():
    while True:
        time.sleep(60)
        return "running"


@app.route('/start/motoblouz', methods=['GET'])
def start_motoblouz():
    motoblouz.process_articles()
    return 'success'


@app.route('/read', methods=['GET'])
def read():
    result = Store.query.filter(Store.name == 'Motocard').first()
    print(result)
    return 'ok'


@app.route('/new', methods=['GET'])
def new():
    new_store = Store('fc-moto', 'fc-moto.com')
    db.session.add(new_store)
    db.session.commit()
    return 'test'
