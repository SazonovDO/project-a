class User():
    def __init__(self, user_id):
        self.id = user_id
        self.name = ''
        self.anonymous = False
        self.authenticated = False
        self.active = True

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return self.anonymous

    def get_id(self):
        return self.id
