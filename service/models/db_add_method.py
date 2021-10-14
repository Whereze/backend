from service.models.db import db_session
from service.models.models import Waterfall_details


def add_data_in_db(waterfall):
    content = Waterfall_details(**waterfall)
    print(content)
    db_session.add(content)
    db_session.commit()
