class Twitter:

    def __init__(self, token):
        self.token = token

    def connect(self):
        print(f'connecting with ... {self.token}')
