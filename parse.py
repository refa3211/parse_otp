import re


def parse_otpauth_uri(uri):
        match = re.match(r'otpauth://totp/([^?]+)\?secret=([A-Z0-9]+)', uri)
        secret_match = re.match(r'([A-Z0-9]+)', uri)
        if match:
            name = match.group(1)
            secret = match.group(2)
            return name, secret
        if secret_match:
            name = "Default"
            secret = secret_match.group(1)
            return name, secret
        else:
            raise ValueError("Invalid otpauth URI format")
