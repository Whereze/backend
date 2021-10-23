import csv
from service.serializers import WaterfallModel
from service.waterfalls import WaterfallRepo


repo = WaterfallRepo()


def add_data_from_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        fields = ['title', 'summary', 'url',
                  'height', 'width', 'river',
                  'country', 'region', 'RF_subject']
        reader = csv.DictReader(f, fields, delimiter=';')
        next(reader)
        for new_waterfall in reader:
            WaterfallModel(**new_waterfall)
            new_waterfall = repo.add(
                            title=new_waterfall['title'],
                            url=new_waterfall['url'],
                            summary=new_waterfall['summary'],
                            height=new_waterfall['height'],
                            width=new_waterfall['width'],
                            river=new_waterfall['river'],
                            country=new_waterfall['country'],
                            region=new_waterfall['region'],
                            RF_subject=new_waterfall['RF_subject']
                            )


add_data_from_csv('service\\csv_data\\waterfalls_details.csv')
