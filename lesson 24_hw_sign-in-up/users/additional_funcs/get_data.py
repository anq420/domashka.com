from users.models import Users


def get_all_emails():
    email_list = []
    all_users = Users.objects.values_list("email", flat=True)
    for email in all_users:
        email_list.append(str(email))
    return email_list


def get_all_nicknames():
    nickname_list = []
    all_users = Users.objects.values_list("nickname", flat=True)
    for nickname in all_users:
        nickname_list.append(str(nickname))
    return nickname_list


def hide_email(users):
    user_list = []
    for user in users:
        split_email = user.split("@")
        part_email = split_email[0][:3]
        len_str = len(split_email[0][3:])
        part2_email = split_email[0][3:].replace(split_email[0][3:], "*" * len_str)
        hidden_email = part_email + part2_email + "@" + split_email[1]
        user_list.append(hidden_email)
    return user_list
