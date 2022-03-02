## regex_as_re_globally

This package does very unusual things, and you normally don't need it.
It helps you use the "[regex](https://pypi.org/project/regex/)" package which is a backwards-compatible replacement for `re`, with additional features and better performance in some situations (and worse performance in others).
Normally you can put `import regex as re` in your .py files and that's all you need.

However, if you want to use `regex` instead of `re` across your whole environment, even within 3rd-party libraries, then this package is for you.

Run `pip install regex_as_re_globally` to install this package.
It will create a .pth file in site-packages which modifies `sys.modules` so that `regex` is used _everywhere_ instead of `re`.
**This changes behavior within the whole python environment.**

The wheel files generated are platform and python specific due to the limitations of wheel files, where the relative directory for site-packages needs to be determined at wheel building time, not install time. The directory is dependent on the version of python and the platform you are on.

The site-packages .pth technique is heavily inspired by https://github.com/dougn/coverage_pth and https://nedbatchelder.com/blog/201001/running_code_at_python_startup.html  Thanks!
