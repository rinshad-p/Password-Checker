# check_pwned.py
import requests
import hashlib

def check_pwned(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code == 200:
        hashes = response.text.splitlines()
        for h in hashes:
            if suffix in h:
                count = int(h.split(':')[1])
                return f"Warning: This password has been seen {count} times in data breaches!"
        return "Good news: This password hasn’t been found in known breaches."
    else:
        return "Couldn’t check breach status—API error."