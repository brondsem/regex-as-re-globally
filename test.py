# run from tox.ini

import sys, regex, re, fnmatch, pathlib, glob

# basic test
assert re.__package__ == 'regex', re.__file__
assert re.match('a', 'a')

# issue #4
fnmatch.translate('LICEN[CS]E*')

# make sure its actually usable
re.compile(fnmatch.translate('LICEN[CS]E*'))

# issue #9
pathlib.Path('foo').glob('bar*')

# issue #11
assert glob.escape('ab*') == 'ab[*]'
assert glob.escape(b'ab*') == b'ab[*]'

import tokenize
tokenize.blank_re.match(b'foo')

# check for any other modules with original 're'
bad_attrs = []
for k, v in sys.modules.items():
    assert getattr(v, 're', None) in {None, regex}, f'{k} has reference to original `re`'

"""
    # this is quite aggressive, more than necessary I think
    for attr in dir(v):
        if attr == 'NOFLAG':
            continue
        attr_obj = getattr(v, attr)
        # assert type(attr_obj).__module__ != 're', f'{k}.{attr} has reference to original `re`'
        if type(attr_obj).__module__ == 're':
            bad_attrs.append(f'{k}.{attr} ({type(attr_obj)})')

assert not bad_attrs, bad_attrs
"""
