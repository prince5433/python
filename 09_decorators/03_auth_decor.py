from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("access denied, admins only")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(user_role):
    print("access granted to tea inventory")

access_tea_inventory("user")
access_tea_inventory("admin")