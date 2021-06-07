<div align=center>

[![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-green)](https://github.com/komeilparseh/mozlink/blob/main/LICENSE)
[![CodeQL](https://github.com/komeilparseh/mozlink/workflows/CodeQL/badge.svg)](https://github.com/komeilparseh/mozlink/actions?query=workflow%3ACodeQL)
[![Requirements](https://img.shields.io/badge/Requirements-See%20Here-orange)](https://github.com/komeilparseh/mozlink/blob/main/requirements.txt)

[About_EN](https://komeilparseh.github.io/blog/mozlink/)-[درباره این به فارسی](https://vrgl.ir/yEtRu)

</div>

# mozlink

<div align=center>

![logo](app/static/logo.png)

</div>

A program to build **shortLinks**

[mozlink-komeilparseh.fandogh.cloud](https://mozlink-komeilparseh.fandogh.cloud/)Temporary (perhaps permanent!) service link.

Note: Sometimes links may **not work** due to site updates.

## How to run

1. Install python3, pip3, virtualenv in your system.
2. Clone the project

```console
git clone https://github.com/KomeilParseh/mozlink.git && cd mozlink
```

3. Create a virtualenv named venv using

```console
virtualenv -p python3 venv
```

4. Connect to virtualenv using

```console
source venv/bin/activate
```

5. From the project folder, install packages using

```console
pip install -r requirements.txt
```

6. Now environment is ready. Run it by

```console
python app/main.py
```

## TODO

- [x] Automatically add http and https to url
- [ ] Mysql support
