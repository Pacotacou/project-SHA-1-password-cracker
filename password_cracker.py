import hashlib

def crack_sha1_hash(hash, use_salts = False):
    known_passwords = get_from_file('top-10000-passwords.txt')

    if use_salts:
        salted_passwords = {}
        top_salts = get_from_file('known-salts.txt')
        for bsalt in top_salts:
            for bpassword in known_passwords:
                prepended = hashlib.sha1(bsalt + bpassword).hexdigest()
                appended = hashlib.sha1(bpassword + bsalt).hexdigest()
                salted_passwords[prepended] = bpassword.decode('utf-8')
                salted_passwords[appended] = bpassword.decode('utf-8')
        if hash in salted_passwords:
            return salted_passwords[hash]
    
    passwords_dict = {}
    for p in known_passwords:
        hash_line = hashlib.sha1(p).hexdigest()
        passwords_dict[hash_line] = p.decode('utf-8')
    
    if hash in passwords_dict:
        return passwords_dict[hash]
    
    return 'PASSWORD NOT IN DATABASE'
 
def get_from_file(file_name):
    passwords = []
    with open(file_name, 'rb') as f:
        line = f.readline().strip()
        while line:
            passwords.append(line)
            line = f.readline().strip()
    return passwords
    

