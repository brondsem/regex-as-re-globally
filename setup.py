from setuptools import setup
from distutils import sysconfig
import sys
from pathlib import Path

if sys.argv[1] == 'develop':
    print('This package cannot be used with `pip install -e .` or `python setup.py develop`')
    print('It must be fully installed')
    sys.exit(-1)

site_packages_path = sysconfig.get_python_lib()
try:
    assert site_packages_path.startswith(sys.prefix)
    rel_site_packages = site_packages_path.replace(sys.prefix + '/', '', 1)
except Exception as exc:
    print("I'm having trouble finding your site-packages directory.  Is it where you expect?")
    print("sysconfig.get_python_lib() returns '{}' and sys.prefix returns '{}'".format(site_packages_path, sys.prefix))
    print("Exception was: {}".format(exc))
    sys.exit(-1)

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='regex_as_re_globally',
    version='0.0.1',
    description='Creates a regex_as_re_globally.pth to replace stdlib "re" module with "regex" module globally before any code runs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/brondsem/regex_as_re_globally/',
    author='Dave Brondsema',
    author_email='dave@brondsema.net',
    data_files=[
        (rel_site_packages, ['regex_as_re_globally.pth', ]),
    ],
    # the following forces platform-specific wheel files, since generic wheels are not valid for this package
    # from https://stackoverflow.com/questions/35112511/pip-setup-py-bdist-wheel-no-longer-builds-forced-non-pure-wheels
    has_ext_modules=lambda: True,
    install_requires=[
        'regex>=2022.3.2',
    ],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
    ]
)
