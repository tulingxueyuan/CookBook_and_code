class DemoException(Exception):
    """
    custom exception
    """
    pass

def handle_exception():
    print('-> start')

    while True:
        try:
            x = yield
        except DemoException:
            print('-> run demo exception')
        else:
            print('-> recived x:', x)


he = handle_exception()
next(he)
he.send(10) # recived x: 10
he.send(20) # recived x: 20


try:
    he.send(40) # recived x: 40
    he.close()
    he.send(50) # recived x: 40
    he.close()
except Exception as e:
    print(str(e))
    print(e.value)
