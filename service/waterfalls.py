from service.models.models import Waterfall
from service.models.db import db_session
from sqlalchemy import or_


class WaterfallRepo:

    def check_by_id(self, waterfall_id) -> bool:
        return Waterfall.query.filter(
                Waterfall.uid == waterfall_id).count() > 0

    def get(self, title: str, detail: str) -> Waterfall:
        if not detail:
            waterfalls = Waterfall.query.filter(
                Waterfall.title.ilike(f'%{title}%')
            ).all()
        else:
            waterfalls = Waterfall.query.filter(
                or_(
                    Waterfall.title.ilike(f'%{title}%'),
                    Waterfall.summary.ilike(f'%{detail}%'),
                    Waterfall.height.ilike(f'%{detail}%'),
                    Waterfall.width.ilike(f'%{detail}%'),
                    Waterfall.river.ilike(f'%{detail}%'),
                    Waterfall.country.ilike(f'%{detail}%'),
                    Waterfall.region.ilike(f'%{detail}%'),
                    Waterfall.RF_subject.ilike(f'%{detail}%')),
            ).all()
        return waterfalls

    def add(self, title: str, summary: str,
            height: str, width: str,
            river: str, country: str,
            region: str, RF_subject: str) -> Waterfall:
        new_waterfall = Waterfall(
                             title=title,
                             summary=summary,
                             height=height,
                             width=width,
                             river=river,
                             country=country,
                             region=region,
                             RF_subject=RF_subject
                             )
        db_session.add(new_waterfall)
        db_session.commit()
        return Waterfall(
                        title=new_waterfall.title,
                        summary=new_waterfall.summary
                        )

    def update(
                self, uid: int, title: str, summary: str,
                height: str, width: str,
                river: str, country: str,
                region: str, RF_subject: str) -> Waterfall:
        waterfall = Waterfall.query.filter(
                    Waterfall.uid == uid
                    ).first()
        waterfall.title = title
        waterfall.summary = summary
        waterfall.height = height
        waterfall.width = width
        waterfall.river = river
        waterfall.country = country
        waterfall.region = region
        waterfall.RF_subject = RF_subject
        db_session.commit()
        return Waterfall(title=waterfall.title, summary=waterfall.summary)

    def delete(self, waterfall_id):
        waterfall_to_delete = Waterfall.query.filter(
                Waterfall.uid == waterfall_id).first()
        db_session.delete(waterfall_to_delete)
        db_session.commit()
