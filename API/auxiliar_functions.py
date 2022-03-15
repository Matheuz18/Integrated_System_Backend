def verify_user_only(data):
    try:
        data.get("user")
        return True
    except:
        return False


def verify_user_dict(data):
    try:
        data.get("user")
        data.get("psw")
        return True
    except:
        return False

