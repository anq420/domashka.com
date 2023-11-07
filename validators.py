def check_data(email, password, current_users):
    for user in current_users:
        if user['email'] == email and user['password'] == password:
            return email
    return None

