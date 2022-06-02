<div align=center>

[![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-green)](https://github.com/mmdbalkhi/mozlink/blob/main/LICENSE)
[![CodeQL](https://github.com/mmdbalkhi/mozlink/workflows/CodeQL/badge.svg)](https://github.com/mmdbalkhi/mozlink/actions?query=workflow%3ACodeQL)
[![Test](https://github.com/mmdbalkhi/mozlink/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/mmdbalkhi/mozlink/actions/workflows/python-app.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/parseh/parseh/badge)](https://www.codefactor.io/repository/github/parseh/parseh)
[![Requirements](https://img.shields.io/badge/Requirements-See%20Here-orange)](https://github.com/mmdbalkhi/mozlink/blob/main/requirements.txt)

[About_EN](https://parseh.github.io/blog/2021/May/04/Mozlink/) | [درباره این به فارسی](https://vrgl.ir/yEtRu)
  

![logo](app/static/logo.png)

</div>

# Moz link

> A program to build **shortLinks**

~[mozlink-mmdbalkhi.fandogh.cloud](https://mozlink-mmdbalkhi.fandogh.cloud/)Temporary (perhaps permanent!) service link.~

## How to run

1. Install python3, pip3, virtualenv in your system.
2. Clone the project

```sh
git clone https://github.com/parseh/mozlink.git && cd mozlink
```

3. Create a virtualenv named venv using

```sh
virtualenv -p python3 venv
```

4. Connect to virtualenv using

```sh
source venv/bin/activate
```

5. From the project folder, install packages using

```sh
pip install -r requirements.txt
```

6. Now environment is ready. Run it by

```sh
python app/main.py
```

## TODO

* [x] ~Automatically add http and https to url~
* [x] ~Mysql support~
* [X] support SqlAlchemy
* [ ] Support Custom short url
