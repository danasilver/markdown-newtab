markdown-newtab
===============

[![Build Status](https://travis-ci.org/Undeterminant/markdown-newtab.svg?branch=master)](https://travis-ci.org/Undeterminant/markdown-newtab)
[![PyPI](https://img.shields.io/pypi/v/markdown-newtab.svg)](https://pypi.python.org/pypi/markdown-newtab)
![CC0 License](https://img.shields.io/badge/license-CC0-lightgrey.svg)

This extension modifies the HTML output of Python-Markdown to open all
links in a new tab by adding `target="_blank"`. See `run_tests.py` for
example usage.

To only convert external links (i.e. links to other domains, containing "http"),
instantiate the extension with the `external_only` option set to true.

```python
Markdown(extensions=[NewTabExtension(external_only=True)])
```
