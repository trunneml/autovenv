# VenvFreezer [![Build Status](https://travis-ci.org/trunneml/venvfreezer.svg)](https://travis-ci.org/trunneml/venvfreezer)
Creates a Python 3 venv from a given requirements.txt file and stores the exact version of each installed package, for later recreation of the venv, in a requirements.freeze file. It can also download all dependencies for a later offline build or a faster recreation of the venv.

## Features
 * Uses Python 3 **venv**! No need to install `virtualenv`.
 * Supports **offline** builds! Using `pip wheels`, `pip download` and `pip --find-links`.
 * **Reliable** and **deterministic**! It creates a requirements.freeze file with the exact version of each package like `pip freeze`.
 * **Fast!** It only recreates the venv when the `requirements.freeze` has changed.
 * **Windows**, **Linux** and **MacOSX** are supported.

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

VenvFreezer also creates a `requirements.freeze` file with the exact versions of your requirements (like php composer or npm packages). 
The next time you create your venv VenvFreezer will use this `requirements.freeze` file to recreate a venv with the same versions as before.
You can commit this file to save the tested versions of your requirements without messing up your `requirements.txt`. This also ensures that each developer in your team uses the same dependencies and versions in development.

To reduce build time VenvFreezer also checks if your `requirements.freeze` has changed between two VenvFreezer runs. It will not recreate the venv when nothing has changed. This way you can run VenvFreezer after every `git pull` without wasting build time if nothing has changed on your requirements.
If you still want to recreate the venv just delete the folder (`rm -Rf venv`) and rerun `python venvfreezer`.

You can also download the dependencies for a later offline build or to save network bandwidth by running:

```sh
$ python3 -m venvfreezer download
```

This command creates a new folder `./requirements` that contains all packages (for the current OS) from the `requirements.freeze` file. VenvFreezer uses this folder as a cache for the next venv creation.

For more information run:

```
$ python3 -m venvfreezer --help
```

## Requirements

* Python >= 3.4
* venv (Standard Python lib)
* Linux, Windows or MacOSX

**Hint:** Under Debian and Ubuntu the standard venv lib must be installed seperate by running:

```
$ sudo apt-get install python3-venv
```

## TODOs

* Detect vagrant and change venv path
* Add upgrade command
* Upload to pypi
