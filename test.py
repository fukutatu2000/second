def f():
    """
    Returns a ** 2
    :return: int exponontiation of a
    """
    a = input("type a number:")
    a = int(a)
    return a ** 2

def g(x):
    """
    Returns str(x)
    :param x: str.
    :return: str of x
    """
    x = str(x)
    return x

def h(a, b, c, d=10, e=100):
    """
    Returns (a + b + c) * d * e
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int default 10.
    :param e: int default 100.
    :return : sum(a,b,c) * d * e
    """
    return (a + b + c) * d * e

def i(x):
    """
    Returns int(x / 2)
    :param x: int.
    :return : int of x / 2
    """
    x = x / 2
    x = int(x)
    return x

def j(y):
    """
    Returns i(x) * 4
    :param y: int.
    :return : int of i(x) * 4
    """
    y = y * 4
    y = int(y)
    return y

def k():
    """
    Returns float(a)
    :return : float(a) or a string
    """
    try:
        a = input("type:") 
        a = float(a)
        return a
    except ValueError:
        print("Invalid input.")
