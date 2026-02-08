def configure_plugin_decorator(func):

    def wrapper(*args):
        co = dict(args)
        return func(**co)

        
    return wrapper
    


