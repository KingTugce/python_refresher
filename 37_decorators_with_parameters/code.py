import functools

user = { "username": "Jose", "access_level": "guest"}


#  "make_secure" is the decorative function
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*arg, **kwargs):
            if user["access_level"] == access_level:
                return func(*arg, **kwargs)
            else: f"No {access_level} permissions for {user['username']}."

        return secure_function
    
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())

user = { "username": "Jose", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())