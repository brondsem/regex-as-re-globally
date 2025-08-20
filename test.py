# run from tox.ini

import sys, regex, re, fnmatch, pathlib

# basic test
assert re.__package__ == 'regex', re.__file__
assert re.match('a', 'a')

# issue #4
fnmatch.translate('LICEN[CS]E*')

# make sure its actually usable
re.compile(fnmatch.translate('LICEN[CS]E*'))

# issue #9
pathlib.Path('foo').glob('bar*')

# check for any other modules with original 're'
for k, v in sys.modules.items():
    assert getattr(v, 're', None) in {None, regex}, f'{k} has reference to original `re`'
