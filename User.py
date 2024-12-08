from Parsers import Parser

parser = Parser()
class PublicUser:
    username = None
    data = {}
    def __init__(self, username):
        self.username = username
        self.data = parser.parse_all_data_from_public_user(username)
    
    def get_data(self):
        return self.data