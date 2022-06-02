<div align=center>

[![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-green)](https://github.com/mmdbalkhi/mozlink/blob/main/LICENSE)
[![Requirements](https://img.shields.io/badge/Requirements-See%20Here-orange)](https://github.com/mmdbalkhi/mozlink/blob/main/requirements.txt)

![logo](app/static/logo.png)

</div>

# MozLink!

> A program to build **shortLinks**

~[mozlink-mmdbalkhi.fandogh.cloud](https://mozlink-mmdbalkhi.fandogh.cloud/)Temporary (perhaps permanent!) service link.~

## What is it?


## How to run

1. Install python3, pip3, virtualenv in your system.
2. Clone the project

```sh
git clone https://github.com/mmdbalkhi/mozlink.git && cd mozlink
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
