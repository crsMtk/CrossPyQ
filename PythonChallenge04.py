usernameList = []
def unique_user(username):
    if username in usernameList:
        return False
    else:
        usernameList.append(username)
        return True


def unique_user_count():
    return len(usernameList)
