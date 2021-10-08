from service.models.db import db_session
from service.models.models import Waterfall
from service.functional.handles import waterfalls


def save_waterfall_data():
    content = Waterfall(uid=waterfalls['uid'], title=waterfalls['title'],
                        description=waterfalls['description'],
                        height=waterfalls['height'], size=waterfalls['size'])

    db_session.add(content)
    db_session.commit()
