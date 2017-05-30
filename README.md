# autovenv
Creates a venv from a given requirements.txt file

## Usage
Just download autovenv.py into your project folder where the requirements.txt is and run:

```sh
$ python ./autovenv.py
```

autovenv will create a venv in the folder `venv` and install all requirements form your `requirements.txt`.

autovenv also creates a `requirements.freeze` with the exect versions of your requirements file like php composer or npm packages. You can commit this file to save the tested development versions of your requirements without messing your `requirements.txt`.
The next time you create your venv autovenv will use this `requirements.freeze` file instead of `requirements.txt`.

To reduce build time autovenv checks if your `requirements.freeze` has changed between two autovenv.py runs or not and will not recreate the venv when nothing has changed. This way you can run autovenv after every `git pull` without wasting build time. If you still want to recreate the venv just delete the folder (`rm -Rf venv`) and rerun `python autovenv.py`.

## Requirements

* Python >= 3.3
* venv (Standard Python lib)
* Linux, Windows or MacOSX

** Hint: ** Under Debian and Ubuntu the standard venv lib must be installed seperate by running:

```
$ sudo apt-get install python3-venv
```
