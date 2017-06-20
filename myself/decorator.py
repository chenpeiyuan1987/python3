def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("begin call %s" % text);
            result = func(*args, **kw);
            print("end call %s" % text);
            return result;
        return wrapper;
    return decorator;

def log(func):
    def wrapper(*args, **kw):
        print("begin call");
        result = func(*args, **kw);
        print("end call");
        return result;
    return wrapper;
"""
@log
def f():
    pass
f();    
"""
@log
def g():
    pass
g();    
