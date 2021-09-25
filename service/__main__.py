from service.clients.twitter import Twitter


def main():
    print('hi')

    twitter_client = Twitter(token='sdkfsfldskjflkdsjfs')
    twitter_client.connect()


if __name__ == '__main__':
    main()