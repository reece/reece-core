class ImmutableDict(dict):
    """
    dict-like class that prohibits updating of values


    >>> from rcore.types.immutabledict import ImmutableDict

    # initialization as with standard dicts:
    >>> d = ImmutableDict(a=1,b=2)
    >>> d
    ImmutableDict({'a': 1, 'b': 2})

    >>> d = ImmutableDict({'a':1,'b':2})
    >>> d
    ImmutableDict({'a': 1, 'b': 2})

    # setting values as with dicts:
    >>> d['c'] = 3
    >>> d
    ImmutableDict({'a': 1, 'c': 3, 'b': 2})

    >>> d.update({'d': 4})
    >>> d
    ImmutableDict({'a': 1, 'c': 3, 'b': 2, 'd': 4})

    # setting a value to the same value is permitted
    >>> d['c'] = 3

    # resetting values via assignment and update are prohibited
    >>> d['a'] = 3
    Traceback (most recent call last):
    ...
    KeyError: 'key "a" already in immutable dictionary'

    >>> d.update({'a': 4})
    Traceback (most recent call last):
    ...
    KeyError: 'key "a" already in immutable dictionary'
    """
    
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, value):
        if name in self and self[name] != value:
            raise KeyError('key "'+str(name) + '" already in immutable dictionary')
        dict.__setitem__(self, name, value)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)

    def update(self, *args, **kwargs):
        for iterable in args:
            for k, v in iterable.iteritems():
                self[k] = v 
        for k, v in kwargs.iteritems():
            self[k] = v


if __name__ == '__main__':
    import doctest
    doctest.testmod()
