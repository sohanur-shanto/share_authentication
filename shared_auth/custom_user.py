class CustomUser:
    def __init__(self, user_id, mobile_number, email, roles, authenticated=False):
        self.id = user_id
        self.mobile_number = mobile_number
        self.email = email
        self.roles = roles
        self._is_authenticated = authenticated

    @property
    def is_authenticated(self):
        return self._is_authenticated

    def is_vendor(self):
        return 'Vendor' in self.roles

    def is_venue_owner(self):
        return 'Venue Owner' in self.roles

    def is_venue_manager(self):
        return 'Venue Manager' in self.roles