waterfalls = [{
    "title": "Ниагарский водопад",
    "description": "Самый большой водопад в мире, располагающийся на границе США и Канады",
    "height": 120, # высота в метрах
    "size": 2000 # ширина в метрах
}]

def main():

    def new_waterfall():
        new_dict = dict.fromkeys(['title','description', 'height','size'])
        new_dict['title'] = input('Имя водопада\n')
        new_dict['description'] = input('Его описание\n')
        new_dict['height'] = input('Его высота в метрах\n')
        new_dict['size'] = input('Его ширина в метрах\n')
        waterfalls.append(new_dict)
    
    new_waterfall()

if __name__ == '__main__':
    main()