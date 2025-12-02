# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split by commas or whitespace
        parts = re.split(r'[,\s]+', self.addresses.strip())

        # Email pattern: something@something.something
        email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        # Keep only valid emails
        emails = [p for p in parts if re.fullmatch(email_pattern, p)]

        # Return unique, sorted list
        return sorted(set(emails))
