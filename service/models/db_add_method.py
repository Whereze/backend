from service.models.db import db_session
from service.models.models import Waterfall


def save_waterfall_data(waterfall):
    content = Waterfall(**waterfall)
    db_session.add(content)
    db_session.commit()
