import toolz


def test_tlz():
    try:
        import importlib
    except ImportError:
        try:
            import tlz
            1/0
        except ImportError as e:
            assert '"tlz" package is not available in Python 2.6' in str(e)
        return
    import tlz
    tlz.curry
    tlz.functoolz.curry
    assert tlz.__package__ == 'tlz'
    assert tlz.__name__ == 'tlz'
    import tlz.curried
    print(tlz.curried.__package__)
    assert tlz.curried.__package__ == 'tlz.curried'
    assert tlz.curried.__name__ == 'tlz.curried'
    tlz.curried.curry
    import tlz.curried.operator
    assert tlz.curried.operator.__package__ in (None, 'tlz.curried')
    assert tlz.curried.operator.__name__ == 'tlz.curried.operator'
    assert tlz.functoolz.__name__ == 'tlz.functoolz'
    m1 = tlz.functoolz
    import tlz.functoolz as m2
    assert m1 is m2
    import tlz.sandbox
    try:
        import tlzthisisabadname.curried
        1/0
    except ImportError:
        pass
    try:
        import tlz.curry
        1/0
    except ImportError:
        pass
    try:
        import tlz.badsubmodulename
        1/0
    except ImportError:
        pass

    assert toolz.__package__ == 'toolz'
    assert toolz.curried.__package__ == 'toolz.curried'
    assert toolz.functoolz.__name__ == 'toolz.functoolz'
    try:
        import cytoolz
        assert cytoolz.__package__ == 'cytoolz'
        #import cytoolz.curried
        assert cytoolz.curried.__package__ == 'cytoolz.curried'
        assert cytoolz.functoolz.__name__ == 'cytoolz.functoolz'
    except ImportError:
        pass

    assert tlz.__file__ == toolz.__file__
    assert tlz.functoolz.__file__ == toolz.functoolz.__file__

    assert tlz.pipe is toolz.pipe
