=======
db demo
=======

this is a demo.


.. code::

    In [6]: u = User(gym_id=1, _status=2)

    In [7]: db.session.add(u)

    In [8]: db.session.commit()
    INFO:sqlalchemy.engine.base.Engine:INSERT INTO user (gym_id, tags, insert_time, status) VALUES (%(gym_id)s, %(tags)s, %(insert_time)s, %(status)s)
    INFO:sqlalchemy.engine.base.Engine:{'insert_time': None, 'tags': '{}', 'gym_id': 1, 'status': 2}

    In [3]: u = User(gym_id=1, status=2)

    In [4]: db.session.add(u)

    In [5]: db.session.commit()
    INFO:sqlalchemy.engine.base.Engine:INSERT INTO user (gym_id, tags, insert_time, status) VALUES (%(gym_id)s, %(tags)s, %(insert_time)s, %(status)s)
    INFO:sqlalchemy.engine.base.Engine:{'insert_time': None, 'tags': '{}', 'gym_id': 1, 'status': 22}
