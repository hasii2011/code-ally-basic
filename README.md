![](https://github.com/hasii2011/code-ally-basic/blob/master/developer/agpl-license-web-badge-version-2-256x48.png "AGPL")

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/hasii2011/code-ally-basic/tree/master.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/hasii2011/code-ally-basic/tree/master)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PyPI version](https://badge.fury.io/py/codeallybasic.svg)](https://badge.fury.io/py/codeallybasic)

This project hosts common artifacts for various projects I am developing.  This package does not include any wxPython dependency.

___

Written by <a href="mailto:humberto.a.sanchez.ii@gmail.com?subject=Hello Humberto">Humberto A. Sanchez II</a>  (C) 2026

## Note 
For all kinds of problems, requests, enhancements, bug reports, etc., please drop me an e-mail.

## Developer Notes
This project uses [buildlackey](https://github.com/hasii2011/buildlackey) for day-to-day development builds.

Also note that this project does not include a `requirements.txt` file.  All dependencies are listed in the `pyproject.toml` file.

#### Install the main project dependencies

```bash
pip install .
```

#### Install the test dependencies

```bash
pip install .[test]
```

#### Install the deploy dependencies

```bash
pip install .[deploy]
```

Normally, the above is not used because this project uses a GitHub workflow that automatically deploys releases.

[Copilot Statement](https://github.com/hasii2011/code-ally-basic/wiki/GitHub-Copilot).

