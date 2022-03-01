## regex_as_re_globally

This package installs a .pth file to site-packages to replace "[re](https://docs.python.org/library/re.html)" with "[regex](https://pypi.org/project/regex/)" globally.
The `regex` package is a backwards-compatible replacement for `re`, with additional features and better performance in some situations.

Run `pip install regex_as_re_globally` to install this package.  It depends on `regex` of course.

The wheel files generated are platform and python specific due to the limitations of wheel files, where the relative directory for site-packages needs to be determined at wheel building time, not install time. The directory is dependent on the version of python and the platform you are on.

This technique is heavily inspired by https://github.com/dougn/coverage_pth and https://nedbatchelder.com/blog/201001/running_code_at_python_startup.html  Thanks! 