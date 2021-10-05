waterfalls = [{
    "uid": 1,
    "title": "Ниагарский водопад",
    "description": """Самый большой водопад в мире,
    располагающийся на границе США и Канады""",
    "height": 120,  # высота в метрах
    "size": 2000  # ширина в метрах
}]


def take_uid_waterfall(uid):
    for waterfall in waterfalls:
        uid_waterlall = waterfall['uid']
        if uid == uid_waterlall:
            return f'''{waterfall['title']} - {waterfall['description']}'''


def new_waterfall(title, description, height, size):
    new_dict = dict.fromkeys(['uid', 'title', 'description', 'height', 'size'])
    new_dict['uid'] = 2
    new_dict['title'] = title
    new_dict['description'] = description
    new_dict['height'] = height
    new_dict['size'] = size
    waterfalls.append(new_dict)

#  Уже не актуально, но пусть будет
