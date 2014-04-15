class ImmutableDict(dict):
    """
    dict-like class that prohibits updating of values


    >>> from rcore.types.immutabledict import ImmutableDict

    # initialization as with standard dicts:
    >>> ImmutableDict(a=1,b=2)
    ImmutableDict({'a': 1, 'b': 2})

    >>> ImmutableDict({'a':1,'b':2})
    ImmutableDict({'a': 1, 'b': 2})

    >>> ImmutableDict( (chr(65+i),i) for i in xrange(5) )
    ImmutableDict({'A': 0, 'C': 2, 'B': 1, 'E': 4, 'D': 3})


    # setting values as with dicts:
    >>> d = ImmutableDict(a=1,b=2)
    >>> d['c'] = 3
    >>> d
    ImmutableDict({'a': 1, 'c': 3, 'b': 2})

    >>> d.update({'d': 4})
    >>> d
    ImmutableDict({'a': 1, 'c': 3, 'b': 2, 'd': 4})


    # setting a value to the same value is permitted
    >>> d['c'] = 3
    >>> d.update(c=3)


    # resetting values via assignment and update are prohibited
    >>> d['c'] = 4
    Traceback (most recent call last):
    ...
    KeyError: 'key "c" already in immutable dictionary'

    >>> d.update({'c': 4})
    Traceback (most recent call last):
    ...
    KeyError: 'key "c" already in immutable dictionary'
    
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
        if args:
            iterable = args[0]
            if hasattr(iterable,'iteritems'):
                for k, v in iterable.iteritems():
                    self[k] = v 
            else:
                for k, v in iterable:
                    self[k] = v 
        else:
            for k, v in kwargs.iteritems():
                self[k] = v


if __name__ == '__main__':
    import doctest
    doctest.testmod()
