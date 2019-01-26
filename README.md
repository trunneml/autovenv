# VenvFreezer [![Build Status](https://travis-ci.org/trunneml/venvfreezer.svg)](https://travis-ci.org/trunneml/venvfreezer)
Creates a venv from a given requirements.txt file and requirements.*.txt files.

## Installation

Just download venvfreezer.py into your project folder where the requirements.txt is.

```sh
$ wget https://raw.githubusercontent.com/trunneml/venvfreezer/master/venvfreezer.py
```

Or checkout out this repository and run:

```sh
$ pip install .
```

## Usage
Switch into your project folder and run:

```sh
$ python3 -m venvfreezer
```

VenvFreezer will create a venv in the folder `venv` and install all requirements form your `requirements.txt` and requirements.*.txt files.

VenvFreezer also creates a `requirements.lock` file with the exact versions of your requirements (like php composer or npm packages).
You can commit this file to save the tested versions of your requirements without messing up your `requirements.txt`.
The next time you create your venv VenvFreezer will use this `requirements.lock` to recreate a venv with the same versions as before.

To reduce build time VenvFreezer also checks if your `requirements.lock` has changed between two VenvFreezer runs. It will not recreate the venv when nothing has changed. This way you can run VenvFreezer after every `git pull` without wasting build time if nothing has changed on your requirements.
If you still want to recreate the venv just delete the folder (`rm -Rf venv`) and rerun `python venvfreezer`.

For more information run:

```
$ python3 -m venvfreezer --help
```

## Requirements

* Python >= 3.4
* venv (Standard Python lib)
* Linux, Windows or MacOSX

** Hint: ** Under Debian and Ubuntu the standard venv lib must be installed seperate by running:

```
$ sudo apt-get install python3-venv
```

## TODOs

* Detect vagrant and change venv path
* Add upgrade command
* Upload to pypi
