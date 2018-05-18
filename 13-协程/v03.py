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

    raise RuntimeError('this line should never run')

he = handle_exception()
next(he)
he.send(10) # recived x: 10
he.send(20) # recived x: 20

he.throw(DemoException) # run demo exception

he.send(40) # recived x: 40
he.close()