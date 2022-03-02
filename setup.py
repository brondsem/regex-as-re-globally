from setuptools import setup
from distutils import sysconfig
import sys
import re
from pathlib import Path

site_packages_path = sysconfig.get_python_lib()
try:
    sprem = re.match(
        r'.*(lib[\\/](python\d(\.\d+)*[\\/])?site-packages)', site_packages_path, re.I)
    if sprem is None:
        sprem = re.match(
            r'.*(lib[\\/](python\d(\.\d+)*[\\/])?dist-packages)', site_packages_path, re.I)
    rel_site_packages = sprem.group(1)
except Exception as exc:
    print("I'm having trouble finding your site-packages directory.  Is it where you expect?")
    print("sysconfig.get_python_lib() returns '{}'".format(site_packages_path))
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
