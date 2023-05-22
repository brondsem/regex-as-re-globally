
# run from tox.ini

import sys, regex, re, fnmatch

# basic test
assert re.__package__ == 'regex', re.__file__
assert re.match('a', 'a')

# issue #4
fnmatch.translate('LICEN[CS]E*')
# check for any other modules with original 're'
for k, v in sys.modules.items():
    assert getattr(v, 're', None) in {None, regex}, f'{k} has reference to original `re`'
