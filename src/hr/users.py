import pwd

def get_users():
    users = []
    allusers = pwd.getpwall()
    for user in allusers:
        if user.pw_uid >= 1000:
            users.append({
                'name': user.pw_name,
                'id': user.pw_uid,
                'home': user.pw_dir,
                'shell': user.pw_shell
            })
    return users