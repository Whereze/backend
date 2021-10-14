from service.models.db import db_session
from service.models.models import WaterfallModel


def add_data_in_db(waterfall):
    content = WaterfallModel(**waterfall)
    print(content)
    db_session.add(content)
    db_session.commit()
