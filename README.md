[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/hasii2011/code-ally-basic/graphs/commit-activity)
[![CI](https://github.com/hasii2011/code-ally-basic/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/hasii2011/code-ally-basic/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/codeallybasic.svg)](https://badge.fury.io/py/codeallybasic)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Copilot: No](https://img.shields.io/badge/GitHub_Copilot-No-red?logo=github&style=flat-square)](https://github.com/hasii2011/code-ally-basic/wiki/GitHub-Copilot)

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

> [!NOTE]
> **I do not consent to GitHub's use of this project's code in Copilot.** See our [GitHub Copilot Statement](https://github.com/hasii2011/code-ally-basic/wiki/GitHub-Copilot) for details.

